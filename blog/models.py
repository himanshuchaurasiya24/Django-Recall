from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_body = models.TextField()
    def __str__(self):
        return self.blog_title
    
class Comment(models.Model):
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    def __str__(self):
        # return self.comment[:20]  # Return the first 20 characters of the comment for display
        return self.comment

      