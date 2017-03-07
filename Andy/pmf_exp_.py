import pmf_
import numpy
import common_function
import sys

if __name__ == "__main__":
	user_item_dict, user_num, item_num = common_function.read_user_item_dict("../data/repo_package_train.txt")
	repo_id_name_dict = common_function.read_dict("../data/repo_dict.txt")
        package_id_name_dict = common_function.read_dict("../data/package_dict.txt")
	model = pmf_.PMF(user_num, item_num, user_item_dict, repo_id_name_dict, package_id_name_dict, "recommendation_result_pmf_" + sys.argv[1] + ".txt", lambda_u = float(sys.argv[1]), lambda_v = float(sys.argv[1]))
    	model.fit()
