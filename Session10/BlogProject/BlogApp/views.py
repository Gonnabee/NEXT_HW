from django.shortcuts import render, redirect
from .models import Article, Comment, Recomment

# Create your views here.
def home(request):
    articles = Article.objects.all()
    categorys = ['daily', 'fashion', 'study']
    count = articles.count()
    return render(request, "home.html", {'articles': articles, 'categorys': categorys, 'count': count})

def create(request):
    categorys = ['daily', 'fashion', 'study']
    if request.method == "POST":
        new_article = Article.objects.create(
            title = request.POST['title'],
            category = request.POST['category'],
            content = request.POST['content'],
        )
        return redirect('home')
    return render(request, "create.html", {'categorys': categorys})

def detail(request, category_nm):
    all_count = Article.objects.all().count()
    articles = Article.objects.filter(category=category_nm)
    count = articles.count()
    categorys = ['daily', 'fashion', 'study']
    return render(request, "detail.html", {'articles': articles, 'categorys': categorys, 'count': count, 'all_count': all_count})

def comment(request, detail_id):
    article = Article.objects.get(pk=detail_id)
    if request.method == "POST":
        content = request.POST['content']
        Comment.objects.create(
            article = article,
            content = content
        )
        return redirect('comment', article.pk)
    all_count = Article.objects.all().count()
    categorys = ['daily', 'fashion', 'study']
    return render(request, 'comment.html', {'article': article, 'categorys': categorys, 'all_count': all_count})

def comment_delete(request, detail_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    return redirect('comment', detail_id)

def recomment(request, detail_id, comment_id):
    article = Article.objects.get(pk=detail_id)
    comment = Comment.objects.get(pk=comment_id)
    all_count = Article.objects.all().count()
    categorys = ['daily', 'fashion', 'study']
    if request.method == "POST":
        content = request.POST['content']
        Recomment.objects.create(
            comment = comment,
            content = content
        )
        return redirect('recomment', article.pk, comment.pk)
    return render(request, 'recomment.html', {'article': article, 'comment': comment, 'categorys': categorys, 'all_count': all_count})

def recomment_delelte(request, detail_id, comment_id, recomment_id):
    recomment = Recomment.objects.get(pk=recomment_id)
    recomment.delete()
    return redirect('recomment', detail_id, comment_id)