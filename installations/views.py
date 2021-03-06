from django.shortcuts import render
from .models import System
from .forms import SystemForm, PersonForm, InstallationForm 
from .forms import EventForm, LiteratureForm, InstitutionForm
from .forms import ReligionForm, ImageForm, FigureForm, StyleForm
from .forms import systeminstallation_formset, installationsystem_formset
from .forms import eventliterature_formset, literatureevent_formset
from .forms import eventperson_formset, personevent_formset
from .forms import eventinstitution_formset, institutionevent_formset
from utilities.views import edit_model


# Create your views here.
def edit_system(request, pk = None, focus = '', view = 'complete'):
	names = 'systeminstallation_formset'
	return edit_model(request, __name__, 'System','installations',pk,
		formset_names = names, focus = focus, view = view)

def edit_installation(request, pk = None, focus = '', view = 'complete'):
	names = 'installationsystem_formset'
	return edit_model(request, __name__, 'Installation','installations',pk,
		formset_names = names, focus = focus, view = view)

def edit_person(request, pk = None, focus = '', view = 'complete'):
	names = 'personevent_formset'
	return edit_model(request, __name__, 'Person','installations',pk,
		formset_names = names, focus = focus, view = view)

def edit_institution(request, pk = None, focus = '', view = 'complete'):
	names = 'institutionevent_formset'
	return edit_model(request, __name__, 'Institution','installations',pk,
		formset_names = names, focus = focus, view = view)

def edit_religion(request, pk = None, focus = '', view = 'complete'):
	names = ''
	return edit_model(request, __name__, 'Religion','installations',pk,
		formset_names = names, focus = focus, view = view)

def edit_event(request, pk = None, focus = '', view = 'complete'):
	names = 'eventliterature_formset,eventperson_formset,eventinstitution_formset'
	return edit_model(request, __name__, 'Event','installations',pk,
		formset_names = names, focus = focus, view = view)

def edit_literature(request, pk = None, focus = '', view = 'complete'):
	names = 'literatureevent_formset'
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
