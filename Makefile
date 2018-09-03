PROJECT=chrysalis
MOUNT_DIR=$(shell pwd)
SRC_DIR=/usr/src/chrysalis


.PHONY: docker docs

docker:
	# Python Container
	docker image build \
		--tag python_$(PROJECT) \
		-f docker/python-Dockerfile \
		--squash .
	# Postgres Container
	# TODO create postgres-Dockerfile
	#docker image build \
		#--tag postgres_$(PROJECT) \
		#-f docker/postgres-Dockerfile \
		#--squash .
	docker system prune -f

docs:
	docker container run \
		-it --rm \
		-v $(MOUNT_DIR):/usr/src/$(PROJECT) \
		-w /usr/src/$(PROJECT)/docs \
		python_$(PROJECT) make html
