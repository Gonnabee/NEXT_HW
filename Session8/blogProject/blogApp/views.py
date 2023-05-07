from django.shortcuts import render, redirect
from .models import Article
# Create your views here.

def new(request):
    categorys = ['취미', '음식', '프로그래밍']
    if request.method == 'POST':
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],

        )
        return redirect('list')

    return render(request,'new.html', {'categorys': categorys})
#url이 new일 때 실행되는 함수. new.html을 렌더링함



def list(request):
    articles = Article.objects.all()
    categorys = ['취미', '음식', '프로그래밍']
    count = articles.count()



    return render(request, 'list.html', {'articles': articles, 'categorys': categorys})
#url이 list일 때 실행되는 함수. 
#articles 이란 변수에 orm으로 Article 모델의 모든 오브젝트가 있는 배열을 담고
#list.html로 랜더링하고 해당 html에 아까 articles에 담았던 값을 articles라는 이름으로 넘겨주자

def detail(request, category_number):
    all_count = Article.objects.all().count()
    articles = Article.objects.filter(category=category_number)
    count = articles.count()
    categorys = ['취미', '음식', '프로그래밍']

    return render(request, 'detail.html', {'articles': articles, 'categorys': categorys, 'count': count, 'all_count': all_count})
    
#article 변수에 ORM으로 Article 모델의 오브젝트 중에 id가 article_id 값과 일치하는 것 찾아서 넣자.
#detail.html 렌더링 해주고 위에서 담은 article 변수를 articl이라는 이름으로 detial.html에서 넘겨주자. 
