from sets import Set
import common_function
import lda_model

def get_top20(filename):
	reader = open(filename, "rb")
	top_20 = []
	for line in reader:
		line = line.strip('\n').split('\t')
		top_20 += line
	return Set(top_20)

def read_dict(filename):
	reader = open(filename, "rb")
        dict_ = dict()
	for line in reader:
		line = line.strip('\n').split('\t')
		if line[0] == "repo_num" or line[0] == "package_num":
			continue
		dict_[line[1]] = line[0]
	return dict_

def recommendation(filename):
	recommend = dict()
	reader = open(filename, "rb")
	for line in reader:
                line = line.strip('\n').split('\t')
                repo_name = line[0]
                packages = line[1:]
		recommend[repo_name] = packages
	return recommend

def generate_explanation(filename, recommend_package, user_item_dict, item_user_dict, package_name_id_dict, repo_name_id_dict, top_20, description_similarity, package_id_name_dict):
	writer = open(filename, "wb")
	for user in recommend_package:
		writer.write(user)
		for item in recommend_package[user]:
			writer.write('\n')
			writer.write(item)
			writer.write('\t')
			is_top20 = False
			if item in top_20:
				is_top20 = True
			x, item_ = computeX(item, user, user_item_dict, item_user_dict, package_name_id_dict, repo_name_id_dict) 
			y = computeY(item, user, user_item_dict, item_user_dict, package_name_id_dict, repo_name_id_dict, description_similarity)
			writer.write(explanation(x, y, is_top20, item, user, package_id_name_dict[item_]))
		writer.write('\n')
	writer.close()

def computeX(item, user, user_item_dict, item_user_dict, package_name_id_dict, repo_name_id_dict):
	x = 0.0
	res_item = ""
	for item_ in user_item_dict[repo_name_id_dict[user]]:
		currentX = float(len(item_user_dict[package_name_id_dict[item]].intersection(item_user_dict[item_])))/float(len(item_user_dict[item_]))	
		if currentX > x:
			x = currentX
			res_item = item_
	return x, item_

def computeY(item, user, user_item_dict, item_user_dict, package_name_id_dict, repo_name_id_dict, description_similarity):
        y = 0.0
	if not description_similarity.has_key(repo_name_id_dict[user]):
		return y
        for user_ in description_similarity[repo_name_id_dict[user]]:
                if package_name_id_dict[item] in user_item_dict[user_]:
			y += 1.0
        return float(y) / float(len(description_similarity[repo_name_id_dict[user]])) 

def explanation(x, y, is_top20, item, user, item_):
	if is_top20 and x < 0.5 and y < 0.5:
		return item + "is one of the most popular java-packages in Github."
	if x > y:
		return str(int(x * 100)) + "% repositories who use java-package " + item_ + " also use java-package " + item
	else:
		return str(int(y * 100)) + "% repositories who has similar description with repository " + user + " also use java-package " + item

def make_dict(similarity):
	res = dict()
	for i in range(0, len(similarity) - 1):
		for j in range(i + 1, len(similarity)):
			if similarity[i][j] > 0.8:
				if not res.has_key(str(i + 1)):
					res[str(i+1)] = Set()
				if not res.has_key(str(j + 1)):
                                        res[str(j+1)] = Set()
				res[str(i+1)].add(str(j+1))
				res[str(j+1)].add(str(i+1))
	return res

if __name__ == "__main__":
	repo_name_id_dict = read_dict("../data/repo_dict.txt")
	package_name_id_dict = read_dict("../data/package_dict.txt")
	user_item_dict = common_function.read_user_item_dict("../data/repo_package_train.txt")
	item_user_dict = common_function.read_item_user_dict("../data/repo_package_train.txt")
	top_20 = get_top20("top-20.txt")
	package_id_name_dict = common_function.read_dict("../data/package_dict.txt")
	description_similarity = make_dict(lda_model.description_similarity(30))
	recommend_package = recommendation("recommendation_result_user_based_CF_.txt")
	generate_explanation("recommendation_result_user_based_CF_explanation.txt", recommend_package, user_item_dict, item_user_dict, package_name_id_dict, repo_name_id_dict, top_20, description_similarity, package_id_name_dict)
