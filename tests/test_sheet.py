import codecs
from textwrap import dedent

import pyexcel
from mytestwrapper import DEFAULT_CONFIG, MyTestCase


class TestSheet(MyTestCase):
    def test_rendering(self):
        self.fake_uuid.return_value = "1"
        self.dump_dict.return_value = DEFAULT_CONFIG
        s = pyexcel.Sheet([[1]])
        s.save_as(self._test_file)
        with codecs.open(self._test_file, "r", encoding="utf-8") as f:
            content = f.read()
            assert "<!-- HANDSON_FILES -->" in content

    def test_rendering_custom_urls(self):
        self.fake_uuid.return_value = "1"
        self.dump_dict.return_value = DEFAULT_CONFIG
        s = pyexcel.Sheet([[1]])
        actual = s.get_handsontable_html(js_url="js", css_url="css")
        expected = dedent(
            """
        <link rel="stylesheet" type="text/css" href="css">
        <script src="js"></script>
        """
        )
        assert expected in actual

    def test_rendering_embed(self):
        self.fake_uuid.return_value = "1"
        self.dump_dict.return_value = DEFAULT_CONFIG
        s = pyexcel.Sheet([[1]])
        actual = s.get_handsontable_html(embed=True)
        assert "<!-- HANDSON_FILES -->" not in actual

    def test_jupyter_rendering(self):
        self.fake_uuid.return_value = "1"
        self.dump_dict.return_value = DEFAULT_CONFIG
        s = pyexcel.Sheet([[1]])
        actual = s.handsontable
        assert (
            "/nbextensions/pyexcel-handsontable/handsontable.min" in actual
        )  # flake8: noqa
