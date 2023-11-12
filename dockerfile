# Using lightweight alpine image
FROM python:3.11.4-alpine

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/usr/src/app

# Installing packages
RUN apk update
RUN pip install --no-cache-dir pipenv

# Defining working directory and adding source code
WORKDIR /usr/src/app
COPY Pipfile Pipfile.lock bootstrap.sh ./
COPY videoman ./videoman

# Install API dependencies
RUN pipenv install --system --deploy

# Start app
EXPOSE 5000
ENTRYPOINT ["/usr/src/app/bootstrap.sh"]