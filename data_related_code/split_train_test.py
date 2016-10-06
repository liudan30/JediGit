import random

reader = open("../data/repo_package.txt", "rb")
packages_count = dict()
repo_count = dict()
writer1 = open("../data/repo_package_test.txt", "wb")
writer1.write("repo_num" + '\t' + "repo_name" + '\t' + "package_num" + '\t' + "package_count" + '\n')
writer2 = open("../data/repo_package_train.txt", "wb")
writer2.write("repo_num" + '\t' + "repo_name" + '\t' + "package_num" + '\t' + "package_count" + '\n')
for line in reader:
	line = line.strip('\n').split('\t')
	if line[0] == "repo_num":
		continue
	if packages_count.has_key(line[3]):
		packages_count[line[3]] += 1
	else:
		packages_count[line[3]] = 1
	if repo_count.has_key(line[1]):
                repo_count[line[1]] += 1
        else:
                repo_count[line[1]] = 1
reader.close()

reader = open("../data/repo_package.txt", "rb")
for line in reader:
        newline = line.strip('\n').split('\t')
	if newline[0] == "repo_num":
		continue
        if packages_count[newline[3]] > 1 and repo_count[newline[1]] > 1:
             	if random.random() < 0.2:
		   	writer1.write(line)
			packages_count[newline[3]] -= 1
			repo_count[newline[1]] -= 1
		else:
			writer2.write(line)
        else:
                writer2.write(line)		
