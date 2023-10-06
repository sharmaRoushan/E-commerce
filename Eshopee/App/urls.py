from django.urls import path
from .import views



urlpatterns = [
    path('base',views.Base),
    path('',views.index)

]