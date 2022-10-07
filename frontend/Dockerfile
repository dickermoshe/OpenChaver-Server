FROM node:18

# set work directory
WORKDIR /app

# Copy source code
COPY . .

# Install and build
RUN npm install && npm run build

# Run the app on $PORT
CMD node build/index.js -p ${PORT}:3000