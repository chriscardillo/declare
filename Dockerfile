FROM python:3.9.1-slim-buster
USER root

# PSQL Requirements
# RUN apt-get update && apt-get install -y libpq-dev build-essential

# Python Requirements
# ADD requirements.txt .
# RUN pip3 install -r requirements.txt
RUN pip3 install pytest
RUN pip3 install pytest-cov

# wd
WORKDIR /declare

# Sleep forever
CMD sleep infinity

# docker build . -t declare-testing
# docker run -d -v $DECLARE_HOME:/declare --name declare-testing declare-testing
# docker exec -it declare-testing /bin/bash
