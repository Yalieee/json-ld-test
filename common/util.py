import requests
import json
import urlparse


def get_json(url):
	response = requests.get(url)
	try:
		result = json.loads(response.text)
	except BaseException as e:
		result = {}
		print e
	return result


def is_valid_url(url):
	parsed_result = urlparse.urlparse(url)
	return len(parsed_result.scheme) != 0 and len(parsed_result.netloc) != 0