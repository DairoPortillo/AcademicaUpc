from django.urls import path
from .views import  *

urlpatterns = [

    path('resolution/create/<str:pk>', CreateResolution.as_view(), name='create_resolution'),

]