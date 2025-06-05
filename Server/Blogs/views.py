from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views import View

from .models  import Blog, Category, BlogComment, BlogContent





class BlogsListView(View):

    def get(self, request, category_slug=None):

        queryset = Blog.objects.filter(status="P")

        most_viewed_blogs = queryset.order_by('-views')[:3]

        categories = Category.objects.all()

        if category_slug is not None:
            queryset = queryset.filter(category__slug=category_slug)

        searched_data = request.GET.get('search')

        if searched_data is not None:
            queryset = queryset.filter(title__icontains=searched_data)

        page_number = request.GET.get('page')
        paginator = Paginator(queryset, 2)
        queryset = paginator.get_page(page_number)

        return render(request, 'Blogs/blog-list.html', {'blogs': queryset, 'most_viewed': most_viewed_blogs, 'categories': categories})




class BlogDetailView(View):


    def get(self, request, slug):
        blog = get_object_or_404(Blog, slug=slug)
        return render(request, 'Blogs/blog-detail.html', {'blog': blog})