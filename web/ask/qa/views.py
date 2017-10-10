from django.contrib.auth import login, models, authenticate
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from qa.models import Question
from qa.utils import paginate
from qa.forms import AskForm, AnswerForm, SignUpForm, LoginForm


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def main_page(request):
    questions = Question.objects.new()
    page, paginator = paginate(request, questions)
    return render(
        request,
        'qa/main_page.html',
        {'questions': page.object_list,
         'paginator': paginator,
         'page': page}
    )


def popular_list(request):
    questions = Question.objects.popular()
    page, paginator = paginate(request, questions)
    return render(
        request,
        'qa/main_page.html',
        {'questions': page.object_list,
         'paginator': paginator,
         'page': page}
    )


def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answer_set.all()
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            form.save()
            return HttpResponseRedirect(
                reverse('qa:detail', kwargs={'pk': pk})
            )
    else:
        form = AnswerForm(initial={'question': question})
    return render(
        request,
        'qa/detail.html',
        {'question': question,
         'answers': answers,
         'form': form}
    )

def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            question = form.save()
            return HttpResponseRedirect(
                reverse('qa:detail', kwargs={'pk': question.pk})
            )
    else:
        form = AskForm()
    return render(request, 'qa/ask_question.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = models.User.objects.create_user(**form.cleaned_data)
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('qa:main_page'))
    else:
        form = SignUpForm()
    return render(request, 'qa/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            route = 'qa:login'
            if user is not None:
                login(request, user)
                route = 'qa:main_page'
            return HttpResponseRedirect(reverse(route))
    else:
        form = LoginForm()
        return render(request, 'qa/login.html', {'form': form})
