from django.urls import include, path
from . import views

app_name = 'installations'

urlpatterns = [
	path('',views.edit_system, name = 'add_system'),
	path('add_system/',views.edit_system, name = 'add_system'),
	path('add_installation/',views.edit_installation, name = 'add_installation'),
	path('add_person/',views.edit_person, name = 'add_person'),
	path('add_institution/',views.edit_institution, name = 'add_institution'),
	path('add_religion/',views.edit_religion, name = 'add_religion'),
	path('add_event/',views.edit_event, name = 'add_event'),
	path('add_literature/',views.edit_literature, name = 'add_literature'),
	path('add_image/',views.edit_image, name = 'add_image'),
	path('add_figure/',views.edit_figure, name = 'add_figure'),
	path('add_style/',views.edit_style, name = 'add_style'),
	path('hello_world/',views.hello_world, name = 'hello_world'),
]
