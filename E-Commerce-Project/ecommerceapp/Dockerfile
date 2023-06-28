FROM python:3.9-slim 

RUN pip install virtualenv && \
  virtualenv /opt/venv && \
  /bin/bash -c "source /opt/venv/bin/activate"


# set workdir for docker
WORKDIR /ecommerceapp

# add requirements file
ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . /ecommerceapp

# add /pipeline to python path
ENV PYTHONPATH="$PYTHONPATH:/ecommerceapp"

# TODO: create cmd to dump aisles and department csvs first into data warehouse
