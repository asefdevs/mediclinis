from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<slug:slug>/', views.blogdetails, name='blogdetails'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('services/', views.services, name='services'),
    path('doctor/', views.doctors, name='doctor'),
    path('doctor-details/<int:id>', views.doctordetails, name='doctordetails'),
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='booking'),
    path('appointment/', views.appointment, name='appointment'),
    path('services/<int:id>', views.service_details, name='servis_details'),

]
