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
	top_20 = get_top20("../model/top-20.txt")
	total_number, test_data = get_test_data("../data/repo_package_test.txt")

	recall_pmf = recall_CF(top_20, test_data, "recommendation_result_pmf.txt")
	recall_pmf1 = recall_CF(top_20, test_data, "recommendation_result_pmf_0.02.txt")
	recall_pmf2 = recall_CF(top_20, test_data, "recommendation_result_pmf_0.015.txt")
	recall_pmf3 = recall_CF(top_20, test_data, "recommendation_result_pmf_0.0075.txt")
	recall_pmf4 = recall_CF(top_20, test_data, "recommendation_result_pmf_0.005.txt")

	for i in range(0, 20):
		recall_pmf[i] = float(recall_pmf[i]) / float(total_number)
		recall_pmf1[i] = float(recall_pmf1[i]) / float(total_number)
		recall_pmf2[i] = float(recall_pmf2[i]) / float(total_number)
		recall_pmf3[i] = float(recall_pmf3[i]) / float(total_number)
		recall_pmf4[i] = float(recall_pmf4[i]) / float(total_number)

	x = range(1, 21)
	pl.plot(x, recall_pmf, label = "pmf_0.01")
	pl.plot(x, recall_pmf1, label = "pmf_0.02")
	pl.plot(x, recall_pmf2, label = "pmf_0.015")
	pl.plot(x, recall_pmf3, label = "pmf_0.0075")
	pl.plot(x, recall_pmf4, label = "pmf_0.005")

	pl.ylabel('recall rate')
	pl.xlabel('recommend K libraries to each repository')
	pl.legend(loc='lower right')
	pl.savefig("recall.png")
