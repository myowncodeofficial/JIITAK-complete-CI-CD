# Base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Install any required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the application runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
