from django.shortcuts import render, HttpResponse
# Create your views here.
def home(request):
    return render(request, 'pages/home.html')
def theone(request):
    return render(request, 'pages/one.html')


def about(request):
    return render(request, 'pages/about.html')

def writings(request):
    return render(request, 'pages/writings.html')
