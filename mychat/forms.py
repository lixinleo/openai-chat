from django import forms

class ChatForm(forms.Form):
    question = forms.CharField(
        widget=forms.Textarea(attrs={
        "rows":"10", 
        "placeholder": "your question",
        "autofocus":True
        }),
        label= "Ask AI a question"
    )