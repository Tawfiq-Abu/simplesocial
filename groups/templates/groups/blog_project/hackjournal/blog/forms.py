from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author','title','text')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            # editable is a medium library class that means we can edit it
            #medium-editor-textarea allows us to style like medium editor
            #postcontent allows is our own css styling class
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

        widgets ={
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea '})
        }
