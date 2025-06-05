from django.shortcuts import render, get_object_or_404
from django.views import View

from .models  import Blog, Category, BlogComment, BlogContent





class BlogsListView(View):

    def get(self, request, category_slug=None):
        blogs = Blog.objects.filter(status="P")
        most_viewed_blogs = blogs.order_by('-views')[:3]
        categories = Category.objects.all()
        if category_slug is not None:
            blogs.filter(category__slug=category_slug)
        return render(request, 'Blogs/blog-list.html', {'blogs': blogs, 'most_viewed': most_viewed_blogs, 'categories': categories})




class BlogDetailView(View):

    def get(self, request, slug):
        blog = get_object_or_404(Blog, slug=slug)
        return render(request, 'Blogs/blog-detail.html', {'blog': blog})