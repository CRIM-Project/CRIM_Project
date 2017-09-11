#!/usr/bin/python3

"""
Provide routines to import CRIM project data set into list of lists format.
Dylan Slack

"""

import json, csv, urllib.request

class get_json:
	def __init__(self, url = None):
		self.url = url
		self.CRIM_url = 'http://92.154.49.37/CRIM/api/citation'

	# Method for setting url
	def set_url(self, url = None):
		if not url:
			raise NameError('Provide url to json API!')
		else:
			self.url = url

	# Extract data from json api
	def get_data(self, write_to_csv = False):
		with urllib.request.urlopen(self.url) as url:
			data = json.loads(url.read().decode())

			#
			# Add method to write to csv? 
			# May not need this
			#

		return data


if __name__ == "__main__":
	crim = get_json("http://92.154.49.37/CRIM/api/citation")
	data = crim.get_data()
	print (data[0]['text'])
	


