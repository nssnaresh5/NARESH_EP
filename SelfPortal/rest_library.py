import requests
import logging
from logging.handlers import RotatingFileHandler
import json
from datetime import datetime


class RestClient:
    def __init__(self):
        self.logger = logging.getLogger('RestClient')
        filename = f"rest_client-{datetime.now().strftime('%Y%m%d')}.log"
        handler = RotatingFileHandler(filename, maxBytes=10 * 1024 * 1024, backupCount=10)
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def log_request_response(self, method, url, request_body, response):
        request_body = json.dumps(request_body, indent=2) if request_body else None
        response_body = json.dumps(response.json(), indent=2)
        log_message = f"{method} - {url}\nRequest Body:\n{request_body}\nResponse Body:\n{response_body}\nResponse Code: {response.status_code}"
        self.logger.info(log_message)

    def get(self, url, headers=None, params=None):
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            self.log_request_response("GET", url, params, response)
        except requests.exceptions.RequestException as err:
            self.logger.error(f"Error: {err}")
            raise
        else:
            return response.json()

    def post(self, url, headers=None, json=None):
        try:
            response = requests.post(url, headers=headers, json=json)
            response.raise_for_status()
            self.log_request_response("POST", url, json, response)
        except requests.exceptions.RequestException as err:
            self.logger.error(f"Error: {err}")
            raise
        else:
            return response.json()

    def put(self, url, headers=None, json=None):
        try:
            response = requests.put(url, headers=headers, json=json)
            response.raise_for_status()
            self.log_request_response("PUT", url, json, response)
        except requests.exceptions.RequestException as err:
            self.logger.error(f"Error: {err}")
            raise
        else:
            return response.json()

    def delete(self, url, headers=None):
        try:
            response = requests.delete(url, headers=headers)
            response.raise_for_status()
            self.log_request_response("DELETE", url, None, response)
        except requests.exceptions.RequestException as err:
            self.logger.error(f"Error: {err}")
            raise
        else:
            return response.json()

    @staticmethod
    def findKeyvalue(obj, path):
        def extract_element_from_json(obj, path):
            def extract(obj, path, ind, arr):
                key = path[ind]
                if ind + 1 < len(path):
                    if isinstance(obj, dict):
                        if key in obj.keys():
                            extract(obj.get(key), path, ind + 1, arr)
                        else:
                            arr.append(None)
                    elif isinstance(obj, list):
                        if not obj:
                            arr.append(None)
                        else:
                            for item in obj:
                                extract(item, path, ind, arr)
                    else:
                        arr.append(None)
                if ind + 1 == len(path):
                    if isinstance(obj, list):
                        if not obj:
                            arr.append(None)
                        else:
                            for item in obj:
                                arr.append(item.get(key, None))
                    elif isinstance(obj, dict):
                        arr.append(obj.get(key, None))
                    else:
                        arr.append(None)
                return arr

            if isinstance(obj, dict):
                return extract(obj, path, 0, [])
            elif isinstance(obj, list):
                outer_arr = []
                for item in obj:
                    outer_arr.append(extract(item, path, 0, []))
                return outer_arr

        path = path.split(".")
        txt = extract_element_from_json(obj, path)
        if txt is not None:
            return txt
        else:
            return ""

# # Create an instance of the RestClient class
# client = RestClient()
#
# # Define the URL, headers, and data for the requests
# url = 'https://jsonplaceholder.typicode.com/posts'
# headers = {'Content-Type': 'application/json'}
# data = {'title': 'foo', 'body': 'bar', 'userId': 1}
#
# # Make a GET request
# get_response = client.get(url, headers)
#
# # Make a POST request
# post_response = client.post(url, headers, data)
#
# # Define a new URL for the PUT and DELETE requests
# url = 'https://jsonplaceholder.typicode.com/posts/1'
#
# # Make a PUT request
# put_response = client.put(url, headers, data)
#
# # Make a DELETE request
# delete_response = client.delete(url, headers)
#
# # Print the responses
# print(f"GET response: {get_response}")
# print(f"POST response: {post_response}")
# print(f"PUT response: {put_response}")
# print(f"DELETE response: {delete_response}")
