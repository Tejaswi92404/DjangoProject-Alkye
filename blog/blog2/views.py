from django.shortcuts import render

def hello_world(request):
    return render(request, 'blog/model.html', {'message': 'Hello, world!'})