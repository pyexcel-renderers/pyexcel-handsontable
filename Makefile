all: test

test:
	bash test.sh

document:
	bash document.sh

css:
	python -mscss <styles/style.scss >.moban.d/handsontable/style.css.jj2
	cp .moban.d/handsontable/style.css.jj2 styles/style.css
	python -mscss <styles/rtd_style.scss >styles/rtd_style.css
