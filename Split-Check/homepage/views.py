from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def index(request):
    if request.user.is_authenticated:
        return redirect("checks:my_receipts")
    return render(request, "homepage/index.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("homepage:index")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})
