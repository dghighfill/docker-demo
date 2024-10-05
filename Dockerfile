# Use the official Python image from the Docker Hub
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Install any dependencies if needed (example: if you have a requirements.txt)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./api/src /app/

EXPOSE 8000

# Run the hello.py script
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]