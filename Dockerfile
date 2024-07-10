# Use python as base image
FROM python

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt /app/requirements.txt

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Expose port 3000 outside of the container
EXPOSE 3000

# Run main.py when the container launches
CMD ["python", "main.py"]