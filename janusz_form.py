import os, os.path
import json
from pprint import pprint

import query
import pyllegro
import cherrypy

result_row = """
<tr>
    <td>{NAME}</td>
    <td><a href="{LINK}">LINK DO OFERTY</a></td>
    <td>{PRICE}</td>
    
</tr>
"""


class JanuszGenerator:
    def __init__(self):
        #self.access_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NzU4NDAwOTcsInVzZXJfbmFtZSI6IjM4ODkwMTM0IiwianRpIjoiNzU1NGUzYWItZmVhZi00MWRiLTljYzYtZTFkNDAwZTBkM2YwIiwiY2xpZW50X2lkIjoiNTA5YWJjMTVjYzViNGU5ZmJmYmM1Y2NkZDdkM2Q0ZGYiLCJzY29wZSI6WyJhbGxlZ3JvX2FwaSJdfQ.I_xYB6kk06vYtOy5ht-HEtS7WcHh2c8-YFzZRbeZRmTVNtmrQbVruqY02ii3PHBc2mD8ON8BXqJczPZJLLSp5bwyG0RLTMeoCA80jy4fptnkiBixU1lJqD9Gz02VF4_7w70ig2S1RDuHPyfFzIP0uyHsTGGYqrM4sjyRQ7uIibl1RDjiA1lMcZj8L788NRzph21zfVtJdKRAja7cNIw5jQ5koDBWoTrQQoh0HvGc4y8YTbnxEIyDHxodBwmImVkWx4ayNLGJymNGZQg-jlB53OlI-vv1JQmRiLti_2l65Tl4vb5wJdhxSuSTe6atnVa_XXgm83cMgCarmy25vx96Gw"
        #here inster access_token, wich you can access via
        # allegro_login.py script, this makes debbuging easier. Access token is
        # changed everyday
        self.access_token = None

    def create_list(self,
                    product1, min_price1, max_price1, reputation1,
                    product2, min_price2, max_price2, reputation2,
                    product3, min_price3, max_price3, reputation3,
                    product4, min_price4, max_price4, reputation4,
                    product5, min_price5, max_price5, reputation5):
        """Creating list of parameters given by the user"""

        param_list = []
        if product1 != "" and min_price1 != "" and max_price1 != "" and reputation1 != "":
            param_list.append([product1, min_price1, max_price1, reputation1])

        if product2 != "" and min_price2 != "" and max_price2 != "" and reputation2 != "":
            param_list.append([product2, min_price2, max_price2, reputation2])

        if product3 != "" and min_price3 != "" and max_price3 != "" and reputation3 != "":
            param_list.append([product3, min_price3, max_price3, reputation3])

        if product4 != "" and min_price4 != "" and max_price4 != "" and reputation4 != "":
            param_list.append([product4, min_price4, max_price4, reputation4])

        if product5 != "" and min_price5 != "" and max_price5 != "" and reputation5 != "":
            param_list.append([product5, min_price5, max_price5, reputation5])

        if len(param_list) > 0:
            return param_list
        else:
            return 0

    @cherrypy.expose
    def index(self):
        if self.access_token is None:
            token = pyllegro.get_token()
            self.access_token = token[0]
        return open('form3.html', 'r')

    @cherrypy.expose
    def search(self, product1=None, min_price1=None, max_price1=None,
               reputation1=None,  product2=None, min_price2=None, max_price2=None,
               reputation2=None, product3=None, min_price3=None, max_price3=None,
               reputation3=None, product4=None, min_price4=None, max_price4=None,
               reputation4=None, product5=None, min_price5=None, max_price5=None,
               reputation5=None, search_btn=None):

        # create list of parameters chosen by user
        param_list = self.create_list(product1, min_price1, max_price1, reputation1,
                                      product2, min_price2, max_price2, reputation2,
                                      product3, min_price3, max_price3, reputation3,
                                      product4, min_price4, max_price4, reputation4,
                                      product5, min_price5, max_price5, reputation5)

        print(param_list)
        if param_list == 0:
            return "No product was chosen"
        else:
            results_offers_list = query.algorithm(self.access_token, param_list)
            # print("item_list: \n")
            # pprint(results_offers_list)

            results = []
            for item_list in results_offers_list:
                result = ""
                for item in item_list:
                    if not 'total_price' in item:
                        # print("name: {}, price: {}".format(item['name'],
                        #                                    str(item['id'])))
                        # add item features to results
                        result += result_row.format(NAME=item['name'],
                                                     LINK=query.get_offer_link(item['id']),
                                                     PRICE=str(item['price']))
                    else:
                        # print(item_list[-1])
                        # add price of all items summed up to results
                        result += "<tr><td colspan='2'>Suma</td><td>{SUM}</td></tr>".format(SUM=item_list[-1]['total_price'])
                results.append(result)

            if len(results) < 3:
                while len(results) < 3:
                    results.append("No results. Try changing price limits or lower minimal reputation")

            print(results)

        return open('wynik.html', 'r').read().format(RESULT1=results[0],
                                                     RESULT2=results[1],
                                                     RESULT3=results[2])


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': '.'
        }
    }
    cherrypy.quickstart(JanuszGenerator(), '/', conf)
