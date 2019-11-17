from django.shortcuts import render
from .models import MyBlog
from .forms import PostForm

# Create your views here.

def index(request):
    blog_all = MyBlog.objects.all()    # 쿼리셋 메소드   MyBlog라는 models.py 에서 모든 오브젝트 가져온다
    blog_one = MyBlog.objects.get(title="두번째 꼭지")

    #context = {'get_blog_all':blog_all}
    context = {'get_blog_all':blog_all, 'get_blog_one':blog_one}


    return render(request, 'index.html',context)

def other(request):
    
    myform = PostForm()

    context = {"myform" : myform}

    return render(request, 'other.html', context)