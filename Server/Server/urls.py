from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls', namespace="home")),
    path('blogs/', include('Blogs.urls', namespace="blogs")),
    path('cranes/', include('Cranes.urls', namespace="cranes")),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
