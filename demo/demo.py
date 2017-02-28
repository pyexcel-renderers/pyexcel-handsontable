import pyexcel
# The census file has three hidden sheets
book = pyexcel.get_book(file_name="census.xls", skip_hidden_sheets=False)
# Please note that the file name has to be *.handsontable.html
book.save_as('demo.handsontable.html',
             readOnly=False,
             js_url='handsontable.full.min.js',
             css_url='handsontable.full.min.css')
