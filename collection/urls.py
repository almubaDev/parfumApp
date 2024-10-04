from django.urls import path
from . import views

urlpatterns = [
    path('', views.collection_manager, name='collection_manager')
]
