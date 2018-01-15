import codecs
import pyexcel
from textwrap import dedent
from mytestwrapper import MyTestCase, DEFAULT_CONFIG


class TestSheet(MyTestCase):

    def test_rendering(self):
        self.fake_uuid.return_value = '1'
        self.dump_dict.return_value = DEFAULT_CONFIG
        s = pyexcel.Sheet([[1]])
        s.save_as(self._test_file)
        self.compareTwoFiles(
            self._test_file,
            'tests/fixtures/sheet_rendering.html')

    def test_rendering_custom_urls(self):
        self.fake_uuid.return_value = '1'
        self.dump_dict.return_value = DEFAULT_CONFIG
        s = pyexcel.Sheet([[1]])
        actual = s.get_handsontable_html(js_url='js', css_url='css')
        expected = dedent("""
        <link rel="stylesheet" type="text/css" href="css">
        <script src="js"></script>
        """)
        print(actual)
        assert expected in actual

    def test_rendering_embed(self):
        self.fake_uuid.return_value = '1'
        self.dump_dict.return_value = DEFAULT_CONFIG
        s = pyexcel.Sheet([[1]])
        actual = s.get_handsontable_html(embed=True)
        with open('tests/fixtures/sheet_rendering_embed.html', 'r') as f:
            expected = f.read()
            self.customAssertMultiLineEqual(expected, actual)

    def test_jupyter_rendering(self):
        self.fake_uuid.return_value = '1'
        self.dump_dict.return_value = DEFAULT_CONFIG
        s = pyexcel.Sheet([[1]])
        actual = s.handsontable
        test_file = 'tests/fixtures/sheet.jupyter_notebook'
        with codecs.open(test_file, 'r', encoding='utf-8') as f:
            expected = f.read()
            self.customAssertMultiLineEqual(expected, actual)
