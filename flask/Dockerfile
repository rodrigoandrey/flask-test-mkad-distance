# Use the Python3.9.6 image
FROM python:3.9.6-buster

# Set the working directory to /app
WORKDIR /myapp

# Copy the current directory contents into the container at /app
ADD . /myapp

# Install the dependencies
RUN pip install wheel
RUN pip install uwsgi
RUN pip install -r requirements.txt

# run the command to start uWSGI
CMD ["uwsgi", "app.ini"]