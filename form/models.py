from django import forms

# Create your models here.
class ShoeForm(forms.Form):
	Shoe_Brand=forms.CharField()
	Shoe_Name=forms.CharField()
	Shoe_Heel=forms.CharField()
	Shoe_Toes=forms.CharField()
	Shoe_Type=forms.CharField()
	Shoe_Spikes=forms.CharField()
	Shoe_Event=forms.CharField()
	Shoe_Comments=forms.CharField(required=False)