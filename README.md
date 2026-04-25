# OpenAI Chat Project

A simple chat web application built with Python Django and OpenAI API.

## About

- **Framework**: Python Django
- **API**: OpenAI Python library for API calls

## Quick Start with Docker

### 1. Create a `.env` file

Add your OpenAI API key:
```
api_key="sk-proj-mZqgeW6JmcYAT3w4KIDpT3Bfdsfdfhsdhfhdsfhdsfhfh"
```

### 2. Build the Docker image

```bash
docker build --no-cache -t mychat-app .
```

### 3. Run the container

```bash
docker run -d -it -p 8066:8066 mychat-app
```

### 4. Access the application

Open your browser and navigate to:
```
http://localhost:8066/mychat
```
