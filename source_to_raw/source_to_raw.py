from pprint import pprint
import requests

url     = 'https://opendata-download-metobs.smhi.se'
url_get = '/api/version/1.0/parameter/1/station-set/all/period/latest-hour/data.json'

r = requests.get(url+url_get)

with open('data/testing/raw/source_to_raw.json', 'w') as outfile:
	pprint(r.json())
	outfile.writelines(r.text)


