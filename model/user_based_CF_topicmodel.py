import common_function
import lda_model

def recommendation(user_item_dict, user_similarity):
	user_item_recommendation = dict()
	for user in range(0, len(user_similarity)):
		print user
		user_item_recommendation[str(user + 1)] = dict()
		for similar_user in range(0, len(user_similarity)):
			if user != similar_user:
				for item in user_item_dict[str(similar_user + 1)]:
					if item not in user_item_dict[str(user + 1)]:
						if not user_item_recommendation[str(user + 1)].has_key(item):
							user_item_recommendation[str(user + 1)][item] = 0.0
						user_item_recommendation[str(user + 1)][item] += user_similarity[user][similar_user]
	for user in user_item_recommendation:
		user_item_recommendation[user] = sorted(user_item_recommendation[user].iteritems(), key=lambda d:d[1], reverse = True)[:20]
	return user_item_recommendation



if __name__ == "__main__":
	user_item_dict = common_function.read_user_item_dict("../data/repo_package_train.txt")
	#user_similarity = common_function.compute_jaccard_similarity(user_item_dict, 100)

	repo_id_name_dict = common_function.read_dict("../data/repo_dict.txt")
	package_id_name_dict = common_function.read_dict("../data/package_dict.txt")

	for n in range(30, 35, 10):
		print n
		user_similarity = lda_model.description_similarity(n)
		top_20_items = recommendation(user_item_dict, user_similarity)
		common_function.write_recommendation_result("result/recommendation_result_user_based_CF_topic" + str(n) + ".txt", top_20_items, repo_id_name_dict, package_id_name_dict)
