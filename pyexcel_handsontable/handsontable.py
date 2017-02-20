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
div#hot {
width: 100%;
height:100%;
}
body {font-family: "Lato", sans-serif;}

ul.tab {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: #f1f1f1;
}

/* Float the list items side by side */
ul.tab li {float: left;}

/* Style the links inside the list items */
ul.tab li a {
    display: inline-block;
    color: black;
    text-align: center;
    padding: 16px 14px;
    text-decoration: none;
    transition: 0.3s;
    font-size: 17px;
}

/* Change background color of links on hover */
ul.tab li a:hover {
    background-color: #ddd;
}

/* Create an active/current tablink class */
ul.tab li a:focus, .active {
    background-color: #ccc;
}

/* Style the tab content */
.tabcontent {
    display: block;
}
</style>
"""

BOOK_SCRIPTS = """
<script>
function openTab(evt, tabId) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabId).style.display = "block";
    evt.currentTarget.className += " active";
}
function activateFirst() {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 1; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
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
        for sheet in book:
            uid = _generate_uuid()
            tabs += '<li><a href="javascript:void(0)" class="tablinks" onClick="openTab(event, \'{1}-sheet\')">{0}</a></li>\n'.format(sheet.name, uid)
            divs += """
            <div id="{1}-sheet" class="tabcontent">
              <div id="{1}"></div>
            </div>
            """.format(sheet.name, uid)
            scripts += BOOK_SHEET % (uid, json.dumps(sheet.array))
        tabs += '</ul>\n'
        scripts += "activateFirst();"
        scripts += '</script>\n'
        table = tabs + divs + BOOK_SCRIPTS + scripts
        self._stream.write(table)
        if not embed:
            self._stream.write('</body></html>')


def _generate_uuid():
    return 'pyexcel-' + uuid.uuid4().hex