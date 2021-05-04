from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]  # return the first 50 characters in the text field instead of having it show up as default Post object(1), Post object(2), ...

    