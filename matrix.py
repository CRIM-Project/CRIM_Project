
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
	ema_dictionary = {}
	matrixviz = {}

	r_keys =  [u'types']  # ideally not use all of these?
	#r_keys = [u'scoreA_meiids', u'titleA', u'titleB', u'scoreA_ema', u'scoreB_ema', u'scoreA', u'scoreB', u'cid', u'boolDir', u'direction', u'comment', u'scoreB_meiids', u'scoreAassert', u'scoreBassert', u'id', u'types']  # ideally not use all of these?
	

	tempdict = dict(zip(r_keys,[None]*len(r_keys)))
	matrixlist = []	


	for session in data:
		
		info = session["text"]
		info2 = json.loads(info) # turns 'text' into usable dict
		relation = info2['relationships'][0]
		#print (info2['assertions'])
		if info2['assertions'] != []:
			assertion = info2['assertions'][0]
		#print(versions)
		

		try:
			relat = str(relation["types"]) 
			#if key == "types":
			#print (relation[key])
			if list(relation["types"]) == []:
				relat = ["None"]
			else:
				relat = list(relation["types"])
								
					#print ("lis")
					#print (list(relation[key]))
		except KeyError:
                        relat = ["None"]


		try:
			assertt = str(assertion["types"])
                                        #print (relation[key])
			if list(assertion["types"]) == []:
				assertt = ["None"]
			else:
				assertt = list(assertion["types"]) # hopefully this works
		except KeyError:
			assertt = ["None"]
	
		newtuple = (assertt,relat) # assertt = music type , relat = relationship type
		matrixlist.append(newtuple)

	for elem in matrixlist:
		mtype = elem[0] #lst
		rtype = elem[1] #lst
		for r in rtype:
			if r in matrixviz.keys():
				for m in mtype:
					if m in matrixviz[r].keys():
						matrixviz[r][m] += 1
					else:
						matrixviz[r][m] = 1 #initialize it
			else: # r doesnt exist -> initialize it
				matrixviz[r] = {}
 
		#rkey = matrixviz[rtype]


	pprint.pprint(matrixviz)
	return matrixviz
 
#	pprint.pprint(tempdict)
	#pprint.pprint(a_tempdict)
	#pprint.pprint(ema_dictionary)
#	return tempdict
	#return user_counts,title_counts,relationship_counts,tempdict,a_tempdict, ema_dictionary

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
	tempdict = get_counts(counts_wanted, data)
	#count_list,title_counts,relationship_counts,tempdict, a_tempdict, ema_dictionary = get_counts(counts_wanted, data)
	#print ('User: Count')	
	#pprint.pprint(count_list)
	#print ("\n")
	#print ('Song: Count')
	#pprint.pprint(title_counts)
	#print ("\n")
	#print ('Relationship(direction): Count')	
	#pprint.pprint(relationship_counts,indent=2)
	
	#to_json(ema_dictionary, 'ema.json')
	#basic_dict_csv(ema_dictionary, 'ema', 'ema.csv')
	#basic_dict_csv(tempdict['types'],'realationship_types', 'relationship_types.csv')
	#basic_dict_csv(count_list,'users','user_counts.csv')
	#basic_dict_csv(title_counts,'titles','title_counts.csv')
	#basic_dict_csv(a_tempdict['types'], 'assertion_types', 'assertion_types.csv')
	#basic_dict_csv(a_tempdict['title'], 'assertion_titles', 'assertion_titles.csv')
	#basic_dict_csv(a_tempdict['score'], 'assertion_scores', 'assertion_scores.csv')

	

if __name__ == "__main__":
	main()
