from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from qa.models import Question

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def new_questions(request):
    questions = Question.objects.new()
    page_num = request.GET.get('page', 1)
    limit = requset.GET.get('limit', 10)
    paginator = Paginator(posts, limit)
    page = paginator.page(page_num)
    render(
        request,
        # template path,
        {questions: page.object_list,
         paginator: paginator,
         page: page}
    )
    
