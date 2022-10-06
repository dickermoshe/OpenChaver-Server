FROM python:3.10
RUN pip install --upgrade pip

EXPOSE 8000

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

# Run the app
CMD ["gunicorn", "-b", "0.0.0.0:8000", "openchaver_server.wsgi:application"]