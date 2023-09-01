# FROM python:3-alpine3.16
# WORKDIR /app
# COPY . /app/
# RUN pip install -r requirements.txt
# EXPOSE 5000
# CMD python ./main.py

# # Use the official Python image
# FROM python:3.8.10
# LABEL author="nadnan"

# # Set the working directory
# WORKDIR /app

# # Copy the application files to the container
# COPY . /app

# # Install dependencies
# RUN pip install -r requirements.txt

# # Start the Flask app
# CMD ["sh", "-c", "export $(cat .env | xargs) && flask run"]
# # CMD ["python3", "main.py"]


# Base image
FROM ubuntu:20.04
LABEL author="nadnan18"

# Set non interactive debian
ARG DEBIAN_FRONTEND=noninteractive

# Update packages
RUN apt update -y && \
    apt install -y software-properties-common && \
    apt upgrade -y

# Install Python
RUN add-apt-repository ppa:deadsnakes/ppa && \
    apt install -y python3.8 python3.8-distutils python3.8-venv python3-pip && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1

# Set the working directory
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Install dependencies
RUN python3 -m pip install -r requirements.txt

# Start app
CMD ["python3", "main.py"]
