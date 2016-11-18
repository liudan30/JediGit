
reader1 = open('used_package.txt', 'rb')
writer1 = open('packageinfo.txt', 'wb')
writer1.write('[')
str = "";
for line in reader1:
	print line
	line = line.strip('\t\n').split('\t')
	str += '['
	print line
	for i in line:
		str += ('\'' + i + '\', ')
	str = str[:-2]
	str += '], '
writer1.write(str[:-2])
writer1.write('];')		
