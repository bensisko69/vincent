from django import forms

class CreateAccountForm(forms.Form):
	CIVILITY_CHOICES = (
		('mr', 'Monsieur'),
		('mme', 'Madame'),
		('mlle', 'Mademoiselle')
	)
	firstname = forms.CharField(label='Votre prénom', max_length=200)
	lastname = forms.CharField(label='Votre nom', max_length=200)
	birthdayDate = forms.DateTimeField('Date de naissance')
	gender =  forms.CharField(max_length=1, choices=CIVILITY_CHOICES)
	level = forms.CharField(label='Votre niveaux d\'étude', max_length=100)
	school = forms.CharField(label='Votre Facultée', max_length=100)
	password =  forms.PasswordField(label='Votre mot de passe')