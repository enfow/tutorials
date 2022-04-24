TXT = "Default Message"

format:
	black src/
	isort src/

lint: 
	pytest src/ --pylint

print-text:
	python src/print_input.py --txt ${TXT}


docker-build-on-docker-dir:
	make -C docker docker-build

docker-run-on-docker-dir:
	make -C docker docker-run
