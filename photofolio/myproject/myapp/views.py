from django.shortcuts import render

# Create your views here.
def hello(request):

    return render(request, 'hello.html')

def photo(request):

    return render(request, 'photo.html')


def info(request):

    return render(request, 'info.html')

