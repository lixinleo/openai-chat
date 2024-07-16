from django import forms

class ChatForm(forms.Form):
    question = forms.CharField(
        widget=forms.Textarea(attrs={"rows":"4", "placeholder": "your question"}),
        label= "Ask AI a question"
    )