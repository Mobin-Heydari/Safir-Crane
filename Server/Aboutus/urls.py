from django.urls import path
from . import views



app_name = "aboutus"

urlpatterns = [
    path('', views.AboutUsView.as_view(), name="about")
]
