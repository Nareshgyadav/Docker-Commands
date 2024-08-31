# Specify the base image
FROM ubuntu:22.04

# Set the maintainer of the image
LABEL maintainer="yourname@example.com"

# Install Node.js and npm
RUN apt-get update && \
    apt-get install -y curl gnupg && \
    curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean

# Create and set the working directory
WORKDIR /usr/src/app

# Add package.json and package-lock.json to the working directory
COPY package*.json ./

# Install Node.js dependencies
RUN npm install

# Add the rest of the application code to the working directory
COPY . .

# Set environment variables
ENV NODE_ENV=production
ENV PORT=3000

# Expose the port that the application will run on
EXPOSE 3000

# Define the command to run the application
CMD ["node", "index.js"]


# Explanation
# FROM ubuntu:22.04: Specifies Ubuntu 22.04 as the base image.
# LABEL maintainer="yourname@example.com": Sets the maintainer label.
# RUN apt-get update && apt-get install -y curl gnupg && curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && apt-get install -y nodejs && apt-get clean: Updates the package list, installs Node.js and npm, and cleans up temporary files.
# WORKDIR /usr/src/app: Sets /usr/src/app as the working directory.
# COPY package*.json ./: Copies package.json and package-lock.json to the working directory.
# RUN npm install: Installs Node.js dependencies.
# COPY . .: Copies the rest of the application code to the working directory.
# ENV NODE_ENV=production and ENV PORT=3000: Sets environment variables.
# EXPOSE 3000: Exposes port 3000 for communication.
# CMD ["node", "index.js"]: Defines the command to start the Node.js application


# docker build -t my-node-app .
# docker run -p 3000:3000 my-node-app
