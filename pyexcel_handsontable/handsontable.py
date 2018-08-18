"""
    pyexcel_handsontable.handsontable
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Transform pyexcel sheet into a handsontable html

    :copyright: (c) 2016-2017 by Onni Software Ltd.
    :license: New BSD License, see LICENSE for further details
"""
import os
import codecs
import uuid
import json
from functools import partial
from datetime import date, datetime

from pyexcel.renderer import Renderer
from jinja2 import Environment, FileSystemLoader


HOST = "https://cdnjs.cloudflare.com/ajax/libs/handsontable/0.31.0/"
JS_URL = HOST + "handsontable.full.min.js"
CSS_URL = HOST + "handsontable.full.min.css"
DEFAULTS = dict(
    colHeaders=True,
    rowHeaders=True,
    preventOverflow="hornizontal",
    readOnly=True,
    columnSorting=True
)


class HandsonTable(Renderer):
    def __init__(self, file_type):
        Renderer.__init__(self, file_type)
        loader = FileSystemLoader(_get_resource_dir('templates'))
        self._env = Environment(loader=loader,
                                keep_trailing_newline=True,
                                trim_blocks=True,
                                lstrip_blocks=True)

    def render_book(self, book, embed=False,
                    css_url=CSS_URL, js_url=JS_URL,
                    **keywords):
        """
        Render the book data in handsontable
        """
        book_data = self._parse_book(book)
        book_data['css_url'] = css_url
        book_data['js_url'] = js_url
        if embed:
            template = self._env.get_template('embed.html')
        else:
            template = self._env.get_template('full.html')
        self._stream.write(template.render(**book_data))

    def render_sheet(self, sheet, embed=False, **keywords):
        book = [sheet]
        self.render_book(book, embed=embed, **keywords)

    def _parse_book(self, book, styles=None, **keywords):
        if styles is None:
            styles = {}
        config = {}
        config.update(DEFAULTS)
        config.update(keywords)
        book_uuid = _generate_uuid() + '-book'
        book_data = {
            'width': keywords.get('width', None),
            'height': keywords.get('height', None),
            'sheets': [],
            'uid': book_uuid,
            'config': _dump_dict(config)
        }
        uids = []
        for sheet in book:
            sheet_uid = _generate_uuid()
            handson_sheet = {
                'uid': sheet_uid,
                'name': sheet.name,
                'content': _dumps(sheet.array)
            }
            if sheet.name in styles:
                sheet_style = styles.get(sheet.name)
                if 'column_widths' in sheet_style:
                    handson_sheet['colWidths'] = _dump_dict(
                        sheet_style['column_widths'])
            if len(sheet.colnames) > 0:
                handson_sheet['colHeaders'] = _dump_dict(sheet.colnames)
            book_data['sheets'].append(handson_sheet)
            uids.append(sheet_uid)
        book_data['active'] = uids[0]
        return book_data


class HandsonTableInJupyter(HandsonTable):
    def get_io(self):
        io = HandsonTable.get_io(self)
        setattr(io,
                '_repr_html_',
                partial(lambda s: s.getvalue(), io))
        return io

    def render_book_to_stream(self, file_stream, book,
                              write_title=True, caption="",
                              display_length=None,
                              **keywords):
        self.set_write_title(write_title)
        self.set_output_stream(file_stream)
        book_data = self._parse_book(book, **keywords)
        __css_file__ = os.path.join(_get_resource_dir('templates'),
                                    'pyexcel-handsontable',
                                    'handsontable.min.css')
        with codecs.open(__css_file__, 'r', 'utf-8') as f:
            book_data['handsontable_css'] = f.read()
            template = self._env.get_template('notebook.html')
        self._stream.write(template.render(**book_data))

    def render_sheet_to_stream(self, file_stream, sheet,
                               **keywords):
        self.render_book_to_stream(file_stream, [sheet], **keywords)

    def render_book(self, book, **keywords):
        """
        Render the book data in handsontable
        """
        raise NotImplementedError()

    def render_sheet(self, sheet,  **keywords):
        raise NotImplementedError()


def _generate_uuid():
    return 'pyexcel-' + uuid.uuid4().hex


def _get_resource_dir(folder):
    current_path = os.path.dirname(__file__)
    resource_path = os.path.join(current_path, folder)
    return resource_path


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            date_string = obj.strftime('%Y-%m-%d')
            return date_string
        if isinstance(obj, datetime):
            datetime_string = obj.strftime("%Y-%m-%d %H:%M:%S")
            return datetime_string
        return json.JSONEncoder.default(self, obj)


def _dumps(data):
    return json.dumps(data, cls=DateTimeEncoder)


def _dump_dict(aconfig):
    """
    This function is made for testing purpose
    """
    return _dumps(aconfig)
