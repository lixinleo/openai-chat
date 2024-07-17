# about this openai-chat project
1. use Python Django as framework to create this simple chat web application
2. use openai-python library to make open ai api call to answer users' question

# to run using docker file
1. create a .env file with your openai api key.
api_key="sk-proj-mZqgeW6JmcYAT3w4KIDpT3Bfdsfdfhsdhfhdsfhdsfhfh"

2. build image
docker build -t mychat-app .

3. run docker container
docker run -it -p 8000:8000 mychat-app

