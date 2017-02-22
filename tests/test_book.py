from mock import patch
import pyexcel
from unittest import TestCase


class TestBook(TestCase):
    def setUp(self):
        self.maxDiff = None

    @patch('pyexcel_handsontable.handsontable._generate_uuid')
    def test_book_renderring(self, fake_uuid):
        fake_uuid.side_effect = ['1', '2', '3', '4']
        book = pyexcel.Book()
        book += pyexcel.Sheet([[1]])
        book += pyexcel.Sheet([[2]])
        book += pyexcel.Sheet([[3]])
        actual = book.handsontable
        with open('tests/fixtures/book.handsontable.html', 'r') as f:
            expected = f.read().strip('\n')
            self.assertMultiLineEqual(actual, expected)
