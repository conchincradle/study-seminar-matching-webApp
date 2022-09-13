from django.contrib import admin
from .models import Post
from .models import AppComment
from .models import AppSeminar


admin.site.register(Post)
admin.site.register(AppComment)
# admin.site.register(AppSeminar)
