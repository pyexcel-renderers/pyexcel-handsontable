import uuid
import json

from pyexcel.renderer import Renderer
import pyexcel_handsontable.htmlwidgets as html


DEFAULTS = dict(
    colHeaders=True,
    rowHeaders=True,
    preventOverflow="hornizontal",
    readOnly=True
)


class HandsonTable(Renderer):
    file_types = ('handsontable.html',)

    def render_book(self, book, embed=False, **keywords):
        """
        Render the book data in handsontable

        <html><header>
        header
        </header><body>
        tabs
        divs
        common
        scripts
        </body>
        """
        book_uuid = _generate_uuid() + '-book'
        if not embed:
            self._render_html_header(**keywords)
        width = keywords.get('width', None)
        if width:
            tabs = '<ul class="tab" style="width:%spx">' % width
        else:
            tabs = '<ul class="tab">\n'
        divs = ''
        scripts = '<script>\n'
        config = {}
        config.update(DEFAULTS)
        config.update(keywords)

        common = html.BOOK_COMMON % (_dump_dict(config))
        scripts += common
        uids = []
        for sheet in book:
            sheet_uid = _generate_uuid()
            tabs += html.BOOK_TAB.format(sheet.name, sheet_uid, book_uuid)
            divs += html.BOOK_DIV.format(book_uuid, sheet_uid)
            scripts += html.BOOK_SHEET % (sheet_uid, json.dumps(sheet.array))
            uids.append(sheet_uid)
        tabs += '</ul>\n'
        scripts += "  activateFirst('%s', '%s-sheet');\n" % (book_uuid,
                                                             uids[0])
        scripts += '</script>\n'
        table = tabs + divs + html.BOOK_SCRIPTS + scripts
        self._stream.write(table)
        if not embed:
            self._stream.write('</body></html>')

    def render_sheet(self, sheet, embed=False, **keywords):
        book = [sheet]
        self.render_book(book, embed=embed, **keywords)

    def _render_html_header(self, **keywords):
        self._stream.write('<html><head>')
        if 'css_url' in keywords:
            css = keywords.pop('css_url')
        else:
            css = html.CSS_URL
        if 'js_url' in keywords:
            js = keywords.pop('js_url')
        else:
            js = html.JS_URL
        self._stream.write(html.HANDSON_FILES % (css, js))
        self._stream.write(html.BOOK_STYLE)
        self._stream.write('</head><body>')


def _generate_uuid():
    return 'pyexcel-' + uuid.uuid4().hex


def _dump_dict(adict):
    """
    This function is made for testing purpose
    """
    return json.dumps(adict)
