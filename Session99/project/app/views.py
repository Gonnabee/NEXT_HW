from django.shortcuts import render,redirect
from .models import Post
from datetime import date

# Create your views here.
def home(request):
    posts	= Post.objects.order_by('deadline')

    today = date.today()
    return render(request,	'home.html', {'posts' :	posts, 'today' : today})



def new(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline'],
        )     
        return redirect('detail',	new_post.pk)

    return render(request,	'new.html')

def detail(request,	post_pk):
    post	= Post.objects.get(pk=post_pk)

    return render(request,	'detail.html',	{'post':	post})

def update(request,	post_pk):
    post	= Post.objects.get(pk=post_pk)
    
    if request.method == 'POST':
        Post.objects.filter(pk=post_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline'],
        )
        return redirect('detail',	post_pk)
    
    return render(request,	'update.html',	{'post':	post})

def delete(request,	post_pk):
    post	= Post.objects.get(pk=post_pk)
    post.delete()
    
    return redirect('home')