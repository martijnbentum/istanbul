from django.shortcuts import render
from .models import System
from .forms import SystemForm, PersonForm 
from .forms import systeminstallation_formset, installationsystem_formset
from utilities.views import edit_model

def hello_world(request):
	return render(request,'installations/hello_world.html')

# Create your views here.
def edit_system(request, pk = None, focus = '', view = 'complete'):
	names = 'systeminstallation_formset'
	return edit_model(request, __name__, 'System','installations',pk,
		formset_names = names, focus = focus, view = view)

def edit_installation(request, pk = None, focus = '', view = 'complete'):
	names = ''
	return edit_model(request, __name__, 'Installation','installations',pk,
		formset_names = names, focus = focus, view = view)

def edit_person(request, pk = None, focus = '', view = 'complete'):
	names = ''
	return edit_model(request, __name__, 'Person','installations',pk,
		formset_names = names, focus = focus, view = view)

def edit_institution(request, pk = None, focus = '', view = 'complete'):
	names = ''
	return edit_model(request, __name__, 'Institution','installations',pk,
		formset_names = names, focus = focus, view = view)

def edit_religion(request, pk = None, focus = '', view = 'complete'):
	names = ''
	return edit_model(request, __name__, 'Religion','installations',pk,
		formset_names = names, focus = focus, view = view)

def edit_event(request, pk = None, focus = '', view = 'complete'):
	names = ''
	return edit_model(request, __name__, 'Event','installations',pk,
		formset_names = names, focus = focus, view = view)

def edit_literature(request, pk = None, focus = '', view = 'complete'):
	names = ''
	return edit_model(request, __name__, 'Literature','installations',pk,
		formset_names = names, focus = focus, view = view)

def edit_image(request, pk = None, focus = '', view = 'complete'):
	names = ''
	return edit_model(request, __name__, 'Image','installations',pk,
		formset_names = names, focus = focus, view = view)

def edit_figure(request, pk = None, focus = '', view = 'complete'):
	names = ''
	return edit_model(request, __name__, 'Figure','installations',pk,
		formset_names = names, focus = focus, view = view)

def edit_style(request, pk = None, focus = '', view = 'complete'):
	names = ''
	return edit_model(request, __name__, 'Style','installations',pk,
		formset_names = names, focus = focus, view = view)
