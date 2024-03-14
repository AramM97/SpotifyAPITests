import requests
from dotenv import load_dotenv
import os
import base64
import json

class APIWrapper:


    def __init__(self):
        self.response = None
        self.my_request = requests
        load_dotenv()
        self.client_id = os.getenv("CLIENT_ID")
        self.client_secret = os.getenv("CLIENT_SECRET")
        self.user_id = os.getenv("USER_ID")

    def get_token(self):
        auth_string = self.client_id + ":" + self.client_secret
        auth_bytes = auth_string.encode("utf-8")
        auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": "Basic " + auth_base64,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {"grant_type": "client_credentials"}
        result = self.my_request.post(url, headers=headers, data=data)
        json_result = json.loads(result.content)
        token = json_result["access_token"]
        return token

    def get_auth_header(self, token):
        return {"Authorization": "Bearer " + token}

    def api_get_request(self, url, token):
        self.headers = self.get_auth_header(token)
        self.response = self.my_request.get(url, headers= self.headers)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

