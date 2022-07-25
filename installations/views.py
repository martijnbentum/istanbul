from django.shortcuts import render
from .models import System
from .forms import SystemForm
from utilities.views import edit_model

def hello_world(request):
	return render(request,'installations/hello_world.html')

# Create your views here.
def edit_system(request, pk = None, focus = '', view = 'complete'):
	names = ''
	return edit_model(request, __name__, 'System','installations',pk,
		formset_names = names, focus = focus, view = view)
