# plotly dash development environment
FROM python:3.12-slim-bullseye AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 # Prevents Python from writing pyc files to disc
ENV PYTHONUNBUFFERED 1 # Prevents Python from buffering stdout and stderr

# Set work directory
WORKDIR /tmp

# Install Poetry
RUN pip install --upgrade pip && \
    pip install \
    poetry \
    setuptools

# Copy the poetry.lock and pyproject.toml
COPY pyproject.toml poetry.lock  ./

# disable virtualenv creation
RUN poetry config virtualenvs.create false

# Install the dependencies
RUN poetry install --only main

# Copy the project
COPY . .

# Set the work directory
WORKDIR /app

# Run the application
CMD ["poetry", "run", "python", "app.py"]