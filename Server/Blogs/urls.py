from django.urls import path

from . import views



app_name = "Blogs"


urlpatterns = [
    path('list/', views.BlogsListView.as_view(), name="blog-list"),
    path('list/<slug:category_slug>/', views.BlogsListView.as_view(), name="blog-list-category"),
    path('detail/<slug:slug>/', views.BlogsListView.as_view(), name="blog-detail")
]
