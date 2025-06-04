from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/about-me/'), name='about_me'),
    path('about-me/', views.about_me, name='about_me'),
    path('program/', views.program, name='program'),
    path('management/', views.management, name='management'),
    path('classmates/', views.classmates, name='classmates'),
]