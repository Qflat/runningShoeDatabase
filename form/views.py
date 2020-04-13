from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'form/home.html')

def process(request):
    if request.method=='POST':
        print(request.session['toe'])
