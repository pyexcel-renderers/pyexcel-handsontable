from mock import patch
import pyexcel
from textwrap import dedent
from nose.tools import assert_equal


@patch('pyexcel_handsontable.handsontable._generate_uuid')
def test_sheet_renderring(fake_uuid):
    fake_uuid.side_effect = ['1', '2', '3']
    book = pyexcel.Book()
    book += pyexcel.Sheet([[1]])
    book += pyexcel.Sheet([[2]])
    book += pyexcel.Sheet([[3]])
    actual = book.handsontable
    print actual
    expected = dedent("""
    <html><head>
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/handsontable/0.31.0/handsontable.full.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/handsontable/0.31.0/handsontable.full.min.js"></script>
    </head><body>
    <div id="1"></div>
    </body></html>""").strip('\n')
    assert_equal(actual, expected)
