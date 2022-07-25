from django.urls import include, path
from . import views

app_name = 'installations'

urlpatterns = [
	path('hello_world/',views.hello_world, name = 'hello_world'),
	path('',views.edit_system, name = 'add_system'),
	path('add_system/',views.edit_system, name = 'add_system'),
]
