# Use the official Bitnami Spark image as the base image
FROM bitnami/spark

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt /app/ 

# Install pipenv and dependencies
RUN pip3 install --no-cache-dir --user -r requirements.txt

# Copy the application code
COPY . /app

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the FastAPI app
CMD ["python3", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]