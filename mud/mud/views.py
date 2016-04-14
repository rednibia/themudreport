from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context

def index(request):
    t = get_template('index.html')
    html = t.render(Context({}))
    return HttpResponse(html)
I
def about(request):
    return HttpResponse("This was created using Django.")

def math(request):
    sum = 0
    for i in range(0, 1000):
        sum+=i
    answer = sum
    return HttpResponse(str(answer))

