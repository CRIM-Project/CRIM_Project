
from JSON_API import data_set_importer
import json
import pprint
import csv

# Modify this to inlcude desired counts
counts_wanted = ['user', 'title', 'relationship_type', 'assertion_type']

# Rerturn counts for desired count types
def get_counts(counts_wanted, data):
	user_counts = {}
	title_counts = {}
	relationship_counts = {}


	r_keys = [ u'titleA', u'titleB', u'scoreA_ema', u'scoreB_ema', u'direction', u'types']  # ideally not use all of these?
	#r_keys = [u'scoreA_meiids', u'titleA', u'titleB', u'scoreA_ema', u'scoreB_ema', u'scoreA', u'scoreB', u'cid', u'boolDir', u'direction', u'comment', u'scoreB_meiids', u'scoreAassert', u'scoreBassert', u'id', u'types']  # ideally not use all of these?
	
	
	#r_keys = [u'scoreA_meiids', u'titleA', u'titleB', u'scoreA_ema', u'scoreB_ema', u'scoreA', u'scoreB', u'cid', u'boolDir', u'direction', u'comment', u'scoreB_meiids', u'scoreAassert', u'scoreBassert', u'id', u'types']  # ideally not use all of these?
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

		relation = info2['relationships'][0]
		versions = info2['scores']
#		print(versions)
		#assertion = info2['assertions'][0] #mimic this after relations
		
		for x in versions:
			title = x['title']
			if title[:2] == ': ': title = title[2:] #cleaning some text
			if title in title_counts.keys():
				temp = title_counts[title]
				title_counts[title] = temp+1
			else: #doesnt exist yet
				title_counts[title]= 1
		try:
			direction = relation['direction']
		except KeyError:
			direction = "None"
		if direction in relationship_counts.keys():
			temp = relationship_counts[direction]
			relationship_counts[direction] = temp+1
		else: #doesnt exist yet
			relationship_counts[direction] = 1
		
		#print( 'here',info2['assertions'])
		#tempdict = dict(zip(r_keys,[None]*len(r_keys)))
		#makes data structure like {u'scoreA_meiids': None, u'titleA': None,...}
		for key in r_keys:
			try:
				relat = str(relation[key]) 
				if key == "types":
					#print (relation[key])
					if list(relation[key]) == []:
						relat = "None"
					else:
						relat = list(relation[key])
								
					#print ("lis")
					#print (list(relation[key]))
			except KeyError:
                        	relat = "None"
			if type(relat) == type([]):
			#	print ("relat list", relat)
				for elem in relat:
			#		print ("elem", elem)
					if tempdict[key] == None:
						tempdict[key] = {}
					if elem in list(tempdict[key]): # hash issue with lists
						temp1 = tempdict[key][elem]
						tempdict[key][elem] = temp1+1
					else: #doesnt exist yet
						tempdict[key][elem] = 1
			
			elif tempdict[key] == None:
				tempdict[key] = {}	
			elif relat in list(tempdict[key]): # hash issue with lists
				temp1 = tempdict[key][relat]
				tempdict[key][relat] = temp1+1					
			else: #doesnt exist yet
				tempdict[key][relat] = 1

		#NOTE: CAN THERE BE ZERO ASSERTIONS FOR ONE ITEM? 
		# Also we still need to make a_keys - similar to r_keys
		"""
		for key in a_keys: #asser is like relat 
                        try:
                                asser = str(assertions[key])
                                if key == "types":
                                        #print (relation[key])
                                        if list(assertions[key]) == []:
                                                asser = "None"
                                        else:
                                                asser = list(assertions[key])[0]
						#currently just takes the first one which is wrong!
                                        #print ("lis")
                                        #print (list(relation[key]))
                        except KeyError:
                                asser = "None"
                #       if type(relat) == type([]):
                #               for elem in relat:
                        if assert_dict[key] == None:
                                assert_dict[key] = {}
                        if relat in assert_dict[key].keys(): # hash issue with lists
                                temp1 = assert_dict[key][asser]
                                assert_dict[key][asser] = temp1+1                              
                        else: #doesnt exist yet
                                assert_dict[key][asser] = 1



 		"""
	pprint.pprint(tempdict)

	return user_counts,title_counts,relationship_counts,tempdict

def basic_dict_csv(d,header,filename):
	with open(filename, 'w') as f:
		f.write(header+ ',counts\n')
		[f.write('{0},{1}\n'.format(key, value)) for key, value in d.items()]

def write_to_csv(count_vals):
	pass

def main():
	crim = data_set_importer.get_json()
	crim.set_url(crim.CRIM_url)
	data = crim.get_data()
	count_list,title_counts,relationship_counts,tempdict = get_counts(counts_wanted, data)
	print ('User: Count')	
	pprint.pprint(count_list)
	print ("\n")
	print ('Song: Count')
	pprint.pprint(title_counts)
	print ("\n")
	print ('Relationship(direction): Count')	
	pprint.pprint(relationship_counts,indent=2)
	
	basic_dict_csv(tempdict['types'],'realationship_types', 'relationship_types.csv')
	basic_dict_csv(count_list,'users','user_counts.csv')
	basic_dict_csv(title_counts,'titles','title_counts.csv')
	


if __name__ == "__main__":
	main()
