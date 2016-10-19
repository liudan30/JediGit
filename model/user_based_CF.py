import JaccardSimilarity
from sets import Set

def read_data(filename):
	reader = open(filename, "rb")
	user_item_dict = dict()
	for line in reader:
		line = line.strip('\n').split('\t')
		if line[0] == "repo_num":
			continue
		if not user_item_dict.has_key(line[0]):
			user_item_dict[line[0]] = Set()
		user_item_dict[line[0]].add(line[2])	
	return user_item_dict

def compute_jaccard_similarity(user_item_dict):
	user_similarity = dict()
	for user1 in user_item_dict:
		for user2 in user_item_dict:
			if int(user1) < int(user2):
				JSimilarity = JaccardSimilarity.JaccardSimilarity(user_item_dict[user1], user_item_dict[user2])
				if JSimilarity > 0:
					if not user_similarity.has_key(user1):
						user_similarity[user1] = dict()
					user_similarity[user1][user2] = JSimilarity
					if not user_similarity.has_key(user2):
                                	        user_similarity[user2] = dict()
                                	user_similarity[user2][user1] = JSimilarity
					print user1 + ' ' + user2 + ' ' + str(JSimilarity)
	return user_similarity

def recommendation(user_item_dict, user_similarity):
	user_item_recommendation = dict()
	for user in user_item_dict:
		user_item_recommendation[user] = dict()
		for similar_user in user_similarity[user]:
			for item in user_item_dict[similar_user]:
				if item not in user_item_dict[user]:
					if not user_item_recommendation[user].has_key(item):
						user_item_recommendation[user][item] = 0.0
					user_item_recommendation[user][item] += user_similarity[user][similar_user]
	for user in user_item_recommendation:
		user_item_recommendation[user] = sorted(user_item_recommendation[user].iteritems(), key=lambda d:d[1], reverse = True)[:20]
	return user_item_recommendation

def read_dict(filename):
	reader = open(filename, "rb")
        dict_ = dict()
	for line in reader:
		line = line.strip('\n').split('\t')
		if line[0] == "repo_num":
			continue
		dict_[line[0]] = line[1]
	return dict_

def write_recommendation_result(filename, top_20_items, repo_id_name_dict, package_id_name_dict):
	writer = open(filename, "wb")
	for user in top_20_items:
		writer.write(repo_id_name_dict[user])
		for item in top_20_items[item]:
			writer.write('\t')
			writer.write(package_id_name_dict[item[0]])
		writer.write('\n')
	writer.close()
				
if __name__ == "__main__":
	user_item_dict = read_data("../data/repo_package_train.txt")
	user_similarity = compute_jaccard_similarity(user_item_dict)
	top_20_items = recommendation(user_item_dict, user_similarity)
	repo_id_name_dict = read_dict("../data/repo_dict.txt")
	package_id_name_dict = read_dict("../data/package_dict.txt")
	write_recommendation_result("recommendation_result_user_based_CF.txt", top_20_items, repo_id_name_dict, package_id_name_dict)
