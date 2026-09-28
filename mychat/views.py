from django.shortcuts import render
from .forms import ChatForm
from openai import OpenAI
import markdown
import bleach
from django.utils.safestring import mark_safe

ALLOWED_TAGS = {
    "p", "br",
    "strong", "b", "em", "i", "del",
    "blockquote",
    "ul", "ol", "li",
    "pre", "code",
    "h1", "h2", "h3", "h4", "h5", "h6",
    "a",
    "table", "thead", "tbody", "tfoot",
    "tr", "th", "td",
    # Required for pymdownx.arithmatex/MathJax wrappers:
    "span", "div",
}

ALLOWED_ATTRIBUTES = {
    "a": ["href", "title"],
    "code": ["class"],
    "span": ["class"],
    "div": ["class"],
    "th": ["align"],
    "td": ["align"],
}

ALLOWED_PROTOCOLS = {"http", "https", "mailto"}

def markdown_to_safe_html(value):
    md = markdown.Markdown(
        extensions=[
            "fenced_code",
            "tables",
            "pymdownx.arithmatex",
        ],
        extension_configs={
            "pymdownx.arithmatex": {
                "generic": True,
            }
        },
    )

    converted_html = md.convert(value or "")

    sanitized_html = bleach.clean(
        converted_html,
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRIBUTES,
        protocols=ALLOWED_PROTOCOLS,
        strip=True,
        strip_comments=True,
    )

    # Only mark it safe after Bleach has sanitized it.
    return mark_safe(sanitized_html)

# Create your views here.
def index(request):
    if request.method == "POST":
        form = ChatForm(request.POST, request=request)
        
        if form.is_valid():
            # set up an open api client
            client = OpenAI()
            model=form.cleaned_data['model']

            if model == 'gpt-5.3-codex':
                response = client.responses.create(
                                model="gpt-5.3-codex",
                                instructions="You are a coding assistant.",
                                input=form.cleaned_data['question'],
                            )

                answer = (response.output_text)
            else:
                completion = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "user", "content": form.cleaned_data['question']}
                        ],
                    n=1,
                )

                # get answer and convert it using markdown libray
                answer = completion.choices[0].message.content or ""
            
            answer = markdown_to_safe_html(answer)

            return render(request, "mychat/index.html", {
                "form": form,
                "answer": answer,
                "model": form.cleaned_data['model'],
            })
        else:
            print("not valid send me haha")
    else:
        form = ChatForm(request=request)
        return render(request, "mychat/index.html", {
            "form": form
        })
    
