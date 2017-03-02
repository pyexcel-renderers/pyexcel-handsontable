from mock import patch
import pyexcel
from mytestwrapper import MyTestCase, DEFAULT_CONFIG


class TestBook(MyTestCase):
    def setUp(self):
        self.maxDiff = None

    @patch('pyexcel_handsontable.handsontable._generate_uuid')
    @patch('pyexcel_handsontable.handsontable._dump_dict')
    def test_book_renderring(self, dump_dict, fake_uuid):
        fake_uuid.side_effect = ['1', '2', '3', '4']
        dump_dict.return_value = DEFAULT_CONFIG
        book = pyexcel.Book()
        book += pyexcel.Sheet([[1]])
        book += pyexcel.Sheet([[2]])
        book += pyexcel.Sheet([[3]])
        actual = book.handsontable_html
        with open('tests/fixtures/book.handsontable.html', 'r') as f:
            expected = f.read().strip('\n')
            self.customAssertMultiLineEqual(expected, actual)
