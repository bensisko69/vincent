from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateAccountForm

def index(request):
	return render(request, 'index.html')

def account(request):
	error = False;
	if request.method == 'POST':
		form = CreateAccountForm(request.POST)
		if form.is_valid():
			return render(request, 'account.html')
		else:
			error = True;
	else:
		form = CreateAccountForm()
	return render(request, 'account.html', {'form': form, 'error': error})