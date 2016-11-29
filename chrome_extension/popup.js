var view = new Swiper('.view', {
   spaceBetween: 15
});
var nav = new Swiper('.nav', {
   spaceBetween: 30,
   slidesPerView: 'auto',
   touchRatio: 1,
   centeredSlides: true,
   slideToClickedSlide: true,
   onSlideChangeEnd: function(){
    $('.nav,.bottom,.view').removeClass('active');
   }
});

$('.content').each(function(){
  var t = $(this),
    content = new Swiper(t, {
      scrollbar: t.find('.swiper-scrollbar'),
      direction: 'vertical',
      slidesPerView: 'auto',
      mousewheelControl: true,
         spaceBetween: 15,
         freeMode: true,
         grabCursor: true,
         onSliderMove: function(swiper){
          if(swiper.activeIndex > 0){
            $('.nav,.bottom,.view').addClass('active');
          }else{
               $('.nav,.bottom,.view').removeClass('active');
          }
         },
         onSlideChangeEnd: function(swiper){
          if(swiper.activeIndex > 0){
            $('.nav,.bottom,.view').addClass('active');
          }else{
               $('.nav,.bottom,.view').removeClass('active');
          }
         },
         onScroll:  function(swiper){
          if(swiper.activeIndex > 0){
            $('.nav,.bottom,.view').addClass('active');
          }else{
               $('.nav,.bottom,.view').removeClass('active');
          }
         }
    });
})

view.params.control = nav;
nav.params.control = view;


