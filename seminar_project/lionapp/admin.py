from django.contrib import admin

from .models import Member
from .models import UserPost
from .models import Comment
from .models import Post

admin.site.register(Post)
admin.site.register(Member)
admin.site.register(Comment)
admin.site.register(UserPost)