from mock import patch
import pyexcel
from textwrap import dedent
from mytestwrapper import MyTestCase, DEFAULT_CONFIG


class TestSheet(MyTestCase):
    def setUp(self):
        self.maxDiff = None

    @patch('pyexcel_handsontable.handsontable._generate_uuid')
    @patch('pyexcel_handsontable.handsontable._dump_dict')
    def test_rendering(self, dump_dict, fake_uuid):
        fake_uuid.return_value = '1'
        dump_dict.return_value = DEFAULT_CONFIG
        s = pyexcel.Sheet([[1]])
        actual = s.handsontable_html
        with open('tests/fixtures/sheet_rendering.html', 'r') as f:
            expected = f.read()
            self.customAssertMultiLineEqual(expected, actual)

    @patch('pyexcel_handsontable.handsontable._generate_uuid')
    @patch('pyexcel_handsontable.handsontable._dump_dict')
    def test_rendering_custom_urls(self, dump_dict, fake_uuid):
        fake_uuid.return_value = '1'
        dump_dict.return_value = DEFAULT_CONFIG
        s = pyexcel.Sheet([[1]])
        actual = s.get_handsontable_html(js_url='js', css_url='css')
        expected = dedent("""
        <link rel="stylesheet" type="text/css" href="css">
        <script src="js"></script>
        """)
        assert expected in actual

    @patch('pyexcel_handsontable.handsontable._generate_uuid')
    @patch('pyexcel_handsontable.handsontable._dump_dict')
    def test_rendering_embed(self, dump_dict, fake_uuid):
        fake_uuid.return_value = '1'
        dump_dict.return_value = DEFAULT_CONFIG
        s = pyexcel.Sheet([[1]])
        actual = s.get_handsontable_html(embed=True)
        with open('tests/fixtures/sheet_rendering_embed.html', 'r') as f:
            expected = f.read()
            self.customAssertMultiLineEqual(expected, actual)
