PROJECT=chrysalis
MOUNT_DIR=$(shell pwd)
SRC_DIR=/usr/src/chrysalis


.PHONY: docker docs

docker-down:
	cd docker && docker-compose down

docker-up:
	cd docker && docker-compose up -d

docs: docker-up
	docker container exec $(PROJECT)_python /bin/bash -c "cd docs && make html"
	open http://localhost:8080

view-docs:
	open http://localhost:8080

