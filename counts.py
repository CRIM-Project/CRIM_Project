
from JSON_API import data_set_importer
import json
import pprint

# Modify this to inlcude desired counts
counts_wanted = ['user', 'title', 'relationship_type', 'assertion_type']

# Rerturn counts for desired count types
def get_counts(counts_wanted, data):
	user_counts = {}
	title_counts = {}
	relationship_counts = {}


	r_keys = [u'scoreA_meiids', u'titleA', u'titleB', u'scoreA_ema', u'scoreB_ema', u'scoreA', u'scoreB', u'cid', u'boolDir', u'direction', u'comment', u'scoreB_meiids', u'scoreAassert', u'scoreBassert', u'id', u'types']  # ideally not use all of these?
	tempdict = dict(zip(r_keys,[None]*len(r_keys)))

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

		versions = info2['scores']
#		print(versions)
		for x in versions:
			title = x['title']
			if title[:2] == ': ': title = title[2:] #cleaning some text
			if title in title_counts.keys():
				temp = title_counts[title]
				title_counts[title] = temp+1
			else: #doesnt exist yet
				title_counts[title]= 1
			
		relation = info2['relationships'][0]
		
		try:
			direction = relation['direction']
		except KeyError:
			direction = "None"
		if direction in relationship_counts.keys():
			temp = relationship_counts[direction]
			relationship_counts[direction] = temp+1
		else: #doesnt exist yet
			relationship_counts[direction] = 1


	#	tempdict = dict(zip(r_keys,[None]*len(r_keys)))
		#makes data structure like {u'scoreA_meiids': None, u'titleA': None,...}
		for key in r_keys:
			try:
				relat = str(relation[key]) 
			except KeyError:
                        	relat = "None"
			if tempdict[key] == None:
				tempdict[key] = {}	
			if relat in tempdict[key].keys(): # hash issue with lists
				temp1 = tempdict[key][relat]
				tempdict[key][relat] = temp1+1
			else: #doesnt exist yet
				tempdict[key][relat] = 1

#	pprint.pprint(tempdict)

	return user_counts,title_counts,relationship_counts


def write_to_csv(count_vals):
	pass

def main():
	crim = data_set_importer.get_json()
	crim.set_url(crim.CRIM_url)
	data = crim.get_data()

	count_list,title_counts,relationship_counts = get_counts(counts_wanted, data)
	print (count_list)
	print("\n")
	pprint.pprint(title_counts)
	print("\n")
	pprint.pprint(relationship_counts)

if __name__ == "__main__":
	main()
