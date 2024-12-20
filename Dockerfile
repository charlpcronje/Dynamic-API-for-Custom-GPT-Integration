FROM python:3.10-slim

# Set up working directory
WORKDIR /app

# Install necessary tools
RUN apt-get update && apt-get install -y git openssh-client && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Configure Git
ARG GIT_NAME
ARG GIT_EMAIL
RUN git config --global user.name "$GIT_NAME" && git config --global user.email "$GIT_EMAIL"

# Expose API port
EXPOSE 8000

# Start the API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
