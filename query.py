import pyllegro
import requests
import json
from pprint import pprint


def get_offer_list(token, phrase, price_min, price_max) -> dict:
    """
    This method returns list of item offers considering phrase, price min
    and price max parameters
    """

    # send request taking params under consideration: phrase, min price and  max price
    offer_list_url = "https://api.allegro.pl/offers/listing"
    response = requests.get(offer_list_url,
                            params={
                                'phrase': phrase,
                                'sellingMode.format': "BUY_NOW",
                                'price.from': price_min,
                                'price.to': price_max,
                                'sort': "+withDeliveryPrice",
                                'limit': "100"
                            },
                            headers={
                                'Authorization': f'Bearer {token}',
                                'Accept': 'application/vnd.allegro.public.v1+json'
                            }
                           )

    # return json response
    return json.loads(response.text)


def get_offer_list_no_price(token, phrase) -> dict:
    """
    This method returns offer list considering only phrase parameter
    """

    # send request taking params under consideration: phrase
    offer_list_url = "https://api.allegro.pl/offers/listing"
    response = requests.get(offer_list_url,
                            params={
                                'phrase': phrase,
                                'sellingMode.format': "BUY_NOW",
                                'sort': "+withDeliveryPrice",
                                'limit': "100"
                            },
                            headers={
                                'Authorization': f'Bearer {token}',
                                'Accept': 'application/vnd.allegro.public.v1+json'
                            }
                           )

    # return json response
    return json.loads(response.text)

def get_seller_reputation(token, seller_id) -> dict:
    # get rating of specified seller
    response = requests.get(
        f'https://api.allegro.pl/users/{seller_id}/ratings-summary',

        headers={
            'Authorization': f'Bearer {token}',
            'Accept': 'application/vnd.allegro.public.v1+json'
        }
    )

    if response.status_code == 200:
        return json.loads(response.text)['recommendedPercentage']
    else:
        return "No reputation"

def check_for_reputation(token, json_list,  reputation_min, item_index, price_min=None, price_max=None):
    # convert reputation min to float
    reputation_min = float(reputation_min)    
    # sort all items considering price parameter
    all_items = sum(json_list["items"].values(), [])
    sorted_items = sorted(all_items, key=lambda x: float(x["sellingMode"]["price"]["amount"]))
    
    # list of all products with given params
    offer_list = []
    for item in sorted_items:
        # item price
        price = float(item["sellingMode"]["price"]["amount"])
        # cheapest delivery cost
        delivery = float(item["delivery"]["lowestPrice"]["amount"])

        # check if full price fits user price range
        reputation = "No reputation"
        if price_min != None and price_max != None:
            if price_min <= price + delivery <= price_max:
                reputation = get_seller_reputation(token, item["seller"]["id"])
        else:
            reputation =  get_seller_reputation(token, item["seller"]["id"])

        # validate reputation
        if reputation != "No reputation":
            temp = float(reputation.replace(",", "."))
            if temp >= reputation_min:
                offer_list.append({'id': item["id"], 'name': item["name"], 
                                   'full_price': price + delivery,
                                   'price': price, 'delivery_price': delivery,
                                   'seller_id': item["seller"]["id"],
                                   'item_index': item_index})
                # only 5 items allowed?
                if len(offer_list) == 5:
                    break
    # return list with all products, if no products found list is empty
    return offer_list


def get_seller_offers(token, seller_id, phrase, item_index, price_min=None, price_max=None):
    # This method list all offers from particular seller
    # specify seller with seller_id

    if price_min != None and price_max != None:
        offers_url = "https://api.allegro.pl/offers/listing"
        response = requests.get(offers_url,
                               params={
                                   'seller.id': seller_id,
                                   'phrase': phrase,
                                   'price.from': price_min,
                                   'price.for': price_max,
                                   'limit': "10"
                               },
                               headers={
                                   'Authorization': f'Bearer {token}',
                                   'Accept': 'application/vnd.allegro.public.v1+json'
                               }
                              )
    else:
        offers_url = "https://api.allegro.pl/offers/listing"
        response = requests.get(offers_url,
                               params={
                                   'seller.id': seller_id,
                                   'phrase': phrase,
                                   'limit': "10"
                               },
                               headers={
                                   'Authorization': f'Bearer {token}',
                                   'Accept': 'application/vnd.allegro.public.v1+json'
                               }
                              )

    seller_offers_json = json.loads(response.text)
    
    # sort all offers
    all_items = sum(seller_offers_json["items"].values(), [])
    sorted_items = sorted(all_items, key=lambda x: float(x["sellingMode"]["price"]["amount"]))
    if sorted_items:
        item = sorted_items[0]
        # item price
        price = float(item["sellingMode"]["price"]["amount"])
        # cheapest delivery cost
        delivery = float(item["delivery"]["lowestPrice"]["amount"])

        return {'id': item["id"], 'name': item["name"], 'price': price,
                       'delivery_price': delivery, 'seller_id': item["seller"]["id"], 'item_index': item_index}
    else:
        return []


