from django.urls import path
from .views import *


urlpatterns = [
    path("",IndexView.as_view(),name="index"),
    path("<int:pk>/",DetailsView.as_view(),name="details"),
    path("<int:pk>/results",ResultView.as_view(),name="results"),
    path("<int:question_id>/vote",vote,name="vote"),
]
