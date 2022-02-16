from django.contrib import admin
from django.urls import path,include
from polls.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("polls.urls"))
]
