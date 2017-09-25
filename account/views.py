from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateAccountForm
from django.http import JsonResponse

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

def validatingForm(request):
	if request.method == 'POST':
		form = CreateAccountForm(request.POST)
		if form.is_valid():
			return JsonResponse({'status':'success'})
		else:
			return JsonResponse({'status':'wrong', 'message':'form is not valid'})
	return JsonResponse({'status':'wrong', 'message':'no post request'})