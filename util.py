import requests
import datetime
import json

class Util:

    # The current
    @staticmethod
    def today_str() -> str:

        return str(datetime.date.today())

    # Call a GET request on the URL and return a string
    @staticmethod
    def get(url: str) -> bytes:

        with requests.get(url) as response:
            return response.content

    # Call a GET request on the URL and return JSON data
    @staticmethod
    def get_json(url: str) -> dict:

        with requests.get(url) as response:
            return response.json()

    @staticmethod
    def send_file(url: str, name: str, file_name: str, file_full_path: str) -> str:
        multipart_form_data = {
            name: (file_name, open(file_full_path, 'rb'))
        }
        with requests.post(url, files=multipart_form_data) as r:
            return r.text

    # Write data to a file on disk
    @staticmethod
    def write_json(data: str, path: str) -> None:

        out_file = open(path, 'w')
        out_file.write(data)
        out_file.close()
