PROJECT=chrysalis
MOUNT_DIR=$(shell pwd)
SRC_DIR=/usr/src/chrysalis
VERSION=$(shell echo $(shell cat $(PROJECT)/__init__.py | \
			grep "^__version__" | \
			cut -d = -f 2))

include envfile
.PHONY: docs

docker-down:
	docker-compose -f docker/docker-compose.yml down

docker-up:
	. envfile
	docker-compose -f docker/docker-compose.yml up -d

docs: docker-up
	docker container exec $(PROJECT)_python \
		/bin/bash -c "pip install -e . && cd docs && make html"
	open http://localhost:8080

docs-init: docker-up
	rm -rf docs/*
	docker container exec $(PROJECT)_python \
		/bin/bash -c \
			"cd docs \
			&& sphinx-quickstart -q \
			-p $(PROJECT) \
			-a EnterAuthorName \
			-v $(VERSION) \
			--ext-autodoc \
			--ext-viewcode \
			--makefile \
			--no-batchfile"
	git fetch
	git checkout origin/master -- docs/

pgadmin: docker-up
	open http://localhost:5000

psql: docker-up
	docker container exec -it $(PROJECT)_postgres \
		psql -U ${POSTGRES_USER} $(PROJECT)

view-docs: docker-up
	open http://localhost:8080
