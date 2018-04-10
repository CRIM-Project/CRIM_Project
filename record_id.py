
import sys
from JSON_API import data_set_importer
import json
import pprint
import csv
import pprint


def get_key(dictt, keyy):
	try:
		answer = str(dictt[keyy])

		if list(dictt[keyy]) == []:
			answer = "None"
		else:
			answer = list(dictt[keyy])[0]
	except KeyError:
		answer = "None"
	return answer




def get_record_id(id, data):

	for rel in data:
		#print(rel["record_id"],id ,type(rel["record_id"]),type(id),rel["record_id"]==id )
		if rel["record_id"] == id:
			info = rel['text']
			info2 = json.loads(info)
			return info2
			
	return "record_id not found"

	#pprint.pprint(user_title_viz)


def main(id):
	crim = data_set_importer.get_json()
	crim.set_url(crim.CRIM_url)
	data = crim.get_data()
	result_id = get_record_id(id,data)



	pprint.pprint(result_id)




if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("\nUsage: python record_id.py <id number> \n")
	else:
		#Reading arguments
		record_id = int(sys.argv[1])
	print("Searching for json with ", record_id, " id number")
	#print(sys.argv) = ['record_id.py', '81']
	main(record_id)
