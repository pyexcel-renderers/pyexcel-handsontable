# flake8: noqa
from .css import BOOK_STYLE

HOST = "https://cdnjs.cloudflare.com/ajax/libs/handsontable/0.31.0/"
JS_URL = HOST + "handsontable.full.min.js"
CSS_URL = HOST + "handsontable.full.min.css"


HANDSON_FILES = """
<!-- HANDSON_FILES -->
<link rel="stylesheet" type="text/css" href="%s">
<script src="%s"></script>
"""

BOOK_DIV = """
<!-- BOOK_DIV -->
<div id="{1}-sheet" class="tabcontent {0}">
  <div id="{1}"></div>
</div>
"""

BOOK_TAB = """
<!-- BOOK_TAB -->
<li id='{1}-sheet-li' class="{2}-li">
<a href="javascript:void(0)" onClick="openTab(event, \'{2}\', \'{1}-sheet\')">{0}</a>
</li>
"""

BOOK_SCRIPTS = """
<!-- BOOK_SCRIPTS -->
<script>
function openTab(evt, bookId, tabId) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName(bookId);
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName(bookId+"-li");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabId).style.display = "block";
    document.getElementById(tabId+"-li").className += " active";
}
function activateFirst(bookId, firstTab) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName(bookId);
    for (i = 1; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    document.getElementById(firstTab+'-li').className += " active";
}
</script>
"""

BOOK_COMMON = """
// BOOK_COMMON
  var config = %s;
"""

BOOK_SHEET = """
// BOOK_SHEET
  var pyexcelElement = document.querySelector("#%s");
  var pyexcelElementContainer = pyexcelElement.parentNode;

  var mydata = %s;
  config["data"] = mydata;
  new Handsontable(pyexcelElement, config);
"""