from django.contrib import admin
from .models import Post,Sex,Comment,Like,Tag,PostTag

# Register your models here.
admin.site.register(Post)
admin.site.register(Sex)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Tag)
admin.site.register(PostTag)

