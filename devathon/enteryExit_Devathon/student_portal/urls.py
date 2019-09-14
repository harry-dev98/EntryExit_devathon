from django.urls import path
form .views import *

urlpatterns=[
    path('foodorder/',studentportal,name='studentportal'),
    path('thanks/',thanks,name="thanks")
]
