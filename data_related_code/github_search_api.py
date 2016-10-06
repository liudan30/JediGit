import urllib2
import json

client_id = "885a451031ff820433b3"
client_secret = "27e532eaebe389c065a7e475aa183b2b379ca206"

star_num = 40000
general_star_num = 40000
should_search = True
repo = {}
while should_search:
	print str(len(repo))
	i = 1
	while i < 11:
		url = "https://api.github.com/search/repositories?page=" + str(i) + "&per_page=100&q=language:Java+stars:<=" + str(general_star_num) + "&sort=stars&order=desc" + "&client_id=" + client_id + "&client_secret=" + client_secret
		try:
			response = urllib2.urlopen(url)
		except urllib2.HTTPError as e:
			continue
		except urllib2.URLError as e:
			continue
		else:
			i = i + 1
			results = json.loads(response.read())
			if results["total_count"] == 0:
				should_search = False
			for result in results["items"]:
				name = result["full_name"]
				if repo.has_key(name):
					continue
				else:
					repo[name] = 1
				description = result["description"]
				if description == None:
					description = ""
				star_num = result["stargazers_count"]
				fork_count = result["forks"]
				if star_num == 20:
					should_search = False
				if result["fork"] == False and should_search:
					writer = open("java_repo_search_api.txt", "ab+")
					writer.write(name + "\t" + str(star_num) + "\t" + str(fork_count) + "\t")
					writer.write(description.encode("utf-8"))
					writer.write("\n")
		if should_search == False:
			break
	general_star_num = star_num
