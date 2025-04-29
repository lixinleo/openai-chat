from django.shortcuts import render
from .forms import ChatForm
from openai import OpenAI
import os
import markdown

# Create your views here.
def index(request):
    if request.method == "POST":
        form = ChatForm(request.POST)
        
        if form.is_valid():
            # set up an open api client
            client = OpenAI(api_key=os.getenv("api_key"))
            completion = client.chat.completions.create(
                model=form.cleaned_data['model'],
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
                "model": form.cleaned_data['model'],
            })
        else:
            print("not valid send me haha")
    else:
        form = ChatForm()
        return render(request, "mychat/index.html", {
            "form": form
        })
    
