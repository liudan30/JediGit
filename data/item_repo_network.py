writer1 = open("repo_package_network_train.txt", "wb")
for line in open("repo_package_train.txt"):
	line = line.strip('\n').split('\t')
	if line[0] == "repo_num":
		continue
	writer1.write(line[1] + ' ' + line[3] + ' 1\n')
	writer1.write(line[3] + ' ' + line[1] + ' 1\n')
