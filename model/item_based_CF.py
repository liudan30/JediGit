import JaccardSimilarity
from sets import Set
import user_based_CF

def read_data(filename):
	reader = open(filename, "rb")
	item_user_dict = dict()
	for line in reader:
		line = line.strip('\n').split('\t')
		if line[0] == "repo_num":
			continue
		if not item_user_dict.has_key(line[2]):
			item_user_dict[line[2]] = Set()
		item_user_dict[line[2]].add(line[0])	
	return item_user_dict

def recommendation(user_item_dict, item_similarity, item_user_dict):
	user_item_recommendation = dict()
	for user in user_item_dict:
		user_item_recommendation[user] = dict()
		for item in user_item_dict[user]:
			if not item_similarity.has_key(item):
				continue
			for similar_item in item_similarity[item]:
				if similar_item[0] not in user_item_dict[user]:
					if not user_item_recommendation[user].has_key(similar_item[0]):
						user_item_recommendation[user][similar_item[0]] = 0.0
					user_item_recommendation[user][similar_item[0]] += similar_item[1]
	for user in user_item_recommendation:
		user_item_recommendation[user] = sorted(user_item_recommendation[user].iteritems(), key=lambda d:d[1], reverse = True)[:20]
	return user_item_recommendation

if __name__ == "__main__":
	user_item_dict = user_based_CF.read_data("../data/repo_package_train.txt")
	item_user_dict = read_data("../data/repo_package_train.txt")
	item_similarity = user_based_CF.compute_jaccard_similarity(item_user_dict)
	top_20_items = recommendation(user_item_dict, item_similarity, item_user_dict)
	repo_id_name_dict = user_based_CF.read_dict("../data/repo_dict.txt")
	package_id_name_dict = user_based_CF.read_dict("../data/package_dict.txt")
	user_based_CF.write_recommendation_result("recommendation_result_item_based_CF.txt", top_20_items, repo_id_name_dict, package_id_name_dict)
