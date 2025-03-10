from django.urls import path
from . import views


urlpatterns = [
   path('hello/',views.show_my_first)
]
