from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from .models import Author,Category,Post

def homepage (request):
    categories = Category.objects.all()[0:3]
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    context= {
        'object_list': featured,
        'latest': latest,
        'categories':categories,
    }
    print(categories)
    return render(request, 'HomePage.html',context)

def allposts(request):
    posts = Post.objects.order_by('-timestamp')

    context = {
        'posts': posts,
    }
    return render(request, 'AllPosts.html', context)

def postlist(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(categories=category)

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'PostList.html', context)

def post(request,slug):
    post = get_object_or_404(Post,slug=slug)
    latest = Post.objects.order_by('-timestamp')[:3]

    context = {
        'post': post,
        'latest': latest,
    }
    return render(request, 'Post.html', context)


def about (request):
    return render(request, 'AboutPage.html')

def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'object_list': queryset
    }
    return render(request, 'Search.html', context)
