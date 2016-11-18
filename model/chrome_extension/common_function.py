from sets import Set

def JaccardSimilarity(preference1, preference2): 
	s = Set(preference1)
	t = Set(preference2)
	unionSet = s.union(t)
	intersectionSet = s.intersection(t)
	return float(len(intersectionSet))/float(len(unionSet))

def write_recommendation_result(filename, top_20_items, repo_id_name_dict, package_id_name_dict):
	writer = open(filename, "wb")
	for user in top_20_items:
		writer.write(repo_id_name_dict[user])
		for item in top_20_items[user]:
			writer.write('\t')
			writer.write(package_id_name_dict[item[0]])
		writer.write('\n')
	writer.close()

def read_dict(filename):
	reader = open(filename, "rb")
        dict_ = dict()
	for line in reader:
		line = line.strip('\n').split('\t')
		if line[0] == "repo_num" or line[0] == "package_num":
			continue
		dict_[line[0]] = line[1]
	return dict_

def read_user_item_dict(filename):
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

def read_item_user_dict(filename):
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

def compute_jaccard_similarity(dict_, top = -1):
	similarity = dict()
	count = 0
	for u in dict_:
		similarity[u] = dict()
		for v in dict_:
			if int(u) != int(v):
				JSimilarity = JaccardSimilarity(dict_[u], dict_[v])
				if JSimilarity > 0:
					similarity[u][v] = JSimilarity
		print count
		count += 1
		similarity[u] = sorted(similarity[u].iteritems(), key=lambda d:d[1], reverse = True)
		if top != -1:
			similarity[u] = similarity[u][:top]
	return similarity

if __name__ == "__main__":
	print JaccardSimilarity([1,2,3], [2,3,4])
		
