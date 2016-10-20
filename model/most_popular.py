import common_function

if __name__ == "__main__":
	item_user_dict = common_function.read_item_user_dict("../data/repo_package_train.txt")
	top_20_items = sorted(item_user_dict.iteritems(), key=lambda d:len(d[1]), reverse = True)[:20]
	package_id_name_dict = common_function.read_dict("../data/package_dict.txt")
	writer = open("recommendation_result_most_popular.txt", "wb")
	for i in range(0, 20):
		writer.write(package_id_name_dict[top_20_items[i][0]])
		if i != 19:
			writer.write('\t')
		else:
			writer.write('\n')
