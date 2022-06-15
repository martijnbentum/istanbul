from django import forms
from .models import System, Religion, Gender, Person, InstitutionType
from .models import Institution,EventType,Image,Style,Figure,Event
from .models import Purpose,InstallationType,Installation,Literature
from .models import SystemInstallationRelation,TextType
from .models import EventLiteratureRelation

from .widgets import SystemWidget, ReligionWidget, GenderWidget, PersonsWidget
from .widgets import InstitutionTypeWidget,InstitutionsWidget,ImagesWidget
from .widgets import EventTypeWidget,StyleWidget,FigureWidget,
from .widgets import InstallationTypeWidget,InstallationWidget
from .widgets import TextTypeWidget,LiteratureWidget,PurposesWidget
from .widgets import EventWidget, EventsWidget
from utils.select2 import  make_select2_attr


dattr = {'attrs':{'style':'width:100%'}}
dchar = {'widget':forms.TextInput(**dattr),'required':False}
dchar_required = {'widget':forms.TextInput(**dattr),'required':True}
dtext = {'widget':forms.Textarea(attrs={'style':'width:100%','rows':3}),
	'required':False}
dgps = {'widget':forms.NumberInput(**dattr,'required':False)}
dnumber= {'widget':forms.NumberInput(attrs={'style':'width:100%','rows':3}),
	'required':False}
dselect2 = make_select2_attr(input_length = 0)
dselect2n2 = make_select2_attr(input_length = 2)


class SystemForm(forms.Model):
	original_name = forms.CharField(**dchar_required)
	ottoman_name = forms.CharField(**dchar)
	english_name = forms.CharField(**dchar)
	turkish_name = forms.CharField(**dchar)
	description = models.TextField(default = '')
	comments = models.Charifield(**dtext)

	class Meta:
		model = System
		fields = 'original_name,ottoman_name,english_name,turkish_name'
		fields = ',description,comments'
		fields = fields.split(',')


class ReligionForm(forms.Model):
	name = forms.CharField(**dchar_required)
	description = forms.CharField(**dtext)
	comments = forms.CharField(**dtext)

	class Meta:
		model = Religion
		fields = 'name,description,comments'.split(',')


class GenderForm(forms.ModelForm):
	name = forms.CharField(**dchar_required)

	class Meta:
		model = Gender
		fields = ['name']


class PersonForm(forms.ModelForm):
	name = forms.CharField(**dchar_required)
	gender = forms.ModelChoiceField(
		queryset = Gender.objects.all(),
		widget = GenderWidget(**dselect2),
		required = False)
	religion = models.ModelChoiceField(
		queryset = Religion.objects.all(),
		widget = ReligionWidget(**dselect2)
		required = False)
	description = forms.CharField(**dtext)
	comments = forms.CharField(**dtext)

	class Meta:
		model = Person
		fields = 'name,gender,birth_year,death_year,start_reign,end_reign'
		fields = ',religion,description,comments'
		fields = fields.split(',')


class InstitutionType(forms.ModelForm):
	name = forms.CharField(**dchar_required)
	description = forms.CharField(**dtext)
	comments = forms.CharField(**dtext)

	class Meta:
		model = InstitutionType
		fields = 'name,description,comments'.split(',')


class Institution(forms.ModelForm):
	original_name = forms.CharField(**dchar_required)
	ottoman_name = forms.CharField(**dchar)
	english_name = forms.CharField(**dchar)
	turkish_name = forms.CharField(**dchar)
	institution_type = models.ModelChoiceField(
		queryset = InstitutionType.objects.all(),
		widget = InstitutionTypeWidget(**dselect2),
		required = False)
	religion = models.ModelChoiceField(
		queryset = Religion.objects.all(),
		widget = ReligionWidget(**dselect2)
		required = False)
	description = forms.CharField(**dtext)
	comments = forms.CharField(**dtext)

	class Meta:
		model = Institution
		fields = 'original_name,ottoman_name,english_name,turkish_name'
		fields = ',institution_type,religion,description,comments'
		fields = fields.split(',')


class EventType(forms.ModelForm):
	name = forms.CharField(**dchar_required)
	description = forms.CharField(**dtext)
	comments = forms.CharField(**dtext)

	class Meta:
		model = EventType
		fields = 'name,description,comments'.split(',')


