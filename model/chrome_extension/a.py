reader = open('recommendation_result_user_based_CF_alldata.txt', 'rb')
currentRepo = ""
writer = open('final_result.txt', 'wb')
writer1 = open('1.txt', 'wb')
writer1.write('[')
for line in reader:
	line = line.strip('\t\n').split('\t')
	if len(line) == 1:
		currentRepo = line[0]
	else:
		if len(line) == 6:
			writer1.write('\'github.com/' + currentRepo + '\', ') 
			writer.write(currentRepo)
			for i in line:
				writer.write('\t')
				writer.write(i)
			writer.write('\n')
writer1.write(']')			
