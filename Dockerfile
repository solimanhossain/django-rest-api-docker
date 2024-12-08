# Base image
FROM python:3.12-slim

# Install make and other build dependencies
RUN apt-get update && apt-get install -y make && apt-get clean


# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV POETRY_VIRTUALENVS_CREATE=false

# Install Poetry
RUN pip install --no-cache-dir poetry

# Set the working directory
WORKDIR /usr/src/app

# Copy Poetry config files and install dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry install -n --no-root

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Command to run the Django development server
CMD ["make", "runserver"]
