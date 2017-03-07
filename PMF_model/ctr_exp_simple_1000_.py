import ctr_simple
import numpy
import common_function

if __name__ == "__main__":
	user_item_dict, user_num, item_num = common_function.read_user_item_dict("../data/repo_package_train.txt")
	doc_ids, doc_cnt, voc_num =  common_function.repo_description(common_function.read_dict_("../data/repo_dict.txt"))
	repo_id_name_dict = common_function.read_dict("../data/repo_dict.txt")
        package_id_name_dict = common_function.read_dict("../data/package_dict.txt")
	model = ctr_simple.CTR(user_num, item_num, user_item_dict, repo_id_name_dict, package_id_name_dict, "recommendation_result_ctrsimple_1000.txt")
	model.fit()