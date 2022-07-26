from .models import System, Religion, Gender, Person, InstitutionType
from .models import Institution,EventType,Image,Style,Figure,Event
from .models import Purpose,InstallationType,Installation,Literature
from .models import TextType

from django_select2.forms import ModelSelect2Widget, ModelSelect2MultipleWidget

names = 'original_name,ottoman_name,english_name,turkish_name'.split(',')

class SystemWidget(ModelSelect2Widget):
	model = System
	search_fields = [x + '__icontains' for x in names]
	
	def label_from_instance(self,obj):
		return obj.original_name

	def get_queryset(self):
		return System.objects.all().order_by('original_name')


class ReligionWidget(ModelSelect2Widget):
	model = Religion
	search_fields = ['name__icontains']

	def label_from_instance(self,obj):
		return obj.name
	
	def get_queryset(self):
		return Religion.objects.all().order_by('name')


class GenderWidget(ModelSelect2Widget):
	model = Gender
	search_fields = ['name__icontains']

	def label_from_instance(self,obj):
		return obj.name
	
	def get_queryset(self):
		return Gender.objects.all().order_by('name')


class PersonsWidget(ModelSelect2MultipleWidget):
	model = Person
	search_fields = ['name__icontains']

	def label_from_instance(self,obj):
		return obj.name
	
	def get_queryset(self):
		return Person.objects.all().order_by('name')


class InstitutionTypeWidget(ModelSelect2Widget):
	model = InstitutionType
	search_fields = ['name__icontains']

	def label_from_instance(self,obj):
		return obj.name
	
	def get_queryset(self):
		return InstitutionType.objects.all().order_by('name')


class InstitutionsWidget(ModelSelect2MultipleWidget):
	model = Institution
	search_fields = [x + '__icontains' for x in names]
	
	def label_from_instance(self,obj):
		return obj.original_name

	def get_queryset(self):
		return Institution.objects.all().order_by('original_name')


class EventTypeWidget(ModelSelect2Widget):
	model = EventType
	search_fields = ['name__icontains']

	def label_from_instance(self,obj):
		return obj.name
	
	def get_queryset(self):
		return EventType.objects.all().order_by('name')


class ImagesWidget(ModelSelect2MultipleWidget):
	model = Image
	search_fields = ['title__icontains']

	def label_from_instance(self,obj):
		return obj.title
	
	def get_queryset(self):
		return Image.objects.all().order_by('title')


class StyleWidget(ModelSelect2Widget):
	model = Style
	search_fields = ['name__icontains']

	def label_from_instance(self,obj):
		return obj.name
	
	def get_queryset(self):
		return Style.objects.all().order_by('name')
	

class FigureWidget(ModelSelect2Widget):
	model = Figure
	search_fields = ['name__icontains']

	def label_from_instance(self,obj):
		return obj.name
	
	def get_queryset(self):
		return Figure.objects.all().order_by('name')


class EventWidget(ModelSelect2Widget):
	model = Event
	search_fields = ['name__icontains']

	def label_from_instance(self,obj):
		return obj.name
	
	def get_queryset(self):
		return Event.objects.all().order_by('name')


class EventsWidget(ModelSelect2MultipleWidget):
	model = Event
	search_fields = ['name__icontains']

	def label_from_instance(self,obj):
		return obj.name
	
	def get_queryset(self):
		return Event.objects.all().order_by('name')


class PurposesWidget(ModelSelect2MultipleWidget):
	model = Purpose
	search_fields = ['name__icontains']

	def label_from_instance(self,obj):
		return obj.name
	
	def get_queryset(self):
		return Purpose.objects.all().order_by('name')


class InstallationTypeWidget(ModelSelect2Widget):
	model = InstallationType
	search_fields = ['name__icontains']

	def label_from_instance(self,obj):
		return obj.name
	
	def get_queryset(self):
		return InstallationType.objects.all().order_by('name')


class InstallationWidget(ModelSelect2Widget):
	model = System
	search_fields = [x + '__icontains' for x in names]
	
	def label_from_instance(self,obj):
		return obj.original_name

	def get_queryset(self):
		return Installation.objects.all().order_by('original_name')

class LiteratureWidget(ModelSelect2Widget):
	model = Literature
	search_fields = ['title__icontains']

	def label_from_instance(self,obj):
		return obj.title
	
	def get_queryset(self):
		return Literature.objects.all().order_by('title')


class TextTypeWidget(ModelSelect2Widget):
	model = TextType
	search_fields = ['name__icontains']

	def label_from_instance(self,obj):
		return obj.name
	
	def get_queryset(self):
		return TextType.objects.all().order_by('name')

