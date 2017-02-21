import pyexcel
b=pyexcel.Book()
b+=pyexcel.Sheet([[1]])
b+=pyexcel.Sheet([[2]])
b.save_as('abc.handsontable', js_url='handsontable.full.min.js', css_url='handsontable.full.min.css')