from sets import Set
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer

def read_user_item_dict(filename):
        reader = open(filename, "rb")
        user_item_dict = dict()
        user_set = Set()
        item_set = Set()
        for line in reader:
                line = line.strip('\n').split('\t')
                if line[0] == "repo_num":
                        continue
                user_index = int(line[0]) - 1
                item_index = int(line[2]) - 1
                if not user_item_dict.has_key(user_index):
                        user_item_dict[user_index] = Set()
                user_item_dict[user_index].add(item_index)
                user_set.add(user_index)
                item_set.add(item_index)
        return user_item_dict, len(user_set), len(item_set)

def write_recommendation_result(filename, top_20_items, repo_id_name_dict, package_id_name_dict):
	writer = open(filename, "wb")
	for user_index in xrange(len(top_20_items)):
		writer.write(repo_id_name_dict[user_index])
		for i in xrange(len(top_20_items[user_index])):
			writer.write('\t')
			writer.write(package_id_name_dict[top_20_items[user_index][i]])
		writer.write('\n')
	writer.close()

def read_dict(filename):
	reader = open(filename, "rb")
        dict_ = dict()
	for line in reader:
		line = line.strip('\n').split('\t')
		if line[0] == "repo_num" or line[0] == "package_num":
			continue
		dict_[int(line[0]) - 1] = line[1]
	return dict_

def read_dict_(filename):
	reader = open(filename, "rb")
        dict_ = dict()
	for line in reader:
		line = line.strip('\n').split('\t')
		if line[0] == "repo_num" or line[0] == "package_num":
			continue
		dict_[line[1]] = int(line[0]) - 1
	print len(dict_)
	return dict_

def repo_description(repo_dict):
	tokenizer = RegexpTokenizer(r'\w+')
        en_stop = get_stop_words('en')
        p_stemmer = PorterStemmer()

	vocal = dict()
	doc_ids = dict()
	doc_cnt = dict()

	reader = open("../data/github_java_repo.txt", "rb")
	for line in reader:
		line = line.strip('\t\n').split('\t')
		if repo_dict.has_key(line[0]):
			text = '\t'.join(line[3:])
			raw = text.lower()
			tokens = tokenizer.tokenize(raw)
			stopped_tokens = [i for i in tokens if not i in en_stop]
        		texts = [p_stemmer.stem(i) for i in stopped_tokens]

			doc_ids[repo_dict[line[0]]] = []
			doc_cnt[repo_dict[line[0]]] = []
			voc_local = dict()

			for voc in texts:
				if voc not in vocal:
					vocal[voc] = len(vocal)
				if voc not in voc_local:
					voc_local[voc] = len(voc_local)
					doc_ids[repo_dict[line[0]]].append(vocal[voc])
					doc_cnt[repo_dict[line[0]]].append(0)
				doc_cnt[repo_dict[line[0]]][voc_local[voc]] += 1

	return doc_ids, doc_cnt, len(vocal)
