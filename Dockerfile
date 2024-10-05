# Use the official Python image from the Docker Hub
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Copy the hello.py script from the host to the container's /app directory
COPY hello.py /app/hello.py

# Install any dependencies if needed (example: if you have a requirements.txt)
# COPY requirements.txt /app/
# RUN pip install --no-cache-dir -r requirements.txt

# Run the hello.py script
CMD ["python", "/app/hello.py"]
