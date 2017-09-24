from django import forms

class CreateAccountForm(forms.Form):
	CIVILITY_CHOICES = (
		('mr', ('Monsieur')),
		('mme', ('Madame')),
		('mlle', ('Mademoiselle'))
	)
	firstname = forms.CharField(max_length=200)
	lastname = forms.CharField(max_length=200)
	birthdayDate = forms.DateField()
	gender =  forms.ChoiceField(choices=CIVILITY_CHOICES)
	level = forms.CharField(max_length=100)
	school = forms.CharField(max_length=100)
	password = forms.CharField(max_length=32, widget=forms.PasswordInput)