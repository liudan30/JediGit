from sets import Set
import pylab as pl

def get_test_data(filename):
	reader = open(filename, "rb")
	total_number = 0
	test_data = dict()
	for line in reader:
		line = line.strip('\n').split('\t')
		if line[0] == "repo_num":
			continue
		total_number += 1
		if not test_data.has_key(line[1]):
			test_data[line[1]] = Set()
		test_data[line[1]].add(line[3])
	return total_number, test_data
		

def get_top20(filename):
	reader = open(filename, "rb")
	top_20 = []
	for line in reader:
		line = line.strip('\n').split('\t')
		top_20 += line
	return top_20

def recall_top(top20, test_data):
	recall = []
	for i in range(0, 20):
		hit_num = 0
		for repo in test_data:
			if top20[i] in test_data[repo]:
				hit_num += 1
		recall.append(hit_num)
	for i in range(1, 20):
		recall[i] += recall[i-1]
	return recall

def recall_CF(top20, test_data, filename):
	recall = []
	for i in range(0, 20):
		recall.append(0)
	reader = open(filename, "rb")
	for line in reader:
		line = line.strip('\n').split('\t')
		repo_name = line[0]
		if not test_data.has_key(repo_name):
			continue 
		packages = line[1:] + top20
		packages = packages[:20]
		for i in range(0, 20):
			if packages[i] in test_data[repo_name]:
				recall[i] += 1
	for i in range(1, 20):
		recall[i] += recall[i-1]
	return recall

if __name__ == "__main__":
	top_20 = get_top20("top-20.txt")
	total_number, test_data = get_test_data("../data/repo_package_test.txt")
	recall_top20 = recall_top(top_20, test_data)
	recall_user_based_CF = recall_CF(top_20, test_data, "recommendation_result_user_based_CF.txt")
	recall_item_based_CF = recall_CF(top_20, test_data, "recommendation_result_item_based_CF.txt")
	recall_user_based_CF1 = recall_CF(top_20, test_data, "result/recommendation_result_user_based_CF_topic30.txt")
	#recall_user_based_CF2 = recall_CF(top_20, test_data, "recommendation_result_user_based_CF_topic10_0.01.txt")
	recall_pmf = recall_CF(top_20, test_data, "../PMF_model/recommendation_result_pmf.txt")
	recall_ctr = recall_CF(top_20, test_data, "../PMF_model/recommendation_result_ctrsimple_100.txt")
    	recall_ctr_v1 = recall_CF(top_20, test_data, "../Embedding/recommendation_result_ctrsimple_100_v1.txt")
    	recall_ctr_v2 = recall_CF(top_20, test_data, "../Embedding/recommendation_result_ctrsimple_100_v2.txt")
    	recall_ctr_v12 = recall_CF(top_20, test_data, "../Embedding/recommendation_result_ctrsimple_100_v12.txt")
        recall_ctr_v1_ = recall_CF(top_20, test_data, "../Embedding/recommendation_result_ctrsimple_100_v1_.txt")
        recall_ctr_v2_ = recall_CF(top_20, test_data, "../Embedding/recommendation_result_ctrsimple_100_v2_.txt")
        recall_ctr_v12_ = recall_CF(top_20, test_data, "../Embedding/recommendation_result_ctrsimple_100_v12_.txt")
	recall_ctr_package = recall_CF(top_20, test_data, "../Embedding/recommendation_result_ctrsimple_100_v1package_.txt")

	for i in range(0, 20):
		recall_pmf[i] = float(recall_pmf[i]) / float(total_number)
		recall_ctr[i] = float(recall_ctr[i]) / float(total_number)
		recall_ctr_v1[i] = float(recall_ctr_v1[i]) / float(total_number)
        	recall_ctr_v2[i] = float(recall_ctr_v2[i]) / float(total_number)
        	recall_ctr_v12[i] = float(recall_ctr_v12[i]) / float(total_number)
	        recall_ctr_v1_[i] = float(recall_ctr_v1_[i]) / float(total_number)
                recall_ctr_v2_[i] = float(recall_ctr_v2_[i]) / float(total_number)
                recall_ctr_v12_[i] = float(recall_ctr_v12_[i]) / float(total_number)
		recall_user_based_CF[i] = float(recall_user_based_CF[i]) /float(total_number)
		recall_user_based_CF1[i] = float(recall_user_based_CF1[i]) / float(total_number)
		#recall_user_based_CF2[i] = float(recall_user_based_CF2[i]) / float(total_number)
		recall_item_based_CF[i] = float(recall_item_based_CF[i]) / float(total_number)
		recall_top20[i] = float(recall_top20[i]) / float(total_number)	
		recall_ctr_package[i] = float(recall_ctr_package[i]) /float(total_number)
	
	x = range(1, 21)
	pl.plot(x, recall_top20, label = "most_popular(benchmark)")
	pl.plot(x, recall_user_based_CF, label = "user_based_CF")
	#pl.plot(x, recall_user_based_CF1, label = "user_based_CF_topic_similar")
	#pl.plot(x, recall_user_based_CF2, label = "user_based_CF+description_similarity")
	pl.plot(x, recall_item_based_CF, label = "item_based_CF")
    	pl.plot(x, recall_pmf, label = "pmf")
    	pl.plot(x, recall_ctr, label = "ctr")
        #pl.plot(x, recall_ctr_v1, label = "embedding_v1")
        #pl.plot(x, recall_ctr_v2, label = "embedding_v2")
        #pl.plot(x, recall_ctr_v12, label = "embedding_repo")
	#pl.plot(x, recall_ctr_v1_, label = "embedding_v1_")
        #pl.plot(x, recall_ctr_v2_, label = "embedding_v2_")
        pl.plot(x, recall_ctr_v12_, label = "embedding_contibutors")
	pl.plot(x, recall_ctr_package, label = "embedding_package")	

	pl.ylabel('recall rate')
	pl.xlabel('recommend K libraries to each repository')
	pl.legend(loc='lower right')
	pl.savefig("recall_.png")
