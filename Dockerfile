# Use a specific, slim version of the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Create a non-root user and switch to it
RUN useradd --create-home appuser
USER appuser

# Copy only the requirements file first to leverage Docker's layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application source code
COPY . .

# Set the default command to run the application
CMD ["python", "main.py"]