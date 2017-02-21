all: test

test:
	bash test.sh

document:
	bash document.sh

css:
	python -mscss <styles/style.scss >.moban.d/handsontable/style.css.jj2
