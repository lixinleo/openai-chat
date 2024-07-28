# about this openai-chat project
1. use Python Django as framework to create this simple chat web application
2. use openai-python library to make open ai api call to answer users' question

# to run using docker file
## create a .env file with your openai api key.
```api_key="sk-proj-mZqgeW6JmcYAT3w4KIDpT3Bfdsfdfhsdhfhdsfhdsfhfh"```

## build image
```docker build --no-cache -t mychat-app .  ```

## run docker container
```docker run -it -p 8066:8066 mychat-app```

## go to gpt4: http://localhost:8066/mychat

## go to gpt3: http://localhost:8066/mychat/gpt3
