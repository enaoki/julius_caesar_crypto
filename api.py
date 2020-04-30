from util import Util as Util
from config import Config as Config
import json
import io

# An example API class


class API:

    # Static initialization
    @staticmethod
    def static_init() -> None:

        return Config.static_init()

    @staticmethod
    def get_data() -> None:

        # Build URL
        url: str = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data'
        url += '?token=' + Config.get_key()

        # Get and process data
        data = Util.get_json(url)

        return data

    @staticmethod
    def send_file(name, file_name, file_full_path) -> None:

        url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution'
        url += '?token=' + Config.get_key()

        return Util.send_file(url, name, file_name, file_full_path)

    # numero_casas: str = data['numero_casas']

    # print(numero_casas)
    # image_filename: str = image_url.split('/')[-1]
    # json_filename: str = image_filename + '.json'
    # json_data: str = json.JSONEncoder().encode(data)

    # Download the image and write info to disk
    # Util.download_file(image_url, 'data/' + image_filename)
    # Util.write_json(json_data, 'data/' + json_filename)
