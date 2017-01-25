
.PHONY: install run


install:
	virtualenv-3.5 .
	bin/pip install -r requirements.txt

run:
	bin/molotov -cxv -d 1 loadtest.py
