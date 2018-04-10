
import sys
from JSON_API import data_set_importer
import json
import pprint
import csv


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

def clean_title(title_name):
	#print(title_name[0])
	if title_name[0] == ":":
		#print("before: ", title_name)
		title_name = title_name[2:]
	#print("now: ", title_name)
	return title_name

def get_catLabel(mea_num):

	categoryLabels = ["part_1", "part_2", "part_3", "part_4", "part_5", "part_6", "part_7"]
	catLabels = {"part_1":range(0, 40), "part_2":range(40, 80), "part_3":range(80, 120),
				"part_4":range(120, 160), "part_5":range(160, 200), "part_6":range(200, 240), "part_7":range(240, 10000)}
	#categoryLabels = [0-40, 40-80, 80-120, 120-160, 160-200, 200-240, 240-above]
	num = mea_num.split("-")
	if len(num) == 1:
		num = int(num[0])
	else:
		num = int((int(num[0])+ int(num[1]))/2)

	for key, value in catLabels.items():
		if num in value:
			return key
	return "Error"







def get_user_dict(data):
	user_title_viz = {}
	user_lst = []


	for rel in data:

		info = rel["text"]
		info2 = json.loads(info) # turns 'text' into usable dict

		relation = info2['relationships'][0]
		u_id = info2['user']
		if info2['assertions'] != []:
			assertion = info2['assertions'][0]
		versions = info2['scores']

		mea = (relation['scoreA_ema'].split('/')[0]).split(",")
		# for x in versions:
		# 	pprint.pprint(x)
		# 	#title = x['title']

		if u_id not in user_lst:
			user_lst.append(u_id)
			user_title_viz[u_id] = []
			#print(mea)

			if len(mea) == 1:
				user_sub_dict = {'measures': mea[0] , 'Song_A': clean_title(relation['titleA']), 'Song_B': clean_title(relation['titleB']) }#, 'Direction': relation['direction'] }
				#user_sub_dict['typee'] = get_key(relation, 'types')
				user_sub_dict['typee'] = get_catLabel(mea[0])
				user_title_viz[u_id] = [user_sub_dict]
			else:
				for m_num in mea:
					user_sub_dict = {'measures': m_num , 'Song_A': clean_title(relation['titleA']), 'Song_B': clean_title(relation['titleB']) }#, 'Direction': relation['direction'] }
					#user_sub_dict['typee'] = get_key(relation, 'types')
					user_sub_dict['typee'] = get_catLabel(m_num)
					user_title_viz[u_id] = [user_sub_dict]


		else:
			if len(mea) == 1:
				user_sub_dict = {'measures': mea[0] , 'Song_A': clean_title(relation['titleA']), 'Song_B': clean_title(relation['titleB']) }#, 'Direction': relation['direction'] }
				#user_sub_dict['typee'] = get_key(relation, 'types')
				user_sub_dict['typee'] = get_catLabel(mea[0])
				user_title_viz[u_id] = user_title_viz[u_id] + [user_sub_dict]
			else:
				for m_num in mea:
					user_sub_dict = {'measures': m_num, 'Song_A': clean_title(relation['titleA']), 'Song_B': clean_title(relation['titleB']) }#, 'Direction': relation['direction'] }
					#user_sub_dict['typee'] = get_key(relation, 'types')
					user_sub_dict['typee'] = get_catLabel(m_num)
					user_title_viz[u_id] = user_title_viz[u_id] + [user_sub_dict]



	#pprint.pprint(user_title_viz)
	return user_title_viz


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
	ema_dictionary = get_user_dict(data)


	to_json(ema_dictionary, 'user_timeline.json')




if __name__ == "__main__":
	main()
