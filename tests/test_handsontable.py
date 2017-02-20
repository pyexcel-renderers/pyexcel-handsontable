from mock import patch
import pyexcel
from textwrap import dedent
from nose.tools import assert_equal


@patch('pyexcel_handsontable.handsontable._generate_uuid')
def test_sheet_renderring(fake_uuid):
    fake_uuid.return_value = '1'
    s = pyexcel.Sheet([[1]])
    expected = dedent("""
    <html><head>
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/handsontable/0.31.0/handsontable.full.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/handsontable/0.31.0/handsontable.full.min.js"></script>
    </head><body>
    <div id="1"></div>
    
    <script>
    
      var pyexcelElement = document.querySelector("#1");
      var pyexcelElementContainer = pyexcelElement.parentNode;
    
      var mydata = [[1]];
      var defaults = {
        colHeaders: true,
        rowHeaders: true,
        preventOverflow: "hornizontal"
      };
      var myconfig = {};
      var actualconfig = Object.assign({}, defaults, myconfig);
      actualconfig["data"] = mydata;
      new Handsontable(pyexcelElement, actualconfig);
    
    </script>
    </body></html>""").strip('\n')
    assert_equal(s.handsontable, expected)


@patch('pyexcel_handsontable.handsontable._generate_uuid')
def test_sheet_renderring_custom_urls(fake_uuid):
    fake_uuid.return_value = '1'
    s = pyexcel.Sheet([[1]])
    actual = s.get_handsontable(js_url='js', css_url='css')
    expected = dedent("""
    <html><head>
    <link rel="stylesheet" type="text/css" href="css">
    <script src="js"></script>
    </head><body>
    <div id="1"></div>
    
    <script>
    
      var pyexcelElement = document.querySelector("#1");
      var pyexcelElementContainer = pyexcelElement.parentNode;
    
      var mydata = [[1]];
      var defaults = {
        colHeaders: true,
        rowHeaders: true,
        preventOverflow: "hornizontal"
      };
      var myconfig = {};
      var actualconfig = Object.assign({}, defaults, myconfig);
      actualconfig["data"] = mydata;
      new Handsontable(pyexcelElement, actualconfig);
    
    </script>
    </body></html>""").strip('\n')
    assert_equal(actual, expected)


@patch('pyexcel_handsontable.handsontable._generate_uuid')
def test_sheet_renderring_embend(fake_uuid):
    fake_uuid.return_value = '1'
    s = pyexcel.Sheet([[1]])
    actual = s.get_handsontable(embed=True)
    print(actual)
    expected = dedent("""
    <div id="1"></div>
    
    <script>
    
      var pyexcelElement = document.querySelector("#1");
      var pyexcelElementContainer = pyexcelElement.parentNode;
    
      var mydata = [[1]];
      var defaults = {
        colHeaders: true,
        rowHeaders: true,
        preventOverflow: "hornizontal"
      };
      var myconfig = {};
      var actualconfig = Object.assign({}, defaults, myconfig);
      actualconfig["data"] = mydata;
      new Handsontable(pyexcelElement, actualconfig);
    
    </script>
    """)
    assert_equal(actual, expected)