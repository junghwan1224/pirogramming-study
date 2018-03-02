from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import (
    authenticate,
    login as auth_login,
    logout as auth_logout,
)
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm

from .models import EmailConfirm
from .models import Profile
from .forms import AuthForm
from .forms import SignupForm
from .forms import ProfileForm
from .forms import SignUpProfileForm
from .utils import generate_random_string
# from .forms import LoginForm
# Create your views here.


def login(request):
    form = AuthForm(request, request.POST or None)
    # AuthenticationForm 작성할 때 첫 번째 인자로 request 꼭 적어줘야 한다.
    # from = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        # user = authenticate(
        #     request,
        #     username=form.cleaned_data['username'],
        #     password=form.cleaned_data['password'],
        #     )
        # authenticate 메소드를 안하는 이유는 AuthenticationForm 이용하면 다 처리해주기 때문.
        # user = form.get_user()
        auth_login(request, form.get_user())
        next_url = request.GET.get('next') or request.path
        # return redirect(request.path)
        # 유저가 요청한 path
        return redirect(next_url)

    ctx = {
        'form': form,
    }
    return render(request, 'accounts/login.html', ctx)


def logout(request):
    if request.method == 'POST':
        auth_logout(request)
    return redirect('core:blog_list')


def signup(request):
    signup_form = SignupForm(request.POST or None)
    profile_form = SignUpProfileForm(request.POST or None, prefix='profile')
    if request.method == 'POST':
        if signup_form.is_valid() and profile_form.is_valid():
            user = signup_form.save()
            profile = profile_form.save(commit=False)
            # profile은 유저의 정보가 필요하기 때문에 commit=False해준다.
            profile.user = user
            profile.save()
            return login_and_redirect_next(request, user)
    ctx = {
        'signup_form': signup_form,
        'profile_form': profile_form,
    }
    return render(request, 'accounts/signup.html', ctx)


def login_and_redirect_next(request, user):
    if EmailConfirm.objects.filter(user=user, is_confirmed=True).exists():  # 정상적으로 로그인이 됐을 때
        if not hasattr(user, 'profile'):
            # profile 객체가 없는 경우에 만들어준다.
            Profile.objects.create(user=user)
        auth_login(request, user)
        next_url = request.GET.get('next') or settings.LOGIN_REDIRECT_URL
        return redirect(next_url)
    else:
        # 안되면 인증메일 발송
        send_confirm_email(user)
        return redirect(reverse('accounts:email_confirm_sent'))


def send_confirm_email(user):
    try:
        email_confirm = EmailConfirm.objects.get(user=user)
        # 이미 키가 발급 됐었는지 확인. 있으면 이 전 키 활용
    except EmailConfirm.DoesNotExist:
        email_confirm = EmailConfirm.objects.create(
                user=user,
                key=generate_random_string(length=60),
            )
        # 없으면 키 새로 만든다.
    url = '{0}{1}?key={2}'.format(
            'http://localhost:8000',
            reverse('accounts:confirm_email'),
            email_confirm.key,
        )  # 인증 url
    html = '<a href="{0}">인증하기</a>'.format(url)
    send_mail(
            '인증메일 입니다.',
            '',
            settings.EMAIL_HOST_USER,
            [user.email],
            html_message=html,
        )


def email_confirm_sent(request):
    return render(request, 'accounts/email_confirm_sent.html')


def confirm_email(request):
    key = request.GET.get('key')
    email_confirm = get_object_or_404(EmailConfirm, key=key, is_confirmed=False)  # 서버에 키가 없다면 404, 있다면 인스턴스를 변수에 할당해준다
    email_confirm.is_confirmed = True
    email_confirm.save()
    return login_and_redirect_next(request, email_confirm.user)


def profile_detail(request, username):
    ctx = {
        'profile': get_object_or_404(Profile, user__username=username)
    }
    return render(request, 'accounts/profile_detail.html', ctx)


@login_required
def profile_update(request):
    form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)
    if request.method == 'POST' and form.is_valid():
        profile = form.save()
        return redirect(reverse('accounts:profile_detail', kwargs={
            'username': profile.user.username,
        }))
    ctx = {
        'form': form,
    }
    return render(request, 'accounts/profile_create.html', ctx)
