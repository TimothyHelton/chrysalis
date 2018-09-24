PROJECT=chrysalis
MOUNT_DIR=$(shell pwd)
SRC_DIR=/usr/src/chrysalis


include envfile
.PHONY: docs

docker-down:
	docker-compose -f docker/docker-compose.yml down

docker-up:
	docker-compose -f docker/docker-compose.yml up -d

docs: docker-up
	docker container exec $(PROJECT)_python \
		/bin/bash -c "cd docs && make html"
	open http://localhost:8080

psql: docker-up
	docker container exec -it $(PROJECT)_postgres \
		psql -U ${POSTGRES_USER} $(PROJECT)

view-docs: docker-up
	open http://localhost:8080

