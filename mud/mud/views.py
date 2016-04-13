from django.http import HttpResponse
from django.views import generic



def index(request):
    template_name = 'polls/index.html'
    return HttpResponse("Hello, world. You're at the main index.")

def about(request):
    return HttpResponse("This was created using Django.")

def math(request):
    sum = 0
    for i in range(0, 1000):
        sum+=i
    answer = sum
    return HttpResponse(str(answer))

