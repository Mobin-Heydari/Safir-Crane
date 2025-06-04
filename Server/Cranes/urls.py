from django.urls import path
from . import views





app_name = "cranes"



urlpatterns = [
    path('list/', views.CranesListView.as_view(), name="crane-list"),
    path('detail/<slug:slug>/', views.CraneDetailView.as_view(), name="crane-detail")
]