class Image(forms.ModelForm):
	maker = forms.CharField(**dchar)
	title = forms.CharField(**dchar
	url= forms.CharField(**dchar)
	current_location= forms.CharField(**dchar)
	collection = forms.CharField(**dchar)
	description = models.CharField(**dtext)
	latitude = forms.DecimalField(**dgps)
	longitude = forms.DecimalField(**dgps)
	comments = forms.CharField(**dtext)

	class Meta:
		model = Image
		fields = 'image_file,maker,year,title,url,current_location'
		fields = ',collection,description,comments,latitude,longitude'
		fields = fields.split(',')


class Style(forms.ModelForm):
	name = forms.CharField(**dchar_required)
	line_thickness = forms.IntegerField(**dnumber)
	fill_opacity = forms.FloatField(**dnumber)
	line_opacity = forms.FloatField(**dnumber)
	z_index = forms.IntegerField(**dnumber)

	class Meta:
		model = Style
		fields = 'name,color,line_thickness,fill_opacity,line_opacity'
		fields = ',dashed,z_index'
		fields = fields.split(',')
	

class Figure(forms.ModelForm):
	name = forms.CharField(**dchar_required)
	style = models.ModelChoiceField(
		queryset = Style.objects.all(),
		widget = StyleWidget(**dselect2),
		required = False)

	class Meta:
		model = Figure 
		fields = 'name,geojson,style'.split(',')


class Event(Forms.ModelForm):
	name = models.CharField(**dchar_required)
	event_type = models.ModelChoiceField(
		queryset = EventType.objects.all(),
		widget = EventTypeWidget(**dselect2),
		required = False)
	persons= models.ModelMultipleChoiceField(
		queryset = Person.objects.all(),
		widget = PersonsWidget(**dselect2),
		required = False)
	institutions= models.ModelMultipleChoiceField(
		queryset = Person.objects.all(),
		widget = PersonsWidget(**dselect2),
		required = False)
	date_comments = forms.TextField(**dtext)
	images = models.ModelMultipleChoiceField(
		queryset = Image.objects.all(),
		widget = ImagesWidget(**dselect2),
		required = False)
	figure = models.ModelChoiceField(
		queryset = Figure.objects.all(),
		widget = FigureWidget(**dselect2),
		required = False)
	description = forms.TextField(**dtext)
	comments = forms.TextField(**dtext

	class Meta:
		model = Event
		fields = 'name,start_date,end_date,date_comments,images'
		fields = ',figure,description,comments,event_type,persons'
		fields = ',institutions'
		fields = fields.split(',')

class Purpose(forms.ModelForm):
	name = forms.CharField(**dchar_required)
	description = forms.CharField(**dtext)
	comments = forms.CharField(**dtext)

	class Meta:
		model = Purpose
		fields = 'name,description,comments'.split(',')


class InstallationType(forms.ModelForm):
	name = forms.CharField(**dchar_required)
	description = forms.CharField(**dtext)
	comments = forms.CharField(**dtext)

	class Meta:
		model = Purpose
		fields = 'name,description,comments'.split(',')
	

class InstallationForm(forms.ModelForm):
	original_name = forms.CharField(**dchar)
	ottoman_name = forms.CharField(**dchar)
	english_name = forms.CharField(**dchar)
	turkish_name = forms.CharField(**dchar)
	installation_type = models.ModelChoiceField(
		queryset = InstallationType.objects.all(),
		widget = InstallationTypeWidget(**dselect2),
		required = False)
	events = models.ModelMultipleChoiceField(
		queryset = Event.objects.all(),
		widget = EventsWidget(**dselect2),
		required = False)
	purposes = models.ModelMultipleChoiceField(
		queryset = Purpose.objects.all(),
		widget = PurposesWidget(**dselect2),
		required = False)
	description = models.TextField(default = '')
	comments = models.Charifield(**dtext)

	class Meta:
		model = Installation
		fields = 'original_name,ottoman_name,english_name,turkish_name'
		fields = ',installation_type,events,purposes,description,comments'
		fields = ',still_exists'
		fields = fields.split(',')


class Literature(forms.ModelForm):
	code = forms.CharField(**dchar)
	title= forms.CharField(**dchar_required)
	author= forms.CharField(**dchar)
	editor= forms.CharField(**dchar)
	publisher= forms.CharField(**dchar)
	place= forms.CharField(**dchar)
	year= forms.CharField(**dchar)
	journal= forms.CharField(**dchar)
	volume= forms.CharField(**dchar)
	page_numbers= fomrs.CharField(**dchar)
	issue= forms.CharField(**dchar)
	description = forms.TextField(**dtext)
	comments = forms.TextField(**dtext)
	
	class Meta:
		model = Literature
		fields = 'code,title,author,editor'
		fields = ',publisher,place,year,journal,volume'
		fields = ',page_numbers,issue,description,comments'
		fields = fields.split(',')


class SystemInstallationRelation(forms.ModelForm):
	system = models.ModelChoiceField(
		queryset = System.objects.all(),
		widget = SystemWidget(**dselect2),
		required = False)
	installation= models.ModelChoiceField(
		queryset = Installation.objects.all(),
		widget = InstallationWidget(**dselect2),
		required = False)
	description = forms.CharField(**dtext)
	comments = forms.CharField(**dtext)

	class Meta:
		model = SystemInstallationRelation
		fields = 'system,installation,start_date,end_date'
		fields = ',description,comments,is_part_of'
		fields = fields.split(',')


class TextType(forms.ModelForm):
	name = forms.CharField(**dchar_required)

	class Meta:
		model = TextType
		fields = ['name']


class EventLiteratureRelation(forms.ModelForm):
	event = models.ModelChoiceField(
		queryset = Event.objects.all(),
		widget = EventWidget(**dselect2),
		required = False)
	literature = models.ModelChoiceField(
		queryset = Literature.objects.all(),
		widget = LiteratureWidget(**dselect2),
		required = False)
	page_number= forms.CharField(**dchar)
	text = forms.CharField(**dtext)
	text_type = models.ModelChoiceField(
		queryset = TextType.objects.all(),
		widget = TextTypeWidget(**dselect2),
		required = False)

	class Meta:
		model = EventLiteratureRelation(forms.ModelForm)
		fields = 'event,literature,page_number,text'
		fields = ',text_file,text_type'
		fields = fields.split(',')
