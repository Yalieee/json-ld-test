import requests
import json
import urlparse
from common import util
from common.person import Person


class JsonLdParser(object):
	@staticmethod
	def get_node_type(json_body):
		if '@type' in json_body:
			node_type = json_body['@type']
			if util.is_valid_url(node_type):
				return node_type
			else:
				return urlparse.urljoin(json_body['@context'], node_type)

	@staticmethod
	def generate_node_object(json_body):
		node_type = JsonLdParser.get_node_type(json_body)
		
		if node_type in ["http://schema.org/Person", "https://schema.org/Person"]:
			# find colleagues
			colleagues = []
			if 'colleague' in json_body and isinstance(json_body['colleague'], list):
				for colleague in json_body['colleague']:
					if '@context' not in colleague:
						colleague['@context'] = json_body['@context']
					node_object = JsonLdParser.generate_node_object(colleague)
					colleagues.append(node_object)

			return Person(json_body['name'], json_body['email'], json_body['jobTitle'], colleagues)
		else:
			return None


json_body = util.get_json("https://raw.githubusercontent.com/Yalieee/json-ld-test/master/json/person.json")

print JsonLdParser.generate_node_object(json_body)


