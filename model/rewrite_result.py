

def get_top20(filename):
        reader = open(filename, "rb")
        top_20 = []
        for line in reader:
                line = line.strip('\n').split('\t')
                top_20 += line
        return top_20

def recall_CF(top20, filename, newfilename):
	reader = open(filename, "rb")
        writer = open(newfilename, "wb")
	for line in reader:
                line = line.strip('\n').split('\t')
                repo_name = line[0]
                packages = line[1:] + top20
                packages = packages[:20]
		writer.write(repo_name)
		for i in range(0, 20):
			writer.write('\t')
			writer.write(packages[i])
		writer.write('\n')

if __name__ == "__main__":
	top_20 = get_top20("top-20.txt")
	recall_user_based_CF = recall_CF(top_20, "recommendation_result_user_based_CF.txt", "recommendation_result_user_based_CF_.txt")
        recall_item_based_CF = recall_CF(top_20, "recommendation_result_item_based_CF.txt", "recommendation_result_item_based_CF_.txt")
