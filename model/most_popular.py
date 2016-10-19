from sets import Set
import user_based_CF

def recommendation(user_item_dict):
	item_popular = dict()
	for user in user_item_dict:
		for item in user_item_dict[user]:
			if not item_popular.has_key(item):
				item_popular[item] = 0
			item_popular[item] += 1
	top20 = sorted(item_popular.iteritems(), key=lambda d:d[1], reverse = True)[:20]
	for user in user_item_dict:
		item_popular[user] = top20
	return item_popular
	
if __name__ == "__main__":
	user_item_dict = user_based_CF.read_data("../data/repo_package_train.txt")
	top_20_items = recommendation(user_item_dict)
	repo_id_name_dict = user_based_CF.read_dict("../data/repo_dict.txt")
	package_id_name_dict = user_based_CF.read_dict("../data/package_dict.txt")
	user_based_CF.write_recommendation_result("recommendation_result_most_popular.txt", top_20_items, repo_id_name_dict, package_id_name_dict)
