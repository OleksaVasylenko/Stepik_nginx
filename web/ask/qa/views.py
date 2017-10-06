from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from qa.models import Question
from qa.utils import paginate
from qa.forms import AskForm, AnswerForm


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def main_page(request):
    questions = Question.objects.new()
    page, paginator = paginate(request, questions)
    return render(request, 'qa/main_page.html',
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
            question = form.save()
            return HttpResponseRedirect(
                reverse('qa:detail', kwargs={'pk': question.pk})
            )
    else:
        form = AskForm()
    return render(
        request,
        'qa/ask_question.html',
        {'form': form}
    )



