install:
	poetry install
gendiff:
	poetry run gendiff -h
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install dist/*.whl --force-reinstall
lint:
	poetry run flake8 gendiff
reinstall:
	rm -r dist
	poetry build
	python3 -m pip install dist/*.whl --force-reinstall
asci:
	clear
	asciinema rec
push:
	git push -u origin main
test:
	poetry run pytest
test-coverage:
	coverage run -m pytest
	coverage report -m