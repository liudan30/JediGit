reader = open('final_result.txt', 'rb')
writer1 = open('1.txt', 'wb')
writer1.write('[')
str = "";
for line in reader:
	line = line.strip('\t\n').split('\t')
	str += '['
	for i in line:
		str += ('\'' + i + '\', ')
	str = str[:-2]
	str += '], '
writer1.write(str[:-2])
writer1.write('];')			
