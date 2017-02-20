import os
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
    with open('tests/fixtures/book.handsontable.html', 'r') as f:
        expected = f.read()
    assert_equal(actual, expected)
