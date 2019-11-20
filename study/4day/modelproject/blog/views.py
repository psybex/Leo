from django.shortcuts import render, redirect, get_object_or_404
from .models import MyBlog
from .forms import PostForm
from .forms import PostForm2

# Create your views here.

def index(request):
    blog_all = MyBlog.objects.all()    # 쿼리셋 메소드   MyBlog라는 models.py 에서 모든 오브젝트 가져온다
    # blog_one = MyBlog.objects.get(title="두번째 꼭지")

    context = {'get_blog_all':blog_all}
    #context = {'get_blog_all':blog_all, 'get_blog_one':blog_one}


    return render(request, 'index.html',context)

def other(request):
    
    myform = PostForm()

    context = {"myform" : myform}

    return render(request, 'other.html', context)

def posting(request):
    # 모델폼 들어갈 예정

    myform2 = PostForm2()

    if request.method == "POST" :
        myform2 = PostForm2(request.POST)
        if myform2.is_valid:
            myform2.save()
            return redirect('index')               # redirect import 하고 사용해야함!!
        else:
            return redirect('posting')

    else:
        myform2 = PostForm2()        

    context = {"myform2" : myform2}

    return render(request, 'posting.html', context)

def detail(request, post_id):
    # 제목 링크에 대한 detail page를 생성
    post_one = get_object_or_404(MyBlog, id = post_id)

    context = {"post_one":post_one}

    return render(request, 'detail.html', context)

def update(request, post_id):

    my_post_one = get_object_or_404(MyBlog, id = post_id)

    if request.method == "POST" :
        myform2 = PostForm2(request.POST, instance=my_post_one)
        if myform2.is_valid:
            myform2.save()
            return redirect('index')               # redirect import 하고 사용해야함!!
        else:
            return redirect('posting')
    else:
        my_update_form = PostForm2(instance = my_post_one)    

    context = {'myform2' : my_update_form}

    return render(request, 'update.html', context)


def delete(request, post_id):

    my_post_one = get_object_or_404(MyBlog, id = post_id)

    my_post_one.delete()

    return redirect('index')