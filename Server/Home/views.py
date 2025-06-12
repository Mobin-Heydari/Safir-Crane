from django.shortcuts import render
from django.views import View

from Blogs.models import Blog
from Cranes.models import Crane
from Contacts.forms import ContactsForm




class HomeView(View):
    def get(self, request):
        blogs = Blog.objects.filter(status='P').order_by('-published_date')[:6]
        cranes = Crane.objects.all()[:6]
        form = ContactsForm()
        return render(request, 'Home/index.html', {'cranes': cranes, 'blogs': blogs, 'form': form})