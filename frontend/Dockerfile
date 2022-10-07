FROM node:18

# set work directory
WORKDIR /app

# Copy all the frontend files
COPY ./frontend /app/frontend
RUN cd /app/frontend && npm install && npm run build

# Run the app on $PORT
CMD node build/index.js