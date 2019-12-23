FROM python:3.6

WORKDIR /usr/src/chrysalis

COPY . .

RUN cd /opt \
	&& apt-get update \
	&& apt-get install -y \
		protobuf-compiler \
	&& rm -rf /var/lib/apt/lists/* \
	&& git clone \
		--branch master \
		--single-branch \
		--depth 1 \
		https://github.com/tensorflow/models.git \
	&& cd /opt/models/research \
	&& protoc object_detection/protos/*.proto --python_out=. \
	&& cd /usr/src/chrysalis \
	&& pip install --upgrade pip \
	&& pip install --no-cache-dir -r requirements.txt \
	&& pip install -e .[build,data,database,docs,notebook,profile,test,tf-cpu]\
	&& curl -sL https://deb.nodesource.com/setup_11.x | bash - \
	&& apt-get update -y \
	&& apt-get upgrade -y \
	&& apt-get install -y \
		apt-utils \
		nodejs \
	&& jupyter labextension install @telamonian/theme-darcula \
	&& jupyter labextension install jupyterlab-drawio \
	# && jupyter labextension install jupyterlab-plotly \
	# && jupyter labextension install jupyterlab-toc \
	&& rm -rf /tmp/* \
	&& rm -rf /var/lib/apt/lists/* \
	&& apt-get clean

ENV PYTHONPATH $PYTHONPATH:/opt/models/research:/opt/models/research/slim:/opt/models/research/object_detection

CMD [ "/bin/bash" ]
