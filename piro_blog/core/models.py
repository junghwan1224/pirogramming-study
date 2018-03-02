from django.db import models
from django.urls import reverse
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model # User보다 권장하는 방법
from django.conf import settings

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Article(models.Model):  # models 왜 상속? 데이터베이스 관련 처리를 다 해주니까 !
    title = models.CharField(
        max_length=30,
        verbose_name='제목',
    )

    content = models.TextField(verbose_name='내용')  # 텍스트 필드와 차 필드의 차이점 : 텍스트 필드는 길이 지정 안해도 된다.
    liker_set = models.ManyToManyField(
            settings.AUTH_USER_MODEL,
            related_name='liked_article_set',
        )
    # user
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='생성일시'
    )  # 해당 인스턴스가 생길 때, 데이터베이스에 세이브 될 때 자동으로 그 때의 시간 기입
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='최종수정일시'
    )
    # auto now add 와 auto now 차이 : 후자는 세이브 할 때 마다 바뀐다. 전자는 처음에 생성 될 때 생긴다. 전자는 세이브 해도 안바뀐다.

    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return '{0}. {1}'.format(self.pk, self.title)

    def get_absolute_url(self):
        return reverse('core:blog_detail', kwargs={
                'pk': self.pk,
            })


class Comment(models.Model):

    article = models.ForeignKey(
            Article,
            on_delete=models.CASCADE,
        )

    author = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
        )
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment_like = models.ManyToManyField(
            settings.AUTH_USER_MODEL,
            related_name='liked_comment_set',
        )
