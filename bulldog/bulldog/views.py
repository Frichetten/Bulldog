from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')

def notice(request):
    return render(request, 'notice.html')

def dev(request):
    return render(request, 'dev.html')
