# Pull base image
FROM python:3.6

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code
COPY ./ryde /code
COPY ./requirements.txt /code

# Install dependencies
RUN pip3 install --upgrade pip 
RUN pip3 install -r ./requirements.txt