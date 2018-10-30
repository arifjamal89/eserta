from django.urls import path
from . import views

urlpatterns = [
	#http://127.0.0.1:8000/penganjur/
	path('', views.home, name='home_penganjur'),
	#http://127.0.0.1:8000/penganjur/aktiviti/add/
	path('aktiviti/add/', views.addaktiviti, name='add_aktiviti'),
	path('aktiviti/<int:pk>/edit/', views.editaktiviti, name='edit_aktiviti'),
	path('aktiviti/<int:pk>/delete', views.delete_aktiviti, name='delete_aktiviti'),
]