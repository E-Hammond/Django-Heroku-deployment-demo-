from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, world. I am new to Django and Heroku</h1>")

