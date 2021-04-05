from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    #directly linking author to the super user ....
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)
# after publishing it'll send you to the detail page with the primary keys
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    # connecting each comment to a blog app post...
    post = models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE,)
    author = models.CharField(max_length=100)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comments = models.BooleanField(default= False)


    def approve(self):
        self.approved_comments = True
        self.save()

    def get_absolute_url(self):
        #after comments get approved by user, it'll return to the home page of all list of posts
        return reverse('post_list')

    def __str__(self):
        return self.text
