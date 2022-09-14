from django.contrib import admin
from .models import Post
from .models import AppComment, StudyComment
from .models import AppSeminar, AppSeminarParticipant


admin.site.register(Post)
admin.site.register(AppComment)
admin.site.register(StudyComment)
admin.site.register(AppSeminar)
admin.site.register(AppSeminarParticipant)