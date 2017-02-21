import uuid
import json

from pyexcel.renderers.factory import Renderer
import pyexcel_handsontable.htmlwidgets as html


class HandsonTable(Renderer):
    file_types = ('handsontable',)

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

    def render_sheet(self, sheet, embed=False, **keywords):
        book = [sheet]
        self.render_book(book, embed=embed, **keywords)

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
        book_uuid = 'book-' + _generate_uuid()
        if not embed:
            self._render_html_header(**keywords)
        tabs = '<ul class="tab">\n'
        divs = ''
        scripts = '<script>\n'
        common = html.BOOK_COMMON % (json.dumps(keywords))
        scripts += common
        uids = []
        for sheet in book:
            uid = _generate_uuid()
            tabs += html.BOOK_TAB.format(sheet.name, uid, book_uuid)
            divs += html.BOOK_DIV.format(book_uuid, uid)
            scripts += html.BOOK_SHEET % (uid, json.dumps(sheet.array))
            uids.append(uid)
        tabs += '</ul>\n'
        scripts += "activateFirst('%s', '%s-sheet');\n" % (book_uuid, uids[0])
        scripts += '</script>\n'
        table = tabs + divs + html.BOOK_SCRIPTS + scripts
        self._stream.write(table)
        if not embed:
            self._stream.write('</body></html>')


def _generate_uuid():
    return 'pyexcel-' + uuid.uuid4().hex