from django import forms

from .models import Article
from .models import Comment

# class Article


class ArticleForm(forms.ModelForm):

    class Meta:  # 클래스의 메타정보가 들어간 클래스

        model = Article
        exclude = ('liker_set',)  # 리스트보단 튜플을 권장
        # fields = '__all__' # 모델의 모든 필드를 가져옴
        # exclude = ['create_at','updated_at'] # 작성한 필드를 제외하고 가져온다.

    # title = forms.CharField(
    #         max_length=30,
    #         label='Title'
    #     )
    # content = forms.CharField(
    #         max_length=100,
    #         label='Content'
    #     )

    def clean_title(self):
        """
        validate를 통과했을 때 메소드 호출
        title.cleaned_data['title'] 이렇게 해주면 사전에 오류가 날 수 있어서(ex. url 형식으로 입력해야 하는데 그렇게 입력을 하지 않은 경우에는 값이 안들어와 에러 발생) 키 에러가 날 수 있다.
        """

        # flag = False
        title = self.cleaned_data.get('title')
        if (title is not None):
                return title
        else:
            raise forms.ValidationError('input woo')


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput(
            attrs={
                'placeholder': 'Input Content',
            }
        ))
    # content의 input 태그에 placeholder 속성 추가.
    # 변수명은 모델의 속성 이름과 동일하게.

    class Meta:
        model = Comment
        exclude = ('article', 'author', 'comment_like', )

    # save override
    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     if commit:
    #         instance.save()
    #     return instance
