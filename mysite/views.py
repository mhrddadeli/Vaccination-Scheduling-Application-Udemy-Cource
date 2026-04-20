from django.shortcuts import render


def index(request):
    context = {
        "message": "Hello my site."
    }

    return render(request, "mysite/index.html", context)

