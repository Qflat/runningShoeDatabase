from django import forms

# Create your models here.
class ShoeForm(forms.Form):
	shoe_brand=forms.CharField(label='Shoe Brand')
	shoe_name=forms.CharField(label='Name of Shoe Model')
	heel_stack=forms.CharField(label='Heel Stack Height (mm)')
	toe_stack=forms.CharField(label='Toe Stack Height (mm)')
	shoe_type=forms.CharField(label='Is this shoe a trainer, spikes, or racing flat?')
	number_of_spikes=forms.CharField(label='How many spikes can this shoe hold?')
	event=forms.CharField(label='What event would these shoes be best for?')
	comments=forms.CharField(required=False, label='Please type any other comments here')