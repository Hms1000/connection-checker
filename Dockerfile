# i used a python baseline image
FROM python:3.11-slim

# install required packages
RUN apt-get update && apt-get install -y iputils-ping && rm -rf /var/lib/apt/lists/*

# i set up the working directory inside the container
WORKDIR /app

# copying only requirements first for better caching
COPY requirements.txt .

# Installing dependencies
RUN pip install --no-cache-dir -r requirements.txt

# now i copy the rest of the application files
COPY . .

# these are the commands to run the script
CMD ["python3", "connection-checker.py"]
