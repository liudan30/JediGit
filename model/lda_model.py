import lda
import numpy
from sets import Set
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer

def read_dict(filename):
	reader = open(filename, "rb")
        dict_ = dict()
	for line in reader:
		line = line.strip('\n').split('\t')
		if line[0] == "repo_num" or line[0] == "package_num":
			continue
		dict_[line[1]] = line[0]
	print len(dict_)
	return dict_

def repo_description(repo_dict):
	tokenizer = RegexpTokenizer(r'\w+')
        en_stop = get_stop_words('en')
        p_stemmer = PorterStemmer()

	vocal = dict()
	description_dict = dict()
	
	reader = open("../data/github_java_repo.txt", "rb")
	for line in reader:
		line = line.strip('\t\n').split('\t')
		if repo_dict.has_key(line[0]):
			text = '\t'.join(line[3:])
			raw = text.lower()
			tokens = tokenizer.tokenize(raw)
			stopped_tokens = [i for i in tokens if not i in en_stop]
        		texts = [p_stemmer.stem(i) for i in stopped_tokens]
			
			for voc in texts:
				if voc not in vocal:
					vocal[voc] = len(vocal)

			description_dict[repo_dict[line[0]]] = Set(texts)
	print len(description_dict), len(vocal)
	return description_dict, vocal

def generate_matrix(description_dict, vocal):
	X = numpy.full((len(description_dict), len(vocal)), 0, dtype=numpy.int)
	print X.shape
	for repo_num in description_dict:
		for word in description_dict[repo_num]:
			X[int(repo_num) - 1][vocal[word]] += 1
	return X
		

if __name__ == "__main__":
	repo_dict = read_dict("../data/repo_dict.txt")
	description_dict, vocal = repo_description(repo_dict)
	
	X = generate_matrix(description_dict, vocal)
	
	model = lda.LDA(n_topics = 20, n_iter = 1500, random_state = 1)
	model.fit(X)
	doc_topic = model.doc_topic_
	print doc_topic.shape
	print doc_topic
