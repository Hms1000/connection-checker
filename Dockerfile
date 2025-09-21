# install python base image
FROM python:3.11-slim

# install required system packages as root
RUN apt-get update && \
    apt-get install -y --no-install-recommends iputils-ping && \
    rm -rf /var/lib/apt/lists/*

# create not root user
RUN useradd -ms /bin/bash appuser

# set working directory
WORKDIR /app

# copy requirements
COPY --chown=appuser:appuser requirements.txt .

# switch to non root user
USER appuser
ENV PATH=/home/appuser/.local/bin:$PATH

# install python dependencies as non root
RUN pip install --upgrade pip && \ 
    pip install --no-cache-dir --user -r requirements.txt

# copy the rest of the application
COPY --chown=appuser:appuser . .

# run application as non root
CMD ["python3", "connection-checker.py"]


 
