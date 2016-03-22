from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the main index.")

def about(request):
    return HttpResponse("This was created using Django.")

def math(request):
    answer = 5
    return HttpResponse(str(answer))
