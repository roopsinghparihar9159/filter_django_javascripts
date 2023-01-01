from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns=[
    path('',TemplateView.as_view(template_name='mainapp/index.html'),name='home'),
    path('list/',views.StateList.as_view(),name='list'),
    path('jsonlink/',views.jsonlink,name='jsonlink'),
]