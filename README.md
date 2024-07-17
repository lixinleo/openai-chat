# about this openai-chat project
1. use Python Django as framework to create this simple chat web application
2. use openai-python library to make open ai api call to answer users' question

# to run using docker file
## create a .env file with your openai api key.
```api_key="sk-proj-mZqgeW6JmcYAT3w4KIDpT3Bfdsfdfhsdhfhdsfhdsfhfh"```

## build image
```docker build -t mychat-app .  ```

## run docker container
```docker run -it -p 8000:8000 mychat-app```

## go to: http://localhost:8000/mychat