def get_unique_list(list_):
    tmp_set = set(list_)
    return list(tmp_set)


def algorithm(token, param_list):
    item_list = []
    seller_list = []
    item_index_list = []

    # get list of the cheapest offers per item
    for item_index, item in enumerate(param_list, start=1):
        # response from API considering given parameters
        # return offer in format ["id", "name", "price", "seller_id"]
        full_response = get_offer_list(token, item[0], float(item[1]), float(item[2]))
        offer_list = check_for_reputation(token, full_response, float(item[3]), item_index, float(item[1]),
                                          float(item[2]))

        # print(offer_list)

        # simple debug
        print("Basic cheapest offers: {}".format(item[0]))
        pprint(offer_list)
        if offer_list:
            item_list.append(offer_list[0])
            seller_list.append(offer_list[0]['seller_id'])
            item_index_list.append(item_index)
            # break
            # else:
            #     full_response = get_offer_list_no_price(token, item[0])
            #     offer_list = check_for_reputation(token, full_response,
            #                                       float(item[3]), item_index)

        # simple debug
        print("Basic cheapest offers after price correction: {}".format(item[0]))
        pprint(offer_list)

    print("item_list")
    pprint(item_list)

    # get unique sellers
    seller_list = get_unique_list(seller_list)
    print("unique sellers {}".format(seller_list))
    all_sellers_offers = []
    for seller_id in seller_list:
        # offers per one seller
        one_seller_offers = []

        for item_index, item in enumerate( param_list, start = 1):
            best_item = get_seller_offers(token, seller_id, item[0],
                                          item_index, float(item[1]), float(item[2]))
            for i in range(2):
                # repeat only one time if best_item empty
                if best_item:
                    one_seller_offers.append(best_item)
                    break
                else:
                    best_item = get_seller_offers(token, seller_id, item[0],
                                                  item_index)

        #one_seller_offers = sum(one_seller_offers[])
        sorted_items = sorted(one_seller_offers, key=lambda x:
                              float(x["delivery_price"]), reverse=True)
        # get highest delivery price of seller
        delivery_price = sorted_items[0]["delivery_price"]

        sum_offers = 0
        #for item in one_seller_offers:
        #    sum_offers = sum_offers + float(item["price"])

        for item_index in item_index_list:
            # if item with item_index not in one_seller_offers, than add it
            # from item_list
            check_item = next((item for item in one_seller_offers if item["item_index"] == item_index), None) 
            # check if item exist in one_seller_offers
            if not check_item == None:
                sum_offers = sum_offers + float(check_item["price"])
            else:
                original_list_item = next((item for item in item_list if item["item_index"] == item_index), None)
                one_seller_offers.append(original_list_item)
                sum_offers += original_list_item["full_price"]

        # add price for the most expensive delivery
        sum_offers = sum_offers + float(one_seller_offers[0]["delivery_price"])
        one_seller_offers.append({'total_price': sum_offers})
        print("one_seller_offers, seller: {}".format(seller_id))
        pprint(one_seller_offers)
        # add seller offers to all sellers offers
        all_sellers_offers.append(one_seller_offers)

    # price total of original item listing with deliveries
    sum_items = 0
    for item in item_list:
            sum_items = sum_items + float(item['price'])

    if sum_items != 0:
        item_list.append({'total_price': sum_items})

        # all offers in one list
        all_sellers_offers.append(item_list)
    print("all_sellers_offers")
    pprint(all_sellers_offers)
    # sort all offers after price, that is the last value in a list
    sorted_items = all_sellers_offers
    # if at least one offer prepared
    if len(all_sellers_offers) > 0:
        sorted_items = sorted(all_sellers_offers, key=lambda x:
                            float(x[-1]['total_price']))

    if len(sorted_items) >= 3:
        return sorted_items[0:3]
    else:
        return sorted_items


def get_offer_link(offer_id):
    return f'https://allegro.pl/oferta/{offer_id}'
