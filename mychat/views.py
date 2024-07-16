from django.shortcuts import render
from .forms import ChatForm
from openai import OpenAI
import os

# Create your views here.
def index(request):
    if request.method == "POST":
        form = ChatForm(request.POST)
        
        if form.is_valid():
            # get question user asked
            question = form.cleaned_data['question']
            
            # set up an open api client
            client = OpenAI(api_key=os.getenv("api_key"))
            
            # use open api completion api to get ans
            res = client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt=question,
                max_tokens=300,
                temperature=0,
            )
            
            return render(request, "mychat/answer.html", {
                "question" : question,
                "answer": res.choices[0].text
            })
        else:
            print("not valid send me haha")
    else:
        form = ChatForm()
        return render(request, "mychat/index.html", {
            "form": form
        })
    
