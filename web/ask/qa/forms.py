from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        super().clean()

    def save(self):
        if self._user.is_authenticated:
            user = self._user
        else:
            user, _ = User.objects.get_or_create(username='test_user')
        question = Question.objects.create(author=user, **self.cleaned_data)
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.ModelChoiceField(queryset=Question.objects.all(),
                                      widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        super().clean()

    def save(self):
        if self._user.is_authenticated:
            user = self._user
        else:
            user, _ = User.objects.get_or_create(username='test_user')
        answer = Answer.objects.create(author=user, **self.cleaned_data)
        return answer


class SignUpForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
