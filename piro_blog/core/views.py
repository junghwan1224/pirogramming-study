from django.shortcuts import render
from django.utils import timezone  # 시간 다루는 패키지
from django.http import HttpResponse, Http404, JsonResponse  # Http 응답에 관련된 패키지
from django.urls import reverse  # url path 이름으로 url 검색 가능
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article, Comment, Tag
from .forms import ArticleForm, CommentForm
# Create your views here.

############## 2018. 1. 17 #######################
# 동적으로 렌더링, 기본키 값을 url로 받아와서 각각에 해당하는 내용 띄우기
# 1로 가면 1번 게시물로, 2로 가면 2번 게시물로

MAX_COMMENT_COUNT = 5


@login_required
def blog_detail(request, pk):
    # if not request.user.is_authenticated:
    #     url = reverse('accounts:login') + '?next=' + request.path
    #     return redirect(url)
    # article = Article.objects.get(pk=pk) # object = manager
    article = get_object_or_404(Article, pk=pk)
    # 2018. 1. 22
    comment_form = CommentForm(request.POST or None)
    ctx = {
        'article': article,
        'comment_form': comment_form,
        'did_like_article': article.liker_set.filter(pk=request.user.pk),
    }
    if request.method == 'POST' and comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.article = article  # article을 유저가 선택할 수 없도록 지정
        new_comment.author = request.user
        new_comment.save()
        # new_comment 부분 : 필수 부분인 article을 선택할 수 없게 하기 위해 commit=False 을 해준 뒤 author_name과 content 값만 데이터베이스에 저장을 시켜주기 위해 new_comment 변수 이용
        # ctx['comment_form'] = CommentForm() # 이렇게 해주는 이유 : 댓글 작성하고 제출 버튼 클릭 시 입력 내용 초기화 하기 위함
        return redirect(article.get_absolute_url())
    return render(request, 'core/blog.html', ctx)


def blog_list(request, tag_pk=None):
    # article_list = Article.objects.all() # 데이터베이스에 있는거 다 가져온다.
    if tag_pk is not None:
        article_list = Article.objects.filter(tag__pk=tag_pk)
        # Article 안에 있는 tag의 pk에 접근하고 싶을 때 언더바 2개(__) 사용

        # get_object_or_404 사용하는게 좋다.
        try:
            tag = Tag.objects.get(pk=tag_pk)
        except Tag.DoesNotExist:
            # tag = None
            raise Http404('No tag')
    else:
        article_list = Article.objects.all()
        tag = None
    ctx = {
        'article_list': article_list,
        'tag_list': Tag.objects.all(),
        'tag_selected': tag,
    }
    return render(request, 'core/blog_list.html', ctx)


def blog_create(request):
    #ctx = {} # 에러 메세지 담아줄 딕셔너리 2018. 1. 19
    form = ArticleForm()
    if request.method == 'POST': # if request.POST: 이렇게 조건문을 적어주는 건 별로 좋지 않다.
        form = ArticleForm(request.POST)
        if form.is_valid(): # form에 데이터 넣어보고 valid 한지 판단. 이를 통과 하면, cleaned_data가 생성된다. 꼭 해줘야 한다. 통과 못하면 에러 메세지 추가해준다.
            # article = Article.objects.create(
            #         title=form.cleaned_data['title'],
            #         content=form.cleaned_data['content'],
            # )
            article = form.save() # 이미 형식이 들어가 있으므로 그냥 save 메소드 이용할 수 있다.
            #url = reverse('blog_detail', kwargs={'pk': article.pk,})
            return redirect(article.get_absolute_url())
    ctx = {
        'form' : form, #에러가 발생했다면 에러메세지까지 담아서 템플릿으로 보내준다.
    }
    ###################### 2018. 1. 17 ############################
        #title = request.POST.get('title') # get() method는 키 값이 없으면 None 반환
        # request.POST['title'] 하면 keyError 발생
        #content = request.POST.get('content')
        #article = Article.objects.create(title=title, content=content) # 데이터베이스에 추가, 만들어진 인스턴스를 save하고 반환
        #url = reverse('blog_detail', kwargs={'pk': article.pk,}) # blog_detail 이름의 url 에 pk 값 추가해서 => ex) /article/3/
        #return redirect(url) # 페이지 이동
    ###############################################################

        # 2018. 1. 19 form 이용하기 전, 번거롭다.
        #title = request.POST.get('title')
        #content = request.POST.get('content')

        #if title and content: # 빈 입력 예외 처리
        #    article = Article.objects.create(title=title, content=content)
        #    url = reverse('blog_detail', kwargs={'pk': article.pk,})
         #   return redirect(url)

        #else: # 빈 입력이 생길 경우 에러 메세지 출력 처리
        #    err_msg={}
        #    if not title:
        #        err_msg.update({'title' : 'input title'})
        #    if not content:
        #        err_msg.update({'content' : 'input content'})
        #    ctx.update({'error' : err_msg})
    return render(request, 'core/blog_create.html', ctx)


@login_required
def blog_update(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(request.POST or None, instance=article)
    if request.method == 'POST' and form.is_valid():
        article = form.save()
        return redirect(article.get_absolute_url())

    ctx = {
        'form': form,
    }
    return render(request, 'core/blog_create.html', ctx)


@login_required
def blog_delete(request, pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        article.delete()
        return redirect(reverse("core:blog_list"))

    else:
        return HttpResponse(status=400)


@login_required
def blog_like(request, pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        if request.user.liked_article_set.filter(pk=pk).exists():
            article.liker_set.remove(request.user)
        else:
            article.liker_set.add(request.user)
        return redirect(article.get_absolute_url())

    else:
        return HttpResponse(status=400)


@login_required
def comment_like(request, pk):
    if request.method == 'POST':
        comment = Comment.objects.get(pk=pk)
        if request.user.liked_comment_set.filter(pk=pk).exists():
            comment.comment_like.remove(request.user)
        else:
            comment.comment_like.add(request.user)
        return redirect(comment.article.get_absolute_url())
    else:
        return HttpResponse(status=400)
##################################################

def one_func(request):
    title = 'Welcome 1st path !!'
    ctx = {
        'site_title': 'hi there',
        'blog_title': title,
    }
    return render(request, 'core/blog1.html', ctx)


def two_func(request):
    title = 'Welcome 2nd path !!'
    blog_title = '2nd blog title'
    ctx = {
        'site_title2': title,
        'blog_title2' : blog_title,
        'now' : timezone.now(),
        'range_10' : range(10),
    }
    return render(request, 'core/blog2.html',ctx)


def first_dynamic(request,pk):
    ctx = {
        'pk' : pk
    }
    return render(request,'core/first_dynamic.html',ctx)


def capture_string(request,url_path_str):
    ctx = {
        'path' : url_path_str,
    }
    return render(request,'core/first_dynamic.html',ctx)


def nav1_test(request):
    ctx = {
        'blog_title' : 'nav bar1 test',
    }
    return render(request,'core/blog_nav1.html',ctx)


def nav2_test(request):
    ctx = {
        'now' : timezone.now(),
        'range_5' : range(5),
        'blog_title2' : 'nav bar2 test',
    }
    return render(request,'core/blog_nav2.html',ctx)