from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from . import models


# Create your views here.
class ShoeForm(TemplateView):
	template_name='form/home.html'

	def get(self, request):
		form=models.ShoeForm()
		return render(request, self.template_name, {'form':form})

	def post(self, request):
		form=ShoeForm(request.POST)
		if form.is_valid():
			brand=form.cleaned_data['Shoe_Brand']
		args={'form':form,'text':brand}
		return render(request, self.template_name, args)



def index(request):
	if request.method=='POST':
		form=ShoeForm(request.POST)
		if form.is_valid():
			'''
			Process data
			'''
			return HttpResponseRedirect('/meetDeveloper/')
	else:
		form=ShoeForm()

	return render(request, 'form/home.html', {'form':form})
