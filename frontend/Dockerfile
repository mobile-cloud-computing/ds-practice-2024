# Build the React application in development mode
FROM node:alpine

# Set the working directory in the container
WORKDIR /app

# Add the node_modules/.bin directory to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# Copy the package.json and package-lock.json (or yarn.lock)
COPY ./frontend/package*.json .

# Install dependencies
RUN npm install

# Copy the rest of the application files
COPY ./frontend .

# Start the development server with hot reloading
CMD npm run start