import common_function

def recommendation(user_item_dict, user_similarity):
	user_item_recommendation = dict()
	for user in user_item_dict:
		user_item_recommendation[user] = dict()
		for similar_user in user_similarity[user]:
			for item in user_item_dict[similar_user[0]]:
				if item not in user_item_dict[user]:
					if not user_item_recommendation[user].has_key(item):
						user_item_recommendation[user][item] = 0.0
					user_item_recommendation[user][item] += similar_user[1]
	for user in user_item_recommendation:
		user_item_recommendation[user] = sorted(user_item_recommendation[user].iteritems(), key=lambda d:d[1], reverse = True)[:20]
	return user_item_recommendation


				
if __name__ == "__main__":
	user_item_dict = common_function.read_user_item_dict("../data/repo_package_train.txt")
	user_similarity = common_function.compute_jaccard_similarity(user_item_dict, 100)
	top_20_items = recommendation(user_item_dict, user_similarity)
	repo_id_name_dict = common_function.read_dict("../data/repo_dict.txt")
	package_id_name_dict = common_function.read_dict("../data/package_dict.txt")
	common_function.write_recommendation_result("recommendation_result_user_based_CF.txt", top_20_items, repo_id_name_dict, package_id_name_dict)
