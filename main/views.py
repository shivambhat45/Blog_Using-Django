from django.shortcuts import render,get_object_or_404

from django.http import Http404

from main import models

# Create your views here.

def index(request):
    # Queries are executed Lazily   
    latest_articles=models.Article.objects.all().order_by('-createdAt')[:10]

    context={
        "latest_articles":latest_articles
    }

    response=render(request,'main/index.html',context)

    return response

def article(request,pk):
    # try:
    #     article=models.Article.objects.get(pk=pk)

    # except:
    #     raise Http404()

    article=get_object_or_404(models.Article.objects,pk=pk)

    context={
        "article":article
    }

    return render(request,'main/article.html',context)

def author(request,pk):

    author=get_object_or_404(models.Author,pk=pk)

    context={
        "author":author
    }

    return render(request,'main/author.html',context)

def create_article(request):
    
    authors=models.Author.objects.all()

    context={
        "author":authors
    }

    if request.method=='POST':
        print(request.POST)

        article_data={
            "title":request.POST['title'],
            "content":request.POST['content'],

        }

        article=models.Article.objects.create(**article_data)
        author=models.Author.objects.get(pk=request.POST['author'])
        article.authors.set([author])
        # author=models.Author.objects.filter(pk=request.POST['author'])
        # article.authors.set(author)
        context["success"]=True

    return render(request,'main/create_article.html',context)