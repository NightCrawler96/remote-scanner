# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . /app

# Expose the port the app runs on
EXPOSE 5000

# Run database migrations before starting the app with Gunicorn
CMD ["bash", "-c", "flask db upgrade && gunicorn --bind 0.0.0.0:5000 app:app"]
