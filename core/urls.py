# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Homepage
    path('', views.homepage, name='homepage'),
    path('base/', views.basepage, name='base'),
    
    # Navigation Pages - URL names updated to SINGULAR to match base.html
    path('services/', views.servicepage, name='service'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('projects/', views.projectpage, name='project'),
    path('publications/', views.publicationpage, name='publication'),
    path('blogs/', views.blogpage, name='blog'),
    path('events/', views.eventpage, name='event'),
    path('testimonials/', views.testimonialpage, name='testimonial'),
    path('faqs/', views.faqpage, name='faq'),
    path('contact/', views.contactpage, name='contact'),
    path('about/', views.aboutpage, name='about'),
]