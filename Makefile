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
	# NGINX Container
	docker image build \
		--tag nginx_$(PROJECT) \
		-f docker/nginx-Dockerfile \
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
	docker container rm -f nginx_$(PROJECT) || true
	docker container run -d \
		-p 80:80 \
		-v $(MOUNT_DIR)/docs/_build/html:/usr/share/nginx/html:ro \
		--name nginx_$(PROJECT) \
		nginx_$(PROJECT)

