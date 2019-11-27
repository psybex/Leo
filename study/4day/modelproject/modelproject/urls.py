"""modelproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views # 이부분 확인 blog views import
from django.conf import settings
from django.conf.urls.static import static
from myaccount import views as account_views

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),    # path('기본 url 뒤에 붙는 url', '기본화면 호출 view 함수', 'alias')
    path('otherpage', views.other, name="other"),    # path('기본 url 뒤에 붙는 url', '기본화면 호출 view 함수', 'alias')
    path('posting', views.posting, name="posting"),  
    path('detail/<int:post_id>', views.detail, name="detail"),  
    path('update/<int:post_id>', views.update, name="update"),  
    path('delete/<int:post_id>', views.delete, name="delete"),  
    path('myaccount/sign_up', account_views.sign_up, name="sign_up"),
    path('myaccount/login', LoginView.as_view(), name="login"),
    path('myaccount/logout', LogoutView.as_view(), name="logout"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
