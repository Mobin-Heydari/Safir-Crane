from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.views import View

from .models  import Blog, Category, BlogComment, BlogContent
from .forms import CommentForm




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

        instance = get_object_or_404(Blog, slug=slug)

        related_blogs = Blog.objects.filter(status="P", category=instance.category).order_by('?')[:5]

        most_viewed_blogs = Blog.objects.filter(status="P").order_by('-views')[:3]

        categories = Category.objects.all()

        form = CommentForm

        return render(request, 'Blogs/blog-detail.html', {'blog': instance, 'related' : related_blogs, 'most_viewed': most_viewed_blogs, 'categories': categories, 'form': form})
    

    def post(self, request, slug):
        instance = get_object_or_404(Blog, slug=slug)

        form = CommentForm(request.POST)

        if form.is_valid():

            cd = form.cleaned_data

            comment = BlogComment.objects.create(
                blog=instance,
                content=cd['content'],
                name=cd['name'],
            )

            comment.save()

            return redirect('blogs:blog-detail', slug)
        
        return render(request, 'Blogs/blog-detail.html', {'blog': instance, 'form': form})