from django.urls import path
from django.views.generic import TemplateView

from .views import signup

urlpatterns =[
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('signup', signup, name='signup'),
]