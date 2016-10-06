import urllib2
import json

client_id = "885a451031ff820433b3"
client_secret = "27e532eaebe389c065a7e475aa183b2b379ca206"

for star_num in range(20, 0, -1):
	for fork_count in range(12, 0, -1):
		print star_num
		print fork_count
		i = 1
		print i
		while i < 11:
			url = "https://api.github.com/search/repositories?page=" + str(i) + "&per_page=100&q=language:Java+stars:" + str(star_num) + "+forks:" + str(fork_count) + "&client_id=" + client_id + "&client_secret=" + client_secret
			try:
				response = urllib2.urlopen(url)
			except urllib2.HTTPError as e:
				continue
			except urllib2.URLError as e:
				continue
			else:
				i = i + 1
				results = json.loads(response.read())
				print results["total_count"]
				if results["total_count"] <= 1000:
					for result in results["items"]:
						name = result["full_name"]
						description = result["description"]
						if description == None:
							description = ""
						star_num = result["stargazers_count"]
						fork_count = result["forks"]
						if result["fork"] == False:
							writer = open("java_repo_search_api_starfork.txt", "ab+")
							writer.write(name + "\t" + str(star_num) + "\t" + str(fork_count) + "\t")
							writer.write(description.encode("utf-8"))
							writer.write("\n")
				
