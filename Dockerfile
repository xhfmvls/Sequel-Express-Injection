# Use official Node.js image as base
FROM node:20-slim

# Set working directory inside the container
WORKDIR /app

# Copy package.json and app.js to container
COPY package.json .
COPY app.js .

# Install dependencies
RUN npm install
RUN npm install nodemon

# Expose port 8080
EXPOSE 8080

# Command to run the application
# CMD ["npm", "start"]
CMD ["npm", "start"]