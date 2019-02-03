.PHONY: fmt update upgrade


SRCDIR = $(shell pwd)
CODEDIR = $(SRCDIR)/autofactory

fmt: _sort

update:
	CUSTOM_COMPILE_COMMAND="make update" pip-compile --generate-hashes --upgrade --output-file $(SRCDIR)/requirements-dev.out  $(SRCDIR)/requirements-dev.in

upgrade:
	pip-sync $(SRCDIR)/requirements-dev.out

test:
	python -m unittest

test-tox:
	tox

_sort:
	autoflake -r -i --remove-all-unused-imports $(CODEDIR)/
	isort -rc $(CODEDIR)/
