import pyexcel

book = pyexcel.get_book(file_name="census.xls", skip_hidden_sheets=False)
book.save_as('demo.handsontable',
             js_url='handsontable.full.min.js',
             css_url='handsontable.full.min.css')
