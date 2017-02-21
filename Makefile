all: test

test:
	bash test.sh

document:
	bash document.sh

demo:
	python demo.py
	mv abc.handsontable abc.handsontable.html
css:
	python -mscss <styles/style.scss >.moban.d/handsontable/style.css.jj2
