from django.db import models


dargs = {'on_delete':models.SET_NULL,'blank':True,'null':True}

class System(models.Model):
	original_name = models.CharField(max_length=1000,blank=True,null=True)
	ottoman_name = models.CharField(max_length=1000,blank=True,null=True)
	english_name = models.CharField(max_length=1000,blank=True,null=True)
	turkish_name = models.CharField(max_length=1000,blank=True,null=True)
	description = models.TextField(default = '')
	comments = models.TextField(default = '')

class Religion(models.Model):
	name = models.CharField(max_length=300,blank=True,null=True)
	description = models.TextField(default = '')
	comments = models.TextField(default = '')

class Gender(models.Model):
	name = models.CharField(max_length=300,blank=True,null=True)

class Person(models.Model):
	name = models.CharField(max_length=300,blank=True,null=True)
	gender = models.ForeignKey(Gender,**dargs)
	religion = models.ForeignKey(Religion,**dargs)
	description = models.TextField(default = '')
	comments = models.TextField(default = '')

class InstitutionType(models.Model):
	name = models.CharField(max_length=300,blank=True,null=True)
	description = models.TextField(default = '')
	comments = models.TextField(default = '')

class Institution(models.Model):
	original_name = models.CharField(max_length=1000,blank=True,null=True)
	ottoman_name = models.CharField(max_length=1000,blank=True,null=True)
	english_name = models.CharField(max_length=1000,blank=True,null=True)
	turkish_name = models.CharField(max_length=1000,blank=True,null=True)
	institution_type = models.ForeignKey(InstitutionType,**dargs)
	religion = models.ForeignKey(Religion,**dargs)
	description = models.TextField(default = '')
	comments = models.TextField(default = '')

class EventType(models.Model):
	name = models.CharField(max_length=300,blank=True,null=True)
	description = models.TextField(default = '')
	comments = models.TextField(default = '')

class Image(models.Model):
	gpsargs = {'blank':True,'null':True,'max_digits':8,'decimal_places':5}
	image_file = models.FileField(upload_to='IMAGES/',null=True,blank=True)
	maker = models.CharField(max_length=300,blank=True,null=True)
	title = models.CharField(max_length=300,blank=True,null=True)
	url= models.CharField(max_length=1000,blank=True,null=True)
	current_location= models.CharField(max_length=300,blank=True,null=True)
	collection = models.CharField(max_length=300,blank=True,null=True)
	description = models.TextField(default = '')
	latitude = models.DecimalField(**gpsargs)
	longitude = models.DecimalField(**gpsargs)
	comments = models.TextField(default = '')

class Style(models.Model):
	name = models.CharField(max_length=300)
	# color = ColorField(default='#FF0000')
	line_thickness = models.IntegerField(default = 2)
	fill_opacity = models.FloatField(default = 0.3)
	line_opacity = models.FloatField(default = 0.3)
	dashed = models.BooleanField(default =False) 
	z_index = models.IntegerField(default = 0)
	
class Figure(models.Model):
	name = models.CharField(max_length=300,blank=True,null=True)
	geojson= models.FileField(upload_to='GEOJSON/',null=True,blank=True)
	style = models.ForeignKey(Style,**dargs)

class Event(models.Model):
	name = models.CharField(max_length=300,blank=True,null=True)
	event_type = models.ForeignKey(EventType,**dargs)
	persons= models.ManyToManyField(Person,blank=True,default= None)
	institutions= models.ManyToManyField(Institution,blank=True,default= None)
	date_comments = models.TextField(default = '')
	images = models.ManyToManyField(Image,blank=True,default= None)
	figure = models.ForeignKey(Figure,**dargs)
	description = models.TextField(default = '')
	comments = models.TextField(default = '')

class Purpose(models.Model):
	name = models.CharField(max_length=300,blank=True,null=True)
	description = models.TextField(default = '')
	comments = models.TextField(default = '')

class InstallationType(models.Model):
	name = models.CharField(max_length=300,blank=True,null=True)
	description = models.TextField(default = '')
	comments = models.TextField(default = '')
	

class Installation(models.Model):
	original_name = models.CharField(max_length=1000,blank=True,null=True)
	ottoman_name = models.CharField(max_length=1000,blank=True,null=True)
	english_name = models.CharField(max_length=1000,blank=True,null=True)
	turkish_name = models.CharField(max_length=1000,blank=True,null=True)
	installation_type = models.ForeignKey(InstallationType,**dargs)
	events = models.ManyToManyField(Event,blank=True,default= None)
	purpose = models.ManyToManyField(Purpose,blank=True,default= None)
	description = models.TextField(default = '')
	comments = models.TextField(default = '')
	still_exists = models.BooleanField(blank=True,null=True)

class Literature(models.Model):
	code = models.CharField(max_length=300,blank=True,null=True)
	title= models.CharField(max_length=300,blank=True,null=True)
	author= models.CharField(max_length=300,blank=True,null=True)
	editor= models.CharField(max_length=300,blank=True,null=True)
	publisher= models.CharField(max_length=300,blank=True,null=True)
	place= models.CharField(max_length=300,blank=True,null=True)
	year= models.CharField(max_length=100,blank=True,null=True)
	journal= models.CharField(max_length=300,blank=True,null=True)
	volume= models.CharField(max_length=100,blank=True,null=True)
	page_numbers= models.CharField(max_length=100,blank=True,null=True)
	issue= models.CharField(max_length=100,blank=True,null=True)
	description = models.TextField(default = '')
	comments = models.TextField(default = '')
	
class SystemInstallationRelation(models.Model):
	system = models.ForeignKey(System,**dargs)
	installation = models.ForeignKey(Installation,**dargs)
	description = models.TextField(default = '')
	comments = models.TextField(default = '')
	is_part_of = models.BooleanField(blank=True,null=True)

class TextType(models.Model):
	name = models.CharField(max_length=100,blank=True,null=True)

class EventLiteratureRelation(models.Model):
	event = models.ForeignKey(Event,**dargs)
	literature = models.ForeignKey(Literature,**dargs)
	page_number= models.CharField(max_length=100,blank=True,null=True)
	text = models.TextField(default = '')
	text_file = models.FileField(upload_to='FILES/',null=True,blank=True)
	text_type = models.ForeignKey(TextType,**dargs)
	

