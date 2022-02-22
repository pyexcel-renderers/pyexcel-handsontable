import codecs

import pyexcel
from mytestwrapper import DEFAULT_CONFIG, MyBaseCase, MyTestCase


class TestStyle(MyBaseCase):
    def test_book_renderring_style(self):
        self.fake_uuid.side_effect = ["1", "2", "3", "4"]
        styles = {"styled sheet": {"colWidths": [100, 100]}}
        expected = 'var customStyle = {"colWidths": [100, 100]}'
        book = pyexcel.Book()
        book += pyexcel.Sheet([[1]])
        book += pyexcel.Sheet([[2]], name="styled sheet")
        book += pyexcel.Sheet([[3]])
        book.save_as(self._test_file, styles=styles)
        with codecs.open(self._test_file, "r", encoding="utf-8") as f:
            content = f.read()
            assert expected in content


class TestBook(MyTestCase):
    def test_book_renderring(self):
        self.fake_uuid.side_effect = ["1", "2", "3", "4"]
        self.dump_dict.return_value = DEFAULT_CONFIG
        book = pyexcel.Book()
        book += pyexcel.Sheet([[1]])
        book += pyexcel.Sheet([[2]])
        book += pyexcel.Sheet([[3]])
        book.save_as(self._test_file)
        self.compareTwoFiles(
            self._test_file, "tests/fixtures/book.handsontable.html"
        )

    def test_book_in_jupyter_renderring(self):
        self.fake_uuid.side_effect = ["1", "2", "3", "4"]
        self.dump_dict.return_value = DEFAULT_CONFIG
        book = pyexcel.Book()
        book += pyexcel.Sheet([[1]])
        book += pyexcel.Sheet([[2]], name="pyexcel sheet_1")
        book += pyexcel.Sheet([[3]], name="pyexcel sheet_2")
        actual = book.handsontable
        test_fixture = "tests/fixtures/book.jupyter_notebook"
        with codecs.open(test_fixture, "r", encoding="utf-8") as f:
            expected = f.read()
            self.customAssertMultiLineEqual(expected, actual)
