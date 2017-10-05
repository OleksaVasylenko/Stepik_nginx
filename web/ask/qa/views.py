from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from qa.models import Question
from qa.utils import paginate

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def main_page(request):
    questions = Question.objects.new()
    page = paginate(request, questions)
    return render(
        request,
        'qa/main_page.html',
        {questions: page.object_list,
         paginator: paginator,
         page: page}
    )
    
def popular_list(request):
    questions = Question.objects.popular()
    page = paginate(request, questions)
    return render(
        request,
        'qa/main_page.html',
        {questions: page.object_list,
         paginator: paginator,
         page: page}
    )

def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answers.all()
    return render(
        request,
        'qa/detail.html',
        {question: question,
         answers: answer}
    )