var repoinfo = [['dropwizard/dropwizard', 'junit', 'minisu/Dropwizard-EnvVar-Interpolation', 'org.mockito', 'bazaarvoice/dropwizard-caching-bundle', 'org.assertj', 'devops-course/kinneret-server'], ['perwendel/spark', 'com.google.guava', 'Alfresco/alfresco-indexer', 'ch.qos.logback', 'chanjarster/weixin-java-tools', 'org.hamcrest', 'sonyxperiadev/gerrit-events'], ['square/otto', 'com.actionbarsherlock', 'ginatrapani/todo.txt-android', 'junit', '3332523ma/library_universalimageloader', 'org.robolectric', '3332523ma/library_universalimageloader'], ['google/j2objc', 'org.slf4j', 'camunda/camunda-bpm-mockito', 'com.fasterxml.jackson.core', 'HubSpot/jackson-datatype-protobuf', 'org.apache.commons', 'camunda/camunda-bpm-mockito'], ['junit-team/junit4', 'junit', 'rdclark/pptx2html', 'org.mockito', 'valid4j/valid4j', 'org.slf4j', 'Progether/JAdventure'], ['eclipse/vert.x', 'org.mockito', 'zalando/tokens', 'org.springframework', 'gerrytan/stockticker', 'com.google.guava', 'metanet/p2p'], ['prestodb/presto', 'org.slf4j', 'dropbox/presto-kafka-connector', 'junit', 'binarywang/java-generator', 'org.mockito', 'killbill/killbill'], ['alibaba/druid', 'org.aspectj', 'sogyf/mybatis-pagination', 'cglib', 'ianso/scriptus', 'commons-io', 'wosyingjun/beauty_ssm'], ['spring-projects/spring-mvc-showcase', 'javax.servlet', 'yrojha4ever/JavaStudSpringMVCWeb', 'commons-dbcp', 'hot13399/spring-mvc-REST', 'org.apache.tiles', 'bijukunjummen/spring-mvc-test-sample'], ['Graylog2/graylog2-server', 'junit', 'intelie/graylog2-plugin-output-syslog', 'org.mockito', 'Graylog2/graylog-plugin-pagerduty', 'org.slf4j', 'Graylog2/graylog-plugin-slack'], ['twitter/heron', 'com.google.guava', 'openengsb/openengsb', 'org.slf4j', 'Contrast-Security-OSS/contrast-sdk-java', 'org.hamcrest', 'bdemers/maven-wrapper'], ['JodaOrg/joda-time', 'com.google.guava', 'JodaOrg/joda-convert', 'org.testng', 'JodaOrg/joda-money', 'org.apache.maven.doxia', 'pro-grade/pro-grade'], ['Alluxio/alluxio', 'junit', 'lucidworks/yarn-proto', 'org.apache.hbase', 'IBMStreams/streamsx.hbase', 'org.apache.hive', 'brndnmtthws/facebook-hive-udfs'], ['Vedenin/useful-java-links', 'junit', 'jpush/jpush-java-library', 'org.apache.httpcomponents', 'plivo/plivo-java', 'org.mockito', 'twitter/hpack'], ['alibaba/RocketMQ', 'org.springframework', 'hengyunabc/zpush', 'com.google.guava', 'hengyunabc/douyu-helper', 'org.apache.httpcomponents', 'tangqian/12306_ticket'], ['square/javapoet', 'com.google.guava', 'google/auto', 'org.hamcrest', 'JeffreyWei/java-common-showcase', 'joda-time', 'MagenTys/cherry'], ['NLPchina/elasticsearch-sql', 'org.testng', 'bleskes/elasticfacets', 'org.slf4j', 'DavidValeri/blog-sonar-it', 'org.mockito', 'sw360/sw360portal'], ['Bukkit/Bukkit', 'org.mockito', 'Aconex/json-log4j-layout', 'log4j', 'Aconex/json-log4j-layout', 'commons-io', 'openengsb/openengsb'], ['ben-manes/caffeine', 'org.mockito', 'JakeWharton/RxRelay', 'com.google.guava', 'vbauer/caesar', 'com.google.code.gson', 'i13tum/i13kv'], ['tobie/ua-parser', 'org.mockito', 'JeffreyWei/java-common-showcase', 'com.google.guava', 'hgwood/java8-streams-and-exceptions', 'commons-lang', 'jonathanhds/sql-builder'], ['JoanZapata/android-pdfview', 'com.squareup', 'pyricau/androidannotations-dagger-example', 'com.google.code.gson', 'play/play-android', 'com.github.kevinsawicki', 'kevinsawicki/hindstock'], ['iluwatar/java-design-patterns', 'org.springframework', 'nociar/jpa-cloner', 'mysql', 'saltnlight5/java-ee6-examples', 'org.apache.tomcat', 'apache/tomcat'], ['biezhi/blade', 'log4j', 'DavidValeri/blog-sonar-it', 'org.mockito', 'apereo/cas-server-security-filter', 'com.google.code.gson', 'geoquest/Public-GQ-Player-Android--1'], ['eclipse/che', 'xerces', 'julianhyde/eigenbase-xom', 'org.hsqldb', 'flyway/flyway', 'com.amazonaws', 'corley/aws-ant-task'], ['scribejava/scribejava', 'org.apache.httpcomponents', 'mmarum-sugarcrm/sugarcrm-api-java', 'org.apache.commons', 'iyzico/iyzipay-java', 'commons-io', 'sendwithus/sendwithus_java'], ['xetorthio/jedis', 'commons-io', 'RNCryptor/JNCryptor', 'com.google.code.gson', 'danithaca/drupal-computing', 'org.hamcrest', 'dtitov/bracer'], ['brettwooldridge/HikariCP', 'org.springframework', 'camunda/camunda-bpm-mockito', 'ch.qos.logback', 'camunda/camunda-bpm-platform-osgi', 'org.hamcrest', 'camunda/camunda-bpm-mockito'], ['mybatis/mybatis-3', 'org.springframework', 'gratiartis/multids-demo', 'org.hibernate', 'gratiartis/multids-demo', 'mysql', 'akwei/halo-query'], ['jhy/jsoup', 'org.mockito', 'twitter/hpack', 'org.apache.httpcomponents', 'chrislusf/WeedFSClient', 'org.apache.commons', 'danithaca/drupal-computing'], ['apache/storm', 'junit', 'Storm-Applied/C2-Github-commit-count', 'org.slf4j', 'iotcloud/storm-broker-connectors', 'com.google.guava', 'gdfm/partial-key-grouping'], ['stanfordnlp/CoreNLP', 'junit', 'fengyouchao/esocks', 'ch.qos.logback', 'qos-ch/logback-audit', 'org.apache.camel', 'FuseByExample/camel-example-tcpip-proxy'], ['yui/yuicompressor', 'junit', 'gardentree/jambalaya', 'javax.servlet', 'SomMeri/less-wro-wicket', 'org.slf4j', 'redminenb/redminenb'], ['yinwang0/pysonar2', 'junit', 'flipkart-incubator/zjsonpatch', 'org.slf4j', 'Neuw84/RAKE-Java', 'commons-codec', 'Energy0124/MCFreedomLauncher'], ['NLPchina/ansj_seg', 'junit', 'altamiracorp/lucene-compression', 'org.apache.solr', 'chenlb/mmseg4j-from-googlecode', 'org.elasticsearch', 'springyweb/elasticsearch-customisations'], ['naver/pinpoint', 'org.hibernate', 'yiduwangkai/dubbox-solr', 'commons-fileupload', 'yiduwangkai/dubbox-solr', 'commons-dbcp', 'baichengzhou/SpringMVC-Mybatis-Shiro-redis-0.2'], ['OpenTSDB/opentsdb', 'commons-io', 'Jimmy-Shi/bean-query', 'org.apache.httpcomponents', 'eugenp/REST-With-Spring', 'org.springframework', 'eugenp/REST-With-Spring'], ['jankotek/mapdb', 'org.mockito', 'tmorcinek/android-codegenerator-library', 'org.slf4j', 'alexvictoor/ESLab', 'org.apache.commons', 'tmorcinek/android-codegenerator-library'], ['joelittlejohn/jsonschema2pojo', 'junit', 'zenria/Weed-FS-Java-Client', 'org.slf4j', 'crazycodeboy/BreakPointUploadUtil', 'com.google.guava', 'FasterXML/jackson-datatype-guava'], ['square/moshi', 'org.mockito', 'xebia-france/code-elevator', 'org.slf4j', 'joel-costigliola/assertj-swing', 'com.google.guava', 'IanEsling/fyodor'], ['square/okhttp', 'junit', 'apn-proxy/apn-socks', 'org.slf4j', 'ctripcorp/apollo', 'com.google.code.gson', 'PocketServer/PocketServer-Ref'], ['spring-projects/spring-security-oauth', 'org.hamcrest', 'JeffreyWei/java-common-showcase', 'log4j', 'drankye/haox', 'joda-time', 'jenkinsci/categorized-view-plugin'], ['chanjarster/weixin-java-tools', 'com.google.guava', 'devhub-tud/jenkins-ws-client', 'org.apache.commons', 'devhub-tud/jenkins-ws-client', 'org.hamcrest', 'devhub-tud/jenkins-ws-client'], ['antlr/antlr4', 'commons-io', 'mulesoft/npm-maven-plugin', 'org.apache.maven.plugin-testing', 'sap-production/resolve-pom-maven-plugin', 'org.mockito', 'orctom/was-maven-plugin'], ['shekhargulati/99-problems', 'org.mockito', 'JeffreyWei/java-common-showcase', 'org.jmock', 'grumpyjames/limits_of_tda', 'org.apache.commons', 'RIPE-NCC/ipresource'], ['goldmansachs/gs-collections', 'ch.qos.logback', 'DhyanB/Open-Imaging', 'log4j', 'saces/MimeUtil', 'io.netty', 'Hailei/java-redis'], ['bonnyfone/vectalign', 'org.antlr', 'codelion/gramtest', 'org.apache.hadoop', 'tweetmagik/spark-yarn', 'log4j', 'aerospike/delete-set'], ['netty/netty', 'junit', 'prb/bigbird', 'javax.servlet', 'rstoyanchev/spring-sockjs-protocol-webapp', 'org.apache.solr', 'treygrainger/solr-in-action'], ['JakeWharton/ActionBarSherlock', 'junit', 'nicolasjafelle/HoloForFroyo', 'org.robolectric', '3332523ma/library_universalimageloader', 'com.googlecode.androidannotations', 'pyricau/androidannotations-dagger-example'], ['spring-projects/spring-boot', 'javax.servlet', 'steveliles/jetty-embedded-spring-mvc', 'junit', 'bkielczewski/example-spring-mvc-jetty', 'org.slf4j', 'bkielczewski/example-spring-mvc-jetty'], ['alibaba/dubbo', 'junit', 'diandian-dev/diandian-api-sdk-java', 'org.slf4j', 'alibaba/simpleimage', 'org.springframework', 'kimmking/dubbo-jms'], ['alibaba/fastjson', 'org.slf4j', 'inkysea/vmware-vrealize-automation', 'log4j', 'qcri-social/AIDR', 'org.hibernate', 'qcri-social/AIDR'], ['clojure/clojure', 'junit', 'lunkdjedi/clj-ta-lib', 'storm', 'xumingming/storm-lib', 'log4j', '12306NgSQL/12306ngSQL'], ['EnterpriseQualityCoding/FizzBuzzEnterpriseEdition', 'org.slf4j', 'deas/contentreich-eml', 'javax.servlet', 'daniellitoc/xultimate-remoting', 'org.mockito', 'chrishenkel/spring-angularjs-tutorial-2'], ['orfjackal/retrolambda', 'junit', 'google/allocation-instrumenter', 'commons-io', 'fp1203/hotcode', 'org.mockito', 'ogrodnek/asperatus'], ['orientechnologies/orientdb', 'junit', 'orientechnologies/orientdb-jdbc', 'org.testng', 'orientechnologies/orientdb-lucene', 'org.hamcrest', 'orientechnologies/orientdb-jdbc'], ['Atmosphere/atmosphere', 'junit', 'flowersinthesand/portal-java', 'ch.qos.logback', 'spyboost/atmosphere-chat-angular', 'org.slf4j', 'flowersinthesand/portal-java'], ['square/okio', 'junit', 'ignl/BinarySearchTrees', 'org.slf4j', 'OpenHFT/jvm-micro-benchmarks', 'com.google.guava', 'serkan-ozal/ocean-of-memories'], ['AsyncHttpClient/async-http-client', 'junit', 'timboudreau/netty-http-client', 'org.slf4j', 'ACE-Caedmon/NG-Socket', 'log4j', 'buddygjw/nettyWebsocket'], ['code4craft/webmagic', 'ch.qos.logback', 'PhantomThief/model-view-builder', 'org.mockito', 'steveash/guavate', 'commons-io', 'dhorions/boxable'], ['google/guava', 'com.google.guava', 'google/compile-testing', 'org.mockito', 'KengoTODA/findbugs-slf4j', 'org.slf4j', 'google/openrtb-doubleclick'], ['google/binnavi', 'org.slf4j', 'takari/takari-smart-builder', 'com.google.inject', '99soft/rocoto', 'org.springframework', 'The-Alchemist/hibernate-postgresql'], ['apache/zeppelin', 'log4j', 'rdiachenko/jlv', 'org.hamcrest', 'tdunning/knn', 'org.springframework', 'imetaxas/double-entry-booking-spring-jta'], ['weibocom/motan', 'junit', 'Glamdring/google-plus-java-api', 'ch.qos.logback', 'sd4324530/fastweixin', 'com.fasterxml.jackson.core', 'Glamdring/google-plus-java-api'], ['kevinsawicki/http-request', 'javax.servlet', 'rchatley/SimpleWebApp', 'com.sun.jersey', 'heroku/template-java-jaxrs', 'org.apache.jmeter', 'kawasima/jmeter-websocket'], ['twitter/distributedlog', 'ch.qos.logback', 'synchronoss/nio-stream-storage', 'org.hamcrest', 'leveluplunch/levelup-java-exercises', 'commons-io', 'dhorions/boxable'], ['grpc/grpc-java', 'junit', 'dconnelly/grpc-error-example', 'org.apache.avro', 'opencb/ga4gh', 'org.mockito', 'coreos/jetcd'], ['hazelcast/hazelcast', 'junit', 'ThoughtWire/hazelcast-locks', 'org.slf4j', 'velo/sonar-pull-request-integration', 'org.apache.maven', 'duns/maven-swig-plugin']];
var packageinfo = [['ch.qos.logback', 'http://logback.qos.ch/'], ['com.fasterxml.jackson.core', 'https://github.com/FasterXML/jackson-core/wiki'], ['commons-dbcp', 'https://commons.apache.org/proper/commons-dbcp/'], ['com.googlecode.androidannotations', 'http://androidannotations.org/'], ['org.hibernate', 'http://hibernate.org/'], ['android.support', 'https://developer.android.com/topic/libraries/support-library/index.html'], ['org.jboss.xnio', 'http://xnio.jboss.org/'], ['org.assertj', 'http://joel-costigliola.github.io/assertj/'], ['javax.servlet', 'http://docs.oracle.com/javaee/6/api/javax/servlet/package-summary.html'], ['cglib', 'https://github.com/cglib/cglib/wiki'], ['mysql', 'http://dev.mysql.com/doc/refman/5.7/en/ha-memcached-interfaces-java.html'], ['org.hsqldb', 'http://hsqldb.org/'], ['com.google.zxing', 'https://github.com/zxing/zxing'], ['org.apache.avro', 'https://avro.apache.org/'], ['org.slf4j', 'http://www.slf4j.org/'], ['org.jmock', 'http://www.jmock.org/'], ['com.facebook.fresco', 'http://frescolib.org/index.html'], ['com.amazonaws', 'http://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/package-summary.html'], ['com.actionbarsherlock', 'http://actionbarsherlock.com/'], ['xerces', 'https://xerces.apache.org/'], ['org.mockito', 'http://site.mockito.org/'], ['com.google.code.gson', 'https://github.com/google/gson'], ['org.apache.maven.doxia', 'https://maven.apache.org/doxia/'], ['org.apache.kafka', 'https://kafka.apache.org/'], ['org.elasticsearch', 'https://github.com/elastic/elasticsearch-groovy'], ['org.apache.hbase', 'http://hbase.apache.org/'], ['com.sothree.slidinguppanel', 'https://github.com/umano/AndroidSlidingUpPanel'], ['joda-time', 'http://www.joda.org/joda-time/'], ['junit', 'http://junit.org/junit4/'], ['commons-codec', 'https://commons.apache.org/proper/commons-codec/'], ['org.codehaus.plexus', 'https://codehaus-plexus.github.io/'], ['org.apache.jmeter', 'http://jmeter.apache.org/'], ['com.google.guava', 'https://github.com/google/guava'], ['org.apache.camel', 'http://camel.apache.org/'], ['org.apache.hadoop', 'http://hadoop.apache.org/'], ['org.antlr', 'http://www.antlr.org/'], ['org.apache.maven', 'https://maven.apache.org/'], ['org.apache.hive', 'https://hive.apache.org/'], ['org.apache.httpcomponents', 'https://hc.apache.org/'], ['org.apache.maven.plugin-testing', 'http://maven.apache.org/plugin-testing/'], ['commons-io', 'http://commons.apache.org/proper/commons-io/'], ['org.hamcrest', 'http://hamcrest.org/JavaHamcrest/'], ['storm', 'http://storm.apache.org/'], ['com.google.inject', 'https://github.com/google/guice'], ['org.aspectj', 'https://eclipse.org/aspectj/'], ['org.testng', 'http://testng.org/doc/index.html'], ['org.apache.tiles', 'https://tiles.apache.org/'], ['com.github.kevinsawicki', 'https://github.com/kevinsawicki/http-request'], ['org.apache.solr', 'http://lucene.apache.org/solr/'], ['log4j', 'http://logging.apache.org/log4j/2.x/'], ['org.robolectric', 'http://robolectric.org/'], ['org.springframework', 'https://projects.spring.io/spring-framework/'], ['org.netbeans.modules', 'https://netbeans.org/'], ['commons-fileupload', 'https://commons.apache.org/proper/commons-fileupload/'], ['com.sun.jersey', 'https://jersey.java.net/'], ['io.netty', 'http://netty.io/'], ['commons-lang', 'https://commons.apache.org/proper/commons-lang/'], ['org.apache.commons', 'https://commons.apache.org/'], ['org.apache.tomcat', 'http://tomcat.apache.org/']];
function Dictionary() {
  this.add = add;
  this.datastore = new Array();
  this.find = find;
}

function add(key, value) {
  this.datastore[key] = value;
}

function find(key) {
  return this.datastore[key];
}

function buildDictionary() {
  var dict = new Dictionary();
  for (i = 0; i < repoinfo.length; i++) {
     dict.add(repoinfo[i][0], repoinfo[i].slice(1, 7));
  }
  return dict;
}

function buildPackageDictionary() {
  var dict = new Dictionary();
  for (i = 0; i < packageinfo.length; i++) {
     dict.add(packageinfo[i][0], packageinfo[i][1]); 
  }
  return dict;
}

function onAnchorClick(event) {
  chrome.tabs.create({
    selected: true,
    url: event.srcElement.href
  });
  return false;
}


function buildContent(key){
  var github = "http://github.com/";
  var dict = buildDictionary();
  var packagedict = buildPackageDictionary(); 
 
  var repo = document.getElementById("repo");
  var repo_link = document.createElement('a');
  repo_link.href = github + key;
  repo_link.style.fontSize = "28px"
  repo_link.style.fontFamily = "Cursive";
  repo_link.style.color = "#00ace6";
  repo_link.appendChild(document.createTextNode(key));
  repo_link.addEventListener('click', onAnchorClick);
  repo.appendChild(repo_link);

  var library1 = document.getElementById("library1");
  var pac_link1 = document.createElement('a');
  pac_link1.href = packagedict.find(dict.find(key)[0]);
  pac_link1.style.fontSize = "26px"
  pac_link1.style.fontFamily = "Palatino Linotype";
  pac_link1.style.color = "#00ace6";
  pac_link1.appendChild(document.createTextNode(dict.find(key)[0]));
  pac_link1.addEventListener('click', onAnchorClick);
  library1.appendChild(pac_link1);

  var repo1 = document.getElementById("repo1");
  var repo1_link = document.createElement('a');
  repo1_link.href = github + dict.find(key)[1];
  repo1_link.style.fontSize = "18px"
  repo1_link.style.fontFamily = "Palatino Linotype";
  repo1_link.style.color = "#00ace6";
  repo1_link.appendChild(document.createTextNode(dict.find(key)[1]));
  repo1_link.addEventListener('click', onAnchorClick);
  repo1.appendChild(repo1_link);

  var library2 = document.getElementById("library2");
  var pac_link2 = document.createElement('a');
  pac_link2.href = packagedict.find(dict.find(key)[2]);
  pac_link2.style.fontSize = "26px"
  pac_link2.style.fontFamily = "Palatino Linotype";
  pac_link2.style.color = "#00ace6";
  pac_link2.appendChild(document.createTextNode(dict.find(key)[2]));
  pac_link2.addEventListener('click', onAnchorClick);
  library2.appendChild(pac_link2);

  var repo2 = document.getElementById("repo2");
  var repo2_link = document.createElement('a');
  repo2_link.href = github + dict.find(key)[3];
  repo2_link.style.fontSize = "18px"
  repo2_link.style.fontFamily = "Palatino Linotype";
  repo2_link.style.color = "#00ace6";
  repo2_link.appendChild(document.createTextNode(dict.find(key)[3]));
  repo2_link.addEventListener('click', onAnchorClick);
  repo2.appendChild(repo2_link);

  var library3 = document.getElementById("library3");
  var pac_link3 = document.createElement('a');
  pac_link3.href = packagedict.find(dict.find(key)[4]);
  pac_link3.style.fontSize = "18px"
  pac_link3.style.fontFamily = "Palatino Linotype";
  pac_link3.style.color = "#00ace6";
  pac_link3.appendChild(document.createTextNode(dict.find(key)[4]));
  pac_link3.addEventListener('click', onAnchorClick);
  library3.appendChild(pac_link3);

  var repo3 = document.getElementById("repo3");
  repo3_link = document.createElement('a');
  repo3_link.href = github + dict.find(key)[5];
  repo3_link.style.fontSize = "14px"
  repo3_link.style.fontFamily = "Palatino Linotype";
  repo3_link.style.color = "#00ace6";
  repo3_link.appendChild(document.createTextNode(dict.find(key)[5]));
  repo3_link.addEventListener('click', onAnchorClick);
  repo3.appendChild(repo3_link);
}

document.addEventListener('DOMContentLoaded', function () {
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    var str = tabs[0].url;
    var res1 = str.split('github.com/')
    var res2 = res1[1].split('/', 2);
    var key = res2[0] + '/' + res2[1];
    buildContent(key);
  });
});
