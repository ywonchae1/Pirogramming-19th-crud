from django.shortcuts import render, redirect
from .models import Post

# Create your views here.

def hello_world(request):
    return render(request, 'posts/hello_world.html')

def posts_list(request, *args, **kwargs):
    # get data
    posts = Post.objects.all()
    print(posts)
    return render(request, 'posts/posts_list.html', context={'posts':posts})

# read a post
def posts_read(request, pk, *args, **kwargs):
    post = Post.objects.get(id=pk)
    print(post)

    return render(request, 'posts/posts_read.html', {'post':post})

# create a post
def posts_create(request, *argc, **kwargs):
    if request.method == 'POST':
        Post.objects.create(
            title=request.POST['title'],
            user=request.POST['user'],
            region=request.POST['region'],
            price=request.POST['price'],
            content=request.POST['content'],
        )
        return redirect('/')
    return render(request, 'posts/posts_create.html')

# delete a post
def posts_delete(request, pk, *args, **kwargs):
    # DELETE / PUT... -> REST API
    # 삭제해야 할 때 -> 삭제하기 버튼 눌러서 POST로 왔을 때
    if request.method == 'POST':
        post = Post.objects.get(id=pk)
        post.delete()
    return redirect('/')

# update a post
def posts_update(request, pk, *args, **kwargs):

    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        # edit
        post.title=request.POST['title']
        post.user=request.POST['user']
        post.region=request.POST['region']
        post.price=request.POST['price']
        post.content=request.POST['content']
        post.save()
        return redirect(f'/posts/{post.id}/')

    return render(request, 'posts/posts_update.html', {'post':post})
