import requests
import json
import urlparse


def get_json(url):
	try:
		response = requests.get(url)
		result = json.loads(response.text)
	except BaseException as e:
		result = {}
		print e
	return result


def get_json_local(fpath):
	try:
		with open(fpath) as fp:
			result = json.loads(fp.read())
	except BaseException as e:
		result = {}
		print e
	return result


def is_valid_url(url):
	parsed_result = urlparse.urlparse(url)
	return len(parsed_result.scheme) != 0 and len(parsed_result.netloc) != 0