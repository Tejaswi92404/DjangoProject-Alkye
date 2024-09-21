from django.shortcuts import render


#testing changes
def hello_world(request):
    return render(request, 'blog/model.html', {'message': 'Hello, world!'})