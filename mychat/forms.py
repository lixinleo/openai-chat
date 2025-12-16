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
    model = forms.ChoiceField(
        choices=[
            ('o4-mini', 'o4-mini')
        ],
        widget=forms.Select(attrs={
            "class": "form-select"
        }),
        label="Select AI Model"
    )