import requests
import base64
import json
import webbrowser


CLIENT_ID = "509abc15cc5b4e9fbfbc5ccdd7d3d4df"
CLIENT_SECRET = "Q7gLj6hIWUlAjvjNGRlTevHzjtehOa9Mpx6WAbhJdKbmc2g48pk5KFJK3waxsbFi"


def get_token():
    device_response = requests.post(
        'https://allegro.pl/auth/oauth/device',
        params={
            'client_id': CLIENT_ID
        },
        headers={
            'Authorization': 'Basic ' + str(base64.b64encode(bytes(CLIENT_ID + ":" + CLIENT_SECRET, 'utf-8')), "utf-8"),
            'Content-Type': 'application/x-www-form-urlencoded'
        },
    )

    if device_response.status_code == 200:
        # time for user to login in to allegro
        timeout = 2*120
        i = 0

        # open new tab in default webbrowser
        webbrowser.open(json.loads(device_response.text)["verification_uri_complete"], new=2)

        while i < timeout:
            token_response = requests.post(
                f'https://allegro.pl/auth/oauth/token?grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Adevice_code&' +
                f'device_code={json.loads(device_response.text)["device_code"]}',
                headers={
                    'Authorization': 'Basic ' + str(base64.b64encode(bytes(CLIENT_ID + ":" + CLIENT_SECRET, 'utf-8')),
                                                    "utf-8"),
                },
            )
            if token_response.status_code == 200:
                # returns token to calling instance
                return [json.loads(token_response.text)["access_token"], json.loads(token_response.text)["refresh_token"]]
                break
            else:
                i += 1
        # in case of timeout request without success
        print(f"Timed out ({timeout} s, no token received.)")
    return 0

