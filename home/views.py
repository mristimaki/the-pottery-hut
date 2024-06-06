from django.shortcuts import render

def index(request):
    """ View to return to index page"""

    return render(request, 'home/index.html')
