import requests
from requests.exceptions import HTTPError
import json

# {"X-auth-key": "Basic qwertyui12345fdghjkl;", "format": "Application/Python"}

# GET / POST / PUT / DELETE
class BaseAPI:
    def __init__(self, base_url:str, headers:dict=None) -> None:
        self.base_url = base_url
        self.headers = headers or {}

    def get(self, endpoint, params=None):
        """Send a GET request."""
        url = f"{self.base_url}{endpoint}"
        print(f"URL: {url}")
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            print(f"{response.status_code}")
            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")
    
    def post(self, endpoint, data=None, json=None):
        """Send a POST request."""
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.post(url, headers=self.headers, data=data, json=json)
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def put(self, endpoint, data=None, json=None):
        """Send a PUT request."""
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.put(url, headers=self.headers, data=data, json=json)
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def delete(self, endpoint):
        """Send a DELETE request."""
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.delete(url, headers=self.headers)
            response.raise_for_status()
            return response.status_code == 204
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

class PlayStationAPI(BaseAPI):
    def __init__(self, base_url, headers=None):
        super().__init__(base_url, headers)
    
    def get_transactions(self):
        endpoint = "/accounts"
        return self.get(endpoint)
    
    @staticmethod
    def _to_jsonl_buffer(json_data):
        return '\n'.join([json.dumps(record) for record in json_data])