# Use an official Python runtime as the base image
FROM python:3.8-slim

ARG DEBIAN_FRONTED=noninteractive

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory (our Flask app) into the container at /app
COPY . /app

# Install Flask and other dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available for the app
EXPOSE 5000
# Run init_db.py to create database tables
#RUN python3 init_db.py

ENV FLASK_APP=app.py

# Run the command to start the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
