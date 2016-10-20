import common_function
from sets import Set

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
	user_item_dict = common_function.read_user_item_dict("../data/repo_package_train.txt")
	item_user_dict = common_function.read_item_user_dict("../data/repo_package_train.txt")
	item_similarity = common_function.compute_jaccard_similarity(item_user_dict)
	top_20_items = recommendation(user_item_dict, item_similarity, item_user_dict)
	repo_id_name_dict = common_function.read_dict("../data/repo_dict.txt")
	package_id_name_dict = user_based_CF.read_dict("../data/package_dict.txt")
	common_function.write_recommendation_result("recommendation_result_item_based_CF.txt", top_20_items, repo_id_name_dict, package_id_name_dict)
