from django import forms
from .models import Post, AddComment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ['title','text', 'img']

class CommentForm(forms.ModelForm):
    comment= forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'text goes here', 'rows':'4', 'cols':'50'}))


    class Meta():
        model = AddComment
        fields = ['comment']
