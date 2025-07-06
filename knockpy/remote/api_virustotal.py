import requests
import json

"""
Let's start with simple function specifications:

1. if apikey is required, use "api_" before the plugin name:

	api_service.py

2. the function name must be "get" and take as parameter "domain":

	def get(domain):
		foo

3. the function must return a possibly unique list of subdomains:

	['sub1.domain.com', 'sub2.domain.com']

4. to parse the results it is recommended to use the standard modules such as:

	requests, json, bs4, re
"""

# author: Gianni Amato
# plugin: api_virustotal
# version: 1.0

def get(domain):
	# virustotal -> JSON: key -> subdomains
	apikey = "" # <- here your API KEY

	url = f"https://www.virustotal.com/api/v3/domains/{domain}"
	headers = {"x-apikey": apikey}
	resp = requests.get(url, headers=headers, timeout=5).text

	resp = json.loads(resp)
	
	result = []
	if "subdomains" in resp.keys():
		for item in resp["subdomains"]:
			subdomain = item.replace("."+domain, "")
			if subdomain not in result:
				result.append(subdomain)
	
	return result
