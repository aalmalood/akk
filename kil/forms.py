from django import forms
from .models import Customer

class reqForm(forms.ModelForm):
	nppl = forms.CharField()

	class meta:
		model = Customer
		fields = ('post',)