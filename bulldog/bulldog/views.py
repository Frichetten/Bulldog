from django.shortcuts import render

def homepage(request):
    context = {'data': 'info'}
    return render(request, 'index.html', context)
