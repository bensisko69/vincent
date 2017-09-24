from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateAccountForm

def index(request):
	return render(request, 'index.html')

def account(request):
	if request.method == 'POST':
		if form.is_valid():
			return render(request, 'account.html')
	else:
		form = CreateAccountForm()
	return render(request, 'account.html', {'form': form})