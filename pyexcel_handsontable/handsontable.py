import uuid
import json

from pyexcel.renderers.factory import Renderer


HOST = "https://cdnjs.cloudflare.com/ajax/libs/handsontable/0.31.0/"
JS_URL = HOST + "handsontable.full.min.js"
CSS_URL = HOST + "handsontable.full.min.css"


HANDSON_FILES = """
<link rel="stylesheet" type="text/css" href="%s">
<script src="%s"></script>
"""


SHEET = """
<div id="%s"></div>

<script>

  var pyexcelElement = document.querySelector("#%s");
  var pyexcelElementContainer = pyexcelElement.parentNode;

  var mydata = %s;
  var defaults = {
    colHeaders: true,
    rowHeaders: true,
    preventOverflow: "hornizontal"
  };
  var myconfig = %s;
  var actualconfig = Object.assign({}, defaults, myconfig);
  actualconfig["data"] = mydata;
  new Handsontable(pyexcelElement, actualconfig);

</script>
"""

BOOK_STYLE = """
<style>
body {font-family: "Lato", sans-serif;margin: 0px;}

  .tab {
      text-align: center;
      list-style: none;
      padding: 0 0 0 10px;
      line-height: 24px;
      height: 26px;
      overflow: hidden;
      font-size: 12px;
      font-family: verdana;
      position: relative;
      margin:0px;
  }
  .tab li {
      float:left;
      height: 24px;
      border: 1px solid #AAA;
      background: #D1D1D1;
      background: -o-linear-gradient(top, #ECECEC 50%, #D1D1D1 100%);
      background: -ms-linear-gradient(top, #ECECEC 50%, #D1D1D1 100%);
      background: -moz-linear-gradient(top, #ECECEC 50%, #D1D1D1 100%);
      background: -webkit-linear-gradient(top, #ECECEC 50%, #D1D1D1 100%);
      background: linear-gradient(top, #ECECEC 50%, #D1D1D1 100%);
      display: inline-block;
      position: relative;
      z-index: 0;
      border-top-left-radius: 6px;
      border-top-right-radius: 6px;
      box-shadow: 0 3px 3px rgba(0, 0, 0, 0.4), inset 0 1px 0 #FFF;
      text-shadow: 0 1px #FFF;
      margin: 0 -5px;
      padding: 0 20px;
  }
  .tab a {
  	  color: #555;
  	  text-decoration: none;
  }
  .tab li.active {
      background: #FFF;
      color: #333;
      z-index: 2;
  }
  .tab:before {
      position: absolute;
      content: " ";
      width: 100%;
      bottom: 0;
      left: 0;
      border-bottom: 1px solid #AAA;
      z-index: 1;
  }
  .tab li:before {
      left: -6px;
      border-width: 0 1px 1px 0;
      box-shadow: 2px 2px 0 #D1D1D1;
  }
  .tab li:after {
      right: -6px;
      border-width: 0 0 1px 1px;
      box-shadow: -2px 2px 0 #D1D1D1;
  }
 .tabcontent {
      margin-top: -1px;
 }

</style>
"""

BOOK_DIV = """
<div id="{1}-sheet" class="tabcontent {0}">
  <div id="{1}"></div>
</div>
"""

BOOK_TAB = """
<li id='{1}-sheet-li' class="tabli">
<a href="javascript:void(0)" onClick="openTab(event, \'{2}\', \'{1}-sheet\')">{0}</a>
</li>
"""

BOOK_SCRIPTS = """
<script>
function openTab(evt, bookId, tabId) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName(bookId);
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tabli");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabId).style.display = "block";
    //evt.currentTarget.className += " active";
    tablinks = document.getElementById(tabId+"-li");
    tablinks.className += " active";
}
function activateFirst(bookId, firstTab) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName(bookId);
    for (i = 1; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementById(firstTab+'-li');
    tablinks.className += " active";
}
</script>
"""

BOOK_COMMON = """
  var defaults = {
    colHeaders: true,
    rowHeaders: true,
    preventOverflow: "hornizontal"
  };
  var myconfig = %s;
"""

BOOK_SHEET = """
  var pyexcelElement = document.querySelector("#%s");
  var pyexcelElementContainer = pyexcelElement.parentNode;

  var mydata = %s;
  var actualconfig = Object.assign({}, defaults, myconfig);
  actualconfig["data"] = mydata;
  new Handsontable(pyexcelElement, actualconfig);
"""


class HandsonTable(Renderer):
    file_types = ('handsontable',)

    def render_sheet(self, sheet, embed=False, **keywords):
        uid = _generate_uuid()
        if not embed:
            self._stream.write('<html><head>')
            if 'css_url' in keywords:
                css = keywords.pop('css_url')
            else:
                css = CSS_URL
            if 'js_url' in keywords:
                js = keywords.pop('js_url')
            else:
                js = JS_URL
            self._stream.write(HANDSON_FILES % (css, js))
            self._stream.write('</head><body>')
        table = SHEET % (uid, uid,
                         json.dumps(sheet.array),
                         json.dumps(keywords))
        self._stream.write(table)
        if not embed:
            self._stream.write('</body></html>')

    def render_book(self, book, embed=False, **keywords):
        book_uuid = 'book-' + _generate_uuid()
        if not embed:
            self._stream.write('<html><head>')
            if 'css_url' in keywords:
                css = keywords.pop('css_url')
            else:
                css = CSS_URL
            if 'js_url' in keywords:
                js = keywords.pop('js_url')
            else:
                js = JS_URL
            self._stream.write(HANDSON_FILES % (css, js))
            self._stream.write(BOOK_STYLE)
            self._stream.write('</head><body>')
        tabs = '<ul class="tab">\n'
        divs = ''
        scripts = '<script>\n'
        common = BOOK_COMMON % (json.dumps(keywords))
        scripts += common
        uids = []
        for sheet in book:
            uid = _generate_uuid()
            tabs += BOOK_TAB.format(sheet.name, uid, book_uuid)
            divs += BOOK_DIV.format(book_uuid, uid)
            scripts += BOOK_SHEET % (uid, json.dumps(sheet.array))
            uids.append(uid)
        tabs += '</ul>\n'
        scripts += "activateFirst('%s', '%s-sheet');\n" % (book_uuid, uids[0])
        scripts += '</script>\n'
        table = tabs + divs + BOOK_SCRIPTS + scripts
        self._stream.write(table)
        if not embed:
            self._stream.write('</body></html>')


def _generate_uuid():
    return 'pyexcel-' + uuid.uuid4().hex