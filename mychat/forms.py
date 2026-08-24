from django import forms
import re

class ChatForm(forms.Form):
    def __init__(self, *args, request=None, **kwargs):
        super().__init__(*args, **kwargs)
        user_agent = request.META.get("HTTP_USER_AGENT", "") if request else ""
        if re.search(r"iphone|ipad|ipod|android|mobile", user_agent, re.IGNORECASE):
            self.fields["question"].widget.attrs["rows"] = "10"

    question = forms.CharField(
        widget=forms.Textarea(attrs={
            "rows": "30",
            "placeholder": "your question",
            "autofocus": True
        }),
        label="Ask AI a question"
    )
    model = forms.ChoiceField(
        choices=[
            ('gpt-5.3-codex', 'gpt-5.3-codex'),
            ('o4-mini', 'o4-mini'),
            ('gpt-5-mini', 'gpt-5-mini'),
            ('gpt-5.5', 'gpt-5.5')
        ],
        widget=forms.Select(attrs={
            "class": "form-select"
        }),
        label="Select AI Model"
    )
