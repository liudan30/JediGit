var addressBook = ['dropwizard/dropwizard', 'perwendel/spark', 'square/otto', 'google/j2objc', 'junit-team/junit4', 'eclipse/vert.x', 'prestodb/presto', 'alibaba/druid', 'spring-projects/spring-mvc-showcase', 'Graylog2/graylog2-server', 'twitter/heron', 'JodaOrg/joda-time', 'Alluxio/alluxio', 'Vedenin/useful-java-links', 'alibaba/RocketMQ', 'square/javapoet', 'NLPchina/elasticsearch-sql', 'Bukkit/Bukkit', 'ben-manes/caffeine', 'tobie/ua-parser', 'JoanZapata/android-pdfview', 'iluwatar/java-design-patterns', 'biezhi/blade', 'eclipse/che', 'scribejava/scribejava', 'xetorthio/jedis', 'brettwooldridge/HikariCP', 'mybatis/mybatis-3', 'jhy/jsoup', 'apache/storm', 'stanfordnlp/CoreNLP', 'yui/yuicompressor', 'yinwang0/pysonar2', 'NLPchina/ansj_seg', 'naver/pinpoint', 'OpenTSDB/opentsdb', 'jankotek/mapdb', 'joelittlejohn/jsonschema2pojo', 'square/moshi', 'square/okhttp', 'spring-projects/spring-security-oauth', 'chanjarster/weixin-java-tools', 'antlr/antlr4', 'shekhargulati/99-problems', 'goldmansachs/gs-collections', 'bonnyfone/vectalign', 'netty/netty', 'JakeWharton/ActionBarSherlock', 'spring-projects/spring-boot', 'alibaba/dubbo', 'alibaba/fastjson', 'clojure/clojure', 'EnterpriseQualityCoding/FizzBuzzEnterpriseEdition', 'orfjackal/retrolambda', 'orientechnologies/orientdb', 'Atmosphere/atmosphere', 'square/okio', 'AsyncHttpClient/async-http-client', 'code4craft/webmagic', 'google/guava', 'google/binnavi', 'apache/zeppelin', 'weibocom/motan', 'kevinsawicki/http-request', 'twitter/distributedlog', 'grpc/grpc-java', 'hazelcast/hazelcast'];
chrome.runtime.onInstalled.addListener(function() {
  // Replace all rules ...
  chrome.declarativeContent.onPageChanged.removeRules(undefined, function() {
    for (i = 0; i < addressBook.length; i++) {
      chrome.declarativeContent.onPageChanged.addRules([
        {
          conditions: [
            new chrome.declarativeContent.PageStateMatcher({
            pageUrl: { urlContains: addressBook[i] },
            })
          ],
          actions: [ new chrome.declarativeContent.ShowPageAction() ]
        }
      ]);
    }
  });
});
