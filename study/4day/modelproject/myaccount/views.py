from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm # 장고에서 기본으로 제공하는 user model

# Create your views here.
def sign_up(request):

    if request.method=="POST":
        
        save_form = UserCreationForm(request.POST)
        
        if save_form.is_valid:
            save_form.save()

            return redirect('index')
        else:
            return redirect('sign_up')
    else:
        my_signup_form = UserCreationForm()   # user form 생성

    context = {'my_signup_form': my_signup_form}

    return render(request, 'registration/sign_up.html', context)