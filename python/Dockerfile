# Use the official Ubuntu base image
FROM ubuntu:22.04

# Set the maintainer of the image
LABEL maintainer="teammates@gmail.com"

# Update the package list and install Python and other dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

# Add the application code to the image
# Assuming you have a Python script named `app.py` in the same directory
# Copy the requirements.txt file into the container

COPY . .

# Set environment variables
ENV APP_ENV=production
ENV APP_PORT=8080

# Expose port for the application
EXPOSE 8080

# Set the working directory
WORKDIR /app

# Install Python dependencies
# Assuming you have a requirements.txt file in the same directory
RUN pip3 install --no-cache-dir -r requirements.txt

# Define the command to run the application
CMD ["python3", "app.py"]

# Explanation

# FROM ubuntu:22.04: Specifies the base image as Ubuntu 22.04.

# LABEL maintainer="yourname@example.com": Sets the maintainer label for the image.

# RUN apt-get update && apt-get install -y python3 python3-pip && apt-get clean: 
    #Updates the package list, installs Python 3 and pip, and cleans up temporary files.

# COPY app.py /app/app.py: Copies the app.py file into the /app directory in the image.

# ENV APP_ENV=production and ENV APP_PORT=8080: Sets environment variables for the application.

# EXPOSE 8080: Exposes port 8080 for inter-container communication.

# WORKDIR /app: Sets the working directory to /app.

# RUN pip3 install --no-cache-dir -r requirements.txt: Installs Python dependencies listed in requirements.txt.

# CMD ["python3", "app.py"]: Defines the default command to run the application.

# docker build -t my-python-app .
# docker run -p 8080:8080 my-python-app

