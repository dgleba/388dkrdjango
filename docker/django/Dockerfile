# Try to make all my containers based on debian stretch-slim - this may reuse software across the system
#
# FROM python:3.5-slim-stretch --  Command "python setup.py egg_info" failed with error code 1 in 
#  /tmp/pip-install-9vqvu1aa/mysqlclient/ ERROR: Service 'djangodev' failed to build: The command '/bin/sh -c pip install -r requirements.txt' returned a non-zero code: 1
#
FROM python:3.5-stretch  

ENV PYTHONUNBUFFERED 1

# get some utilities..
RUN apt-get update && apt-get install -y \
  mc \
  --no-install-recommends && rm -r /var/lib/apt/lists/*

# project files folder
#
ENV fold=/myproject
ADD . ${fold}
WORKDIR ${fold}

RUN pip install -r requirements.txt

