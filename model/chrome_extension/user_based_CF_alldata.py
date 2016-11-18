import common_function
from sets import Set

sample_repo = Set(['github.com/square/retrofit', 'github.com/square/okhttp', 'github.com/iluwatar/java-design-patterns', 'github.com/google/iosched', 'github.com/google/guava', 'github.com/PhilJay/MPAndroidChart', 'github.com/zxing/zxing', 'github.com/jfeinstein10/SlidingMenu', 'github.com/libgdx/libgdx', 'github.com/excilys/androidannotations', 'github.com/JakeWharton/ViewPagerIndicator', 'github.com/netty/netty', 'github.com/chrisbanes/Android-PullToRefresh', 'github.com/spring-projects/spring-boot', 'github.com/JakeWharton/ActionBarSherlock', 'github.com/alibaba/fastjson', 'github.com/alibaba/dubbo', 'github.com/EnterpriseQualityCoding/FizzBuzzEnterpriseEdition', 'github.com/clojure/clojure', 'github.com/nhaarman/ListViewAnimations', 'github.com/junit-team/junit4', 'github.com/eclipse/vert.x', 'github.com/prestodb/presto', 'github.com/dropwizard/dropwizard', 'github.com/perwendel/spark', 'github.com/square/otto', 'github.com/google/j2objc', 'github.com/alibaba/druid', 'github.com/emilsjolander/StickyListHeaders', 'github.com/openzipkin/zipkin', 'github.com/xetorthio/jedis', 'github.com/scribejava/scribejava', 'github.com/google/auto', 'github.com/apache/storm', 'github.com/jhy/jsoup', 'github.com/mybatis/mybatis-3', 'github.com/brettwooldridge/HikariCP', 'github.com/eclipse/che', 'github.com/ACRA/acra', 'github.com/AsyncHttpClient/async-http-client', 'github.com/code4craft/webmagic', 'github.com/lecho/hellocharts-android', 'github.com/JakeWharton/DiskLruCache', 'github.com/bauerca/drag-sort-listview', 'github.com/square/okio', 'github.com/Atmosphere/atmosphere', 'github.com/cyrilmottier/GreenDroid', 'github.com/orfjackal/retrolambda', 'github.com/orientechnologies/orientdb', 'github.com/alibaba/RocketMQ', 'github.com/Vedenin/useful-java-links', 'github.com/alibaba/jstorm', 'github.com/square/javapoet', 'github.com/twitter/heron', 'github.com/johncarl81/parceler', 'github.com/Alluxio/alluxio', 'github.com/JodaOrg/joda-time', 'github.com/Graylog2/graylog2-server', 'github.com/spring-projects/spring-mvc-showcase', 'github.com/stanfordnlp/CoreNLP', 'github.com/yui/yuicompressor', 'github.com/yinwang0/pysonar2', 'github.com/psaravan/JamsMusicPlayer', 'github.com/NLPchina/ansj_seg', 'github.com/naver/pinpoint', 'github.com/OpenTSDB/opentsdb', 'github.com/jankotek/mapdb', 'github.com/joelittlejohn/jsonschema2pojo', 'github.com/square/moshi', 'github.com/grpc/grpc-java', 'github.com/twitter/distributedlog', 'github.com/kevinsawicki/http-request', 'github.com/weibocom/motan', 'github.com/apache/zeppelin', 'github.com/google/binnavi', 'github.com/androidquery/androidquery', 'github.com/owncloud/android', 'github.com/RobotiumTech/robotium', 'github.com/hazelcast/hazelcast', 'github.com/tobie/ua-parser', 'github.com/alibaba/canal', 'github.com/Bukkit/Bukkit', 'github.com/ben-manes/caffeine', 'github.com/JoanZapata/android-pdfview', 'github.com/wildfly/wildfly', 'github.com/square/wire', 'github.com/pedrovgs/Algorithms', 'github.com/bytedeco/javacpp', 'github.com/NLPchina/elasticsearch-sql', 'github.com/antlr/antlr4', 'github.com/chanjarster/weixin-java-tools', 'github.com/bigbluebutton/bigbluebutton', 'github.com/shekhargulati/99-problems', 'github.com/robovm/robovm', 'github.com/gephi/gephi', 'github.com/bonnyfone/vectalign', 'github.com/goldmansachs/gs-collections', 'github.com/maurycyw/StaggeredGridView', 'github.com/spring-projects/spring-security-oauth', 'github.com/biezhi/blade'])

user_item_user = dict()
user_item_user_similarity = dict()
def recommendation(user_item_dict, user_similarity, repo_id_name_dict):
	user_item_recommendation = dict()
	for user in user_item_dict:
		repo_name = 'github.com/' + repo_id_name_dict[user]
		if repo_name in sample_repo:
			user_item_recommendation[user] = dict()
			user_item_user[user] = dict()
			user_item_user_similarity[user] = dict()
			for similar_user in user_similarity[user]:
				for item in user_item_dict[similar_user[0]]:
					if item not in user_item_dict[user]:
						if not user_item_recommendation[user].has_key(item):
							user_item_recommendation[user][item] = 0
							user_item_user_similarity[user][item] = 0
						user_item_recommendation[user][item] += similar_user[1]
						if similar_user[1] > user_item_user_similarity[user][item]:
							user_item_user_similarity[user][item] = similar_user[1]
							user_item_user[user][item] = similar_user[0]
	for user in user_item_recommendation:
		user_item_recommendation[user] = sorted(user_item_recommendation[user].iteritems(), key=lambda d:d[1], reverse = True)[:3]
	return user_item_recommendation

packages = Set()

def write_recommendation_result(filename, top_3_items, repo_id_name_dict, package_id_name_dict):
	writer = open(filename, "wb")
	for user in top_3_items:
		repo_name = 'github.com/' + repo_id_name_dict[user]
		if repo_name in sample_repo:
			writer.write(repo_id_name_dict[user])
			writer.write('\n')
			for item in top_3_items[user]:
				writer.write(package_id_name_dict[item[0]])
				packages.add(package_id_name_dict[item[0]])
				writer.write('\t')
				print user
				print item
				print user_item_user[user][item[0]]
				writer.write(repo_id_name_dict[user_item_user[user][item[0]]])
				writer.write('\t')
			writer.write('\n')
	writer.close()
	writer = open('used_package.txt', 'wb')
	for package in packages:
		writer.write(package)
		writer.write('\n')
	writer.close()

def getUsefulUserItemDict(user_item_dict, repo_id_name_dict):
	items = Set()
	newdict = dict()
	for user in user_item_dict:
		repo_name = 'github.com/' + repo_id_name_dict[user]
		if repo_name in sample_repo:
			items = items.union(user_item_dict[user])	
	print len(items)
	for user in user_item_dict:
		newset = items.intersection(user_item_dict[user])
		if len(newset) > 0:
			print len(newset)
			newdict[user] = user_item_dict[user]
	print len(newdict)
	return newdict

if __name__ == "__main__":
	user_item_dict = common_function.read_user_item_dict("../../data/repo_package.txt")
	repo_id_name_dict = common_function.read_dict("../../data/repo_dict.txt")
        package_id_name_dict = common_function.read_dict("../../data/package_dict.txt")
	useful_user_item_dict = getUsefulUserItemDict(user_item_dict, repo_id_name_dict)
	user_similarity = common_function.compute_jaccard_similarity(useful_user_item_dict, 100)
	top_3_items = recommendation(user_item_dict, user_similarity, repo_id_name_dict)
	write_recommendation_result("recommendation_result_user_based_CF_alldata.txt", top_3_items, repo_id_name_dict, package_id_name_dict)
