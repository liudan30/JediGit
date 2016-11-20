import common_function
import lda_model
import copy

def description_recommendation(user_item_dict, user_similarity):
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
	return user_item_recommendation

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
	return user_item_recommendation

def getTop20(user_item_description, user_item_recommendation, lambda_):
	res = copy.deepcopy(user_item_recommendation)
	for user in user_item_description:
		for item in user_item_description[user]:
			if res.has_key(user):
				if res[user].has_key(item):
					res[user][item] += lambda_ * user_item_description[user][item]
				else:
					res[user][item] = lambda_ * user_item_description[user][item]
			else:
				res[user] = dict()
				res[user][item] = lambda_ * user_item_description[user][item]
	
	for user in res:
                res[user] = sorted(res[user].iteritems(), key=lambda d:d[1], reverse = True)[:20]
        return res

if __name__ == "__main__":
	user_item_dict = common_function.read_user_item_dict("../data/repo_package_train.txt")
	user_similarity = common_function.compute_jaccard_similarity(user_item_dict, 100)
	topic_similarity = lda_model.description_similarity(30)
	repo_id_name_dict = common_function.read_dict("../data/repo_dict.txt")
	package_id_name_dict = common_function.read_dict("../data/package_dict.txt")
	user_item_description = description_recommendation(user_item_dict, topic_similarity)
	user_item_recommendation = recommendation(user_item_dict, user_similarity)

	for lambda_ in range(1, 11):
		print float(lambda_) / 10.0
		top_20_items = getTop20(user_item_description, user_item_recommendation, float(lambda_) / 10.0)
		common_function.write_recommendation_result("recommendation_result_user_based_CF_topic10_" + str(float(lambda_)/10.0) + ".txt", top_20_items, repo_id_name_dict, package_id_name_dict)

	for lambda_ in range(1, 10):
                print float(lambda_) / 100.0
                top_20_items = getTop20(user_item_description, user_item_recommendation, float(lambda_) / 100.0)
                common_function.write_recommendation_result("recommendation_result_user_based_CF_topic10_" + str(float(lambda_)/100.0) + ".txt", top_20_items, repo_id_name_dict, package_id_name_dict)
