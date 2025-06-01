from django.shortcuts import render, get_object_or_404
from django.views import View

from .models  import Blog, BlogComment, BlogContent





class BlogsListView(View):

    def get(self, request):
        blogs = Blog.objects.filter(status="P")
        return render(request, 'Blogs/blog-list.html', {'blogs': blogs})




class BlogDetailView(View):

    def get(self, request, slug):
        blog = get_object_or_404(Blog, slug=slug)
        return render(request, 'Blogs/blog-detail.html', {'blog': blog})