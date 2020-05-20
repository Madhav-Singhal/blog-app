from django import forms
from .models import Post, AddComment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ['title','text', 'img']

class CommentForm(forms.ModelForm):

    class Meta():
        model = AddComment
        fields = ['comment']