from mock import patch
import pyexcel
from textwrap import dedent
from nose.tools import assert_equal


@patch('pyexcel_handsontable.handsontable._generate_uuid')
def test_sheet_rendering(fake_uuid):
    fake_uuid.return_value = '1'
    s = pyexcel.Sheet([[1]])
    actual = s.handsontable
    with open('tests/fixtures/sheet_rendering.html', 'r') as f:
        expected = f.read()
        assert_equal(actual, expected)


@patch('pyexcel_handsontable.handsontable._generate_uuid')
def test_sheet_rendering_custom_urls(fake_uuid):
    fake_uuid.return_value = '1'
    s = pyexcel.Sheet([[1]])
    actual = s.get_handsontable(js_url='js', css_url='css')
    with open('tests/fixtures/sheet_rendering_custom_urls.html', 'r') as f:
        expected = f.read()
        assert_equal(actual, expected)


@patch('pyexcel_handsontable.handsontable._generate_uuid')
def test_sheet_rendering_embed(fake_uuid):
    fake_uuid.return_value = '1'
    s = pyexcel.Sheet([[1]])
    actual = s.get_handsontable(embed=True)
    with open('tests/fixtures/sheet_rendering_embed.html', 'r') as f:
        expected = f.read()
        assert_equal(actual, expected)