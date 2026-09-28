from django.shortcuts import render
from .forms import ChatForm
from openai import OpenAI
import markdown
import bleach
from django.utils.safestring import mark_safe
import logging

logger = logging.getLogger(__name__)

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
    form = ChatForm(request.POST or None, request=request)
    if request.method == "POST" and form.is_valid():
        # set up an open api client
        client = OpenAI()
        model=form.cleaned_data['model']
        
        # customize instructions for individual models.
        instructions_by_model = {
            "gpt-5.3-codex": "You are a helpful coding assistant.",
        }

        instructions = instructions_by_model.get(model, "You are a helpful assistant.")

        try:
            response = client.responses.create(
                            model=model,
                            instructions=instructions,
                            input=form.cleaned_data['question'],
                        )
            answer = markdown_to_safe_html(response.output_text)
            return render(request, "mychat/index.html", {
                "form": form,
                "answer": answer,
                "model": model,
            })  
        except Exception:
            logger.exception("Error while processing the request")
            return render(
                request,
                "mychat/index.html",
                {
                    "form": form,
                    "error": "An error occurred while processing your request.",
                },
                status=500,
            )
        
    return render(request, "mychat/index.html", {
        "form": form
    })
    
