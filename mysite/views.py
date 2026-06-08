from django.shortcuts import render


def index(request):
    return render(request, "mysite/index.html", {})

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, "mysite/dashboard.html", {"user": request.user})