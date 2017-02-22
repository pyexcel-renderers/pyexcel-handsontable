from mock import patch
import pyexcel
from unittest import TestCase
from textwrap import dedent


class TestSheet(TestCase):
    def setUp(self):
        self.maxDiff = None

    @patch('pyexcel_handsontable.handsontable._generate_uuid')
    def test_rendering(self, fake_uuid):
        fake_uuid.return_value = '1'
        s = pyexcel.Sheet([[1]])
        actual = s.handsontable
        with open('tests/fixtures/sheet_rendering.html', 'r') as f:
            expected = f.read().strip('\n')
            self.assertMultiLineEqual(actual, expected)

    @patch('pyexcel_handsontable.handsontable._generate_uuid')
    def test_rendering_custom_urls(self, fake_uuid):
        fake_uuid.return_value = '1'
        s = pyexcel.Sheet([[1]])
        actual = s.get_handsontable(js_url='js', css_url='css')
        expected = dedent("""
        <link rel="stylesheet" type="text/css" href="css">
        <script src="js"></script>
        """)
        assert expected in actual

    @patch('pyexcel_handsontable.handsontable._generate_uuid')
    def test_rendering_embed(self, fake_uuid):
        fake_uuid.return_value = '1'
        s = pyexcel.Sheet([[1]])
        actual = s.get_handsontable(embed=True)
        with open('tests/fixtures/sheet_rendering_embed.html', 'r') as f:
            expected = f.read()
            self.assertMultiLineEqual(actual, expected)
