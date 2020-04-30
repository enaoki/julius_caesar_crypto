import urllib.request, urllib.response
import datetime, json

class Util:

	# The current 
	@staticmethod
	def today_str() -> str:

		return str(datetime.date.today())

	# Call a GET request on the URL and return a string
	@staticmethod
	def get( url: str) -> bytes:

		with urllib.request.urlopen(url) as response:
   			return response.read()

	# Call a GET request on the URL and return JSON data
	@staticmethod
	def get_json(url: str) -> dict:

		with urllib.request.urlopen(url) as response:
   			return json.load(response)

	# Write data to a file on disk
	@staticmethod
	def write_json(data: str, path: str) -> None:

		out_file = open(path, 'w')
		out_file.write(data)
		out_file.close()