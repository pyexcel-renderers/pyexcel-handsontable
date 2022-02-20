isort $(find pyexcel_handsontable -name "*.py"|xargs echo) $(find tests -name "*.py"|xargs echo)
black -l 79 pyexcel_handsontable
black -l 79 tests
