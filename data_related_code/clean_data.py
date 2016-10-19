import operator

reader = open("../data/java_repo_package.txt", "rb")
package_dict = dict()
packages_count = dict()
writer1 = open("../data/repo_package.txt", "wb")
writer1.write("repo_num" + '\t' + "repo_name" + '\t' + "package_num" + '\t' + "package_name" + '\n') 
writer2 = open("../data/repo_dict.txt", "wb")
writer2.write("repo_num" + '\t' + "repo_name" + '\t' + "star_count" + '\t' + "fork_count" + '\n')
repo_num = 1
package_count = 1
repo_dict = dict()
for line in reader:
	line = line.strip('\n').split('\t');
	l = len(line)
	if (l == 5 or l == 4) and not repo_dict.has_key(line[0]):
		repo_name = line[0]
		repo_dict[repo_name] = 0
		star = line[1]
		fork = line[2]
		
		index = line[l-1].find(':')
		package_info = line[l-1][index+1:].strip(' {}')
		package_info = package_info.split('), ')
		
		flag = False
		temp_dict = dict()
		for name in package_info:
			package_name_index = name.find(':')
			if package_name_index == -1:
				package_name_index = len(name)
			package_name = name[:package_name_index].replace('\\n', '').replace('\\t', '').strip('\\\n\t \'')
			package_name_index = package_name.find('.$')
			if package_name_index == -1:
				package_name_index = len(package_name)
			package_name = package_name[:package_name_index]
			if package_name != '' and package_name[0] != '$' and package_name[0] != '@' and package_name != "Not a proper repo retreived name.":
				flag = True
				package_num = package_count
				if package_dict.has_key(package_name):
					package_num = package_dict[package_name]
					#packages_count[package_name] += 1
				else:
					package_dict[package_name] = package_num
					#packages_count[package_name] = 1
					package_count += 1
				if not temp_dict.has_key(package_name):
					temp_dict[package_name] = 1
					writer1.write(str(repo_num) + '\t' + repo_name + '\t' + str(package_num) + '\t' + package_name + '\n')
		if flag:
			writer2.write(str(repo_num) + '\t' + repo_name + '\t' + star + '\t' + fork + '\n')
			repo_num += 1;		
writer1.close()
writer2.close()

writer = open("../data/package_dict.txt", "wb")
writer.write("package_num" + '\t' + "package_name" + '\n')
sorted_pd = sorted(package_dict.items(), key = operator.itemgetter(1))
for key in sorted_pd:
	#if packages_count[key] > 1:
	writer.write(str(key[1]) + '\t' + key[0] + '\n')
	#else:
	#	print key
writer.close()

		
