from django.shortcuts import render

# Create your views here.

def homePageView(request):
    return render(request, 'home.html', {'usuario': 'Marcos'})

def contactPageView(request):
    return render(request, 'contact.html')

