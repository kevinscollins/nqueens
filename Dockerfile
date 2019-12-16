FROM python:3.7-alpine

# Install Linux packages
RUN apk update && apk add postgresql-dev postgresql-client gcc python3-dev musl-dev bash

# Install Python packages
ADD requirements.txt /
RUN python -m pip install -r /requirements.txt --no-cache-dir
