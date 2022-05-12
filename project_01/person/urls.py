from django.urls import path
from person.views import peopleinfo

urlpatterns = [
    path('info',peopleinfo)
]