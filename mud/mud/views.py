from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'mud/index.html')

def about(request):
    return HttpResponse("This was created using Django.")

def math(request):
    sum = 0
    for i in range(0, 1000):
        sum+=i
    answer = sum
    return HttpResponse(str(answer))

