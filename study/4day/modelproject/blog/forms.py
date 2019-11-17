from django import forms
from .models import MyBlog
class PostForm(forms.ModelForm):

    class Meta:
        model = MyBlog

        fields = ('title', 'desc',)