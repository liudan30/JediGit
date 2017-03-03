import urllib2
import json

client_id = "885a451031ff820433b3"
client_secret = "27e532eaebe389c065a7e475aa183b2b379ca206"
reader = open("../data/repo_dict.txt")

for line in reader:
    line = line.strip('\n').split('\t')
    if line[0] != "repo_num" and int(line[0]) > 15036:
	print str(line[0])
	shouldRetry = True
	while shouldRetry:
		url = "https://api.github.com/repos/" + line[1] + "/contributors" + "?client_id=" + client_id + "&client_secret=" + client_secret
		print url
		try:
			response = urllib2.urlopen(url)
		except urllib2.HTTPError as e:
			if e.code == 404:
				writer = open("../data/repo_novalid", "ab+")
                                writer.write(line[1] + "\n")
				shouldRetry = False
			print e
		except urllib2.URLError as e:
			print e
		else:
			results = json.loads(response.read())
			for result in results:
				name = result["login"]
                		times = result["contributions"]
                		writer = open("../data/repo_contributors.txt", "ab+")
				writer.write(line[1] + "\t" + str(name) + "\t" + str(times) + "\n")
            		shouldRetry = False
