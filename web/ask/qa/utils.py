from django.core.paginator import Paginator, EmptyPage


def paginate(request, query_set):
    try:
	limit = int(request.GET.get('limit', 10))
        page_num =int(request.GET.get('limit', 1))
    except ValueError:
        limit = 10
        page_num = 1
    if limit > 10:
        limit = 10
    paginator = Paginator(query_set, limit)
    try:
        page = paginator.page(page_num)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page

