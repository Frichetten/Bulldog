from django.shortcuts import render
import subprocess

commands = ['ifconfig','ls','echo','pwd','cat','rm']

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

	if validate(command):
	    execute = subprocess.check_output(command, shell=True)
	    to_return += execute
  	elif ";" in command:
	    to_return += "INVALID COMMAND. I CAUGHT YOU HACKER! ';' CAN BE USED TO EXECUTE MULTIPLE COMMANDS!!"
	else:
	    to_return += "INVALID COMMAND. I CAUGHT YOU HACKER!"

	context = {'data': to_return}
	return render(request, 'shell.html', context)
    return render(request, 'shell.html')

def validate(command):
    if any(com in command for com in commands) and ";" not in command:
        return True
    return False
