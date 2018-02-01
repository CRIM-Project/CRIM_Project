
from JSON_API import data_set_importer
import json
import pprint
import csv

# Modify this to inlcude desired counts
counts_wanted = ['user', 'title', 'relationship_type', 'assertion_type']

# Rerturn counts for desired count types
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

def get_counts(counts_wanted, data):
	user_counts = {}
	title_counts = {}
	relationship_counts = {}
	ema_dictionary = {}


	r_keys = [ u'titleA', u'titleB', u'scoreA_ema', u'scoreB_ema', u'direction', u'types']  # ideally not use all of these?
	#r_keys = [u'scoreA_meiids', u'titleA', u'titleB', u'scoreA_ema', u'scoreB_ema', u'scoreA', u'scoreB', u'cid', u'boolDir', u'direction', u'comment', u'scoreB_meiids', u'scoreAassert', u'scoreBassert', u'id', u'types']  # ideally not use all of these?

	a_keys = [u'ema', u'score', u'title', u'types']

	tempdict = dict(zip(r_keys,[None]*len(r_keys)))

	a_tempdict = dict(zip(a_keys,[None]*len(a_keys)))


	for rel in data:

		info = rel["text"]
		info2 = json.loads(info) # turns 'text' into usable dict

		for i, char in enumerate(info):
			if char == "r" and info[i-1] == "e" and info[i-2] == "s" and info[i-3] == "u" and info[i+1] == '"':
				usr = info[i+4]
				if info[i+5] != '"':
					usr = usr + info[i+5]
				if usr not in user_counts:
					user_counts[usr] = 1
				else:
					user_counts[usr] += 1

		relation = info2['relationships'][0]
		#print (info2['assertions'])
		if info2['assertions'] != []:
			assertion = info2['assertions'][0]
		versions = info2['scores']
		#print(versions)


		for x in versions:
			title = x['title']
			#print(x)

			if title[:2] == ': ':
				title = title[2:] #cleaning some text

			if title in title_counts.keys():
				temp = title_counts[title]
				title_counts[title] = temp+1
				ema_sub_dict = {'measures': relation['scoreA_ema'].split('/')[0] , 'Song_From': relation['titleB'] }#, 'Direction': relation['direction'] }
				ema_sub_dict['type'] = get_key(relation, 'types')
				pprint.pprint(ema_sub_dict)
				ema_dictionary[title] = ema_dictionary[title]+ [ema_sub_dict]
			else: #doesnt exist yet
				title_counts[title]= 1
				ema_sub_dict = {'measures': relation['scoreA_ema'].split('/')[0] , 'Song_From': relation['titleA'], }#'Direction': relation['direction'] }
				ema_sub_dict['type'] = get_key(relation, 'types')
				ema_dictionary[title] = [ema_sub_dict]
				#print ("ema_1", relation['scoreA_ema'])
				#print ("ema_2", relation['scoreA_ema'].split('/')[0])
				#print ("ema_3", relation['scoreA_ema'].split('/'), "\n")







	#pprint.pprint(tempdict)
	#pprint.pprint(a_tempdict)
	#pprint.pprint(ema_dictionary)

	return ema_dictionary

def basic_dict_csv(d,header,filename):
	with open(filename, 'w') as f:
		f.write(header+ ',counts\n')
		[f.write('{0},{1}\n'.format(key.replace(',', ''), value)) for key, value in d.items()]

def to_json(d, filename):
	with open(filename, 'w') as f:
		json_str = json.dump(d, f, indent=4)


def write_to_csv(count_vals):
	pass

def main():
	crim = data_set_importer.get_json()
	crim.set_url(crim.CRIM_url)
	data = crim.get_data()
	ema_dictionary = get_counts(counts_wanted, data)
	#print ('User: Count')
	#pprint.pprint(count_list)
	#print ("\n")
	#print ('Song: Count')
	#pprint.pprint(title_counts)
	#print ("\n")
	#print ('Relationship(direction): Count')
	#pprint.pprint(relationship_counts,indent=2)

	to_json(ema_dictionary, 'ema_test.json')
	#basic_dict_csv(ema_dictionary, 'ema', 'ema.csv')
	#basic_dict_csv(tempdict['types'],'realationship_types', 'relationship_types.csv')
	#basic_dict_csv(count_list,'users','user_counts.csv')
	#basic_dict_csv(title_counts,'titles','title_counts.csv')
	#basic_dict_csv(a_tempdict['types'], 'assertion_types', 'assertion_types.csv')
	#basic_dict_csv(a_tempdict['title'], 'assertion_titles', 'assertion_titles.csv')
	#basic_dict_csv(a_tempdict['score'], 'assertion_scores', 'assertion_scores.csv')



if __name__ == "__main__":
	main()
