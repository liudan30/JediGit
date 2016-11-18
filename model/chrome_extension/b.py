from sets import Set

reader1 = open('unused_package.txt', 'rb')
unused = Set()
for line in reader1:
	line = line.strip('\t\n')
	unused.add(line)

reader = open('final_result.txt', 'rb')
writer2 = open('reponame.txt', 'wb')
writer1 = open('repoinfo.txt', 'wb')
writer1.write('[')
writer2.write('[')
str = "";
str2 = "";
for line in reader:
	line = line.strip('\t\n').split('\t')
	if line[1] not in unused and line[3] not in unused and line[5] not in unused: 
		str += '['
		for i in line:
			str += ('\'' + i + '\', ')
		str = str[:-2]
		str += '], '
		str2 += ('\'' + line[0] + '\', ')
writer1.write(str[:-2])
writer1.write('];')		
writer2.write(str2[:-2])
writer2.write(']:')	
