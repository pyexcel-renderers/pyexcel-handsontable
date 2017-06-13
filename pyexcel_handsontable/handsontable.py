import os
import uuid
import json
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
    readOnly=True
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
        config = {}
        config.update(DEFAULTS)
        config.update(keywords)
        book_uuid = _generate_uuid() + '-book'
        book_data = {
            'width': keywords.get('width', None),
            'sheets': [],
            'uid': book_uuid,
            'css_url': css_url,
            'js_url': js_url,
            'config': _dump_dict(config)
        }
        uids = []
        for sheet in book:
            sheet_uid = _generate_uuid()
            sheet = {
                'uid': sheet_uid,
                'name': sheet.name,
                'content': _dumps(sheet.array)
            }
            book_data['sheets'].append(sheet)
            uids.append(sheet_uid)
        book_data['active'] = uids[0]
        if embed:
            template = self._env.get_template('embed.html')
        else:
            template = self._env.get_template('full.html')
        self._stream.write(template.render(**book_data))

    def render_sheet(self, sheet, embed=False, **keywords):
        book = [sheet]
        self.render_book(book, embed=embed, **keywords)


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
