from django.contrib import admin

from .models import Article, Tag # from core.models import Article
# 굳이 상대경로로 한 이유는? app 이름이 변경되도 별도로 수정할 필요가 없기 때문에 상대경로로 해주는 것 권장

# Register your models here.

admin.site.register(Article)
admin.site.register(Tag)