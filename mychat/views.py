from django.shortcuts import render
from .forms import ChatForm
from openai import OpenAI
import os
import markdown

# Create your views here.
def gpt4(request):
    if request.method == "POST":
        form = ChatForm(request.POST)
        
        if form.is_valid():
            # set up an open api client
            client = OpenAI(api_key=os.getenv("api_key"))
            
            # use open api completion api to get ans
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": form.cleaned_data['question']}
                    ],
                n=1,
            )

            # get answer and convert it using markdown libray
            answer = completion.choices[0].message.content
            md = markdown.Markdown(extensions=["fenced_code"])
            answer = md.convert(answer)
            
            return render(request, "mychat/answer.html", {
                "question" : form.cleaned_data['question'],
                "answer": answer,
                "uri": "/mychat/gpt4",
                "model": "gpt-4o-mini",
            })
        else:
            print("not valid send me haha")
    else:
        form = ChatForm()
        return render(request, "mychat/gpt4.html", {
            "form": form
        })
    

# Create your views here.
def index(request):
    if request.method == "POST":
        form = ChatForm(request.POST)
        
        if form.is_valid():
            # set up an open api client
            client = OpenAI(api_key=os.getenv("api_key"))
          
            completion = client.chat.completions.create(
                model="o1-mini",
                messages=[
                    {"role": "user", "content": form.cleaned_data['question']}
                    ],
                n=1,
            )

            # get answer and convert it using markdown libray
            answer = completion.choices[0].message.content
            md = markdown.Markdown(extensions=["fenced_code"])
            answer = md.convert(answer)

            return render(request, "mychat/answer.html", {
                "question" : form.cleaned_data['question'],
                "answer": answer,
                "uri": "/mychat/",
                "model": "o1-mini",
            })
        else:
            print("not valid send me haha")
    else:
        form = ChatForm()
        return render(request, "mychat/index.html", {
            "form": form
        })
    
