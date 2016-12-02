import ctr
import numpy
import common_function

if __name__ == "__main__":
	user_item_dict, user_num, item_num = common_function.read_user_item_dict("../data/repo_package_train.txt")
	doc_ids, doc_cnt, voc_num =  common_function.repo_description(common_function.read_dict_("../data/repo_dict.txt"))
	model = ctr.CTR(user_num, item_num, user_item_dict, voc_num, doc_ids, doc_cnt, lambda_u = 100)
	model.fit()
	rating = model.predict_item()
	top_20_item = numpy.argsort(rating, axis = 1)[:,:20]
	repo_id_name_dict = common_function.read_dict("../data/repo_dict.txt")
	package_id_name_dict = common_function.read_dict("../data/package_dict.txt")
	common_function.write_recommendation_result("recommendation_result_ctr_100.txt", top_20_item, repo_id_name_dict, package_id_name_dict)
