from django.contrib import admin
from .models import Post, Result, ResultDetails

# Register your models here.

admin.site.register(Post)
admin.site.register(Result)
admin.site.register(ResultDetails)