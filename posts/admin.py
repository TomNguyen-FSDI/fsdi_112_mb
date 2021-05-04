from django.contrib import admin

# Register your models here.
from .models import Post

admin.site.register(Post)  # using the import Post from models.py here