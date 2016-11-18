function buildContent(){

  var repo_name = document.getElementById("repo_name");
  repo_name.appendChild(document.createTextNode("1"));

  var repo_link = document.getElementById("repo_link");
  repo_link.appendChild(document.createTextNode("2"));

  var library1 = document.getElementById("library1");
  library1.appendChild(document.createTextNode("3"));

  var repo1 = document.getElementById("repo1");
  repo1.appendChild(document.createTextNode("4"));  

  var library2 = document.getElementById("library2");
  library2.appendChild(document.createTextNode("5"));

  var repo2 = document.getElementById("repo2");
  repo2.appendChild(document.createTextNode("6"));

  var library3 = document.getElementById("library3");
  library3.appendChild(document.createTextNode("7"));

  var repo3 = document.getElementById("repo3");
  repo3.appendChild(document.createTextNode("8"));
}

document.addEventListener('DOMContentLoaded', function () {
  buildContent();
});
