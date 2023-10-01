from django.shortcuts import render, redirect


def index(request):
    return render(request, "index.html")


def logout(request):
    logout(request)
    return redirect("/")

