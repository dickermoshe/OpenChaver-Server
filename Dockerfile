FROM python:3.10
RUN pip install --upgrade pip

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source code
COPY . .

# Run the app on $PORT
CMD ["gunicorn", "-b", "0.0.0.0:$PORT", "openchaver_server.wsgi:application"]