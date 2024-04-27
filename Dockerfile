# Pull base image
FROM python:3.9-slim

# Instal system dependencies
RUN apt-get update && apt-get install git -y

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install pipenv
RUN pip install --upgrade pip
RUN pip install pipenv

# Install project dependencies
COPY Pipfile Pipfile.lock ./
RUN pipenv install --dev --ignore-pipfile --system

# Expose port 8000 in the container
EXPOSE 8000
