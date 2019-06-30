from django.shortcuts import render, get_object_or_404
from .models import blog

# Create your views here.
def allBlogs(request):
    blogloop= blog.objects
    return render(request, 'blog/blogs.html', {'blogl':blogloop, 'author':"Joseph O Wcharles"})

def detail(request, blog_id):
    blogPost= get_object_or_404(blog, pk= blog_id)
    return render(request, 'blog/blogpost.html', {'blog': blogPost})
