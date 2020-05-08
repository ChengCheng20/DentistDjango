from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('service.html', views.service, name='service'),
    path('pricing.html', views.pricing, name='pricing'),
    path('contact.html', views.contact, name='contact'),
]