from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from . import models

def index(request):
    context = {}
    if request.method == 'POST':
        if not 'query' in request.POST:
            context['error'] = 'Invalid query'
        elif len(request.POST['query']) < 3:
            context['error'] = 'Query must be at least 3 characters'
        else:
            context['result'] = models.BaseItemType.objects.filter(name__icontains=request.POST['query'])
    return render(request, 'index.html', context)

def skillgem(request, skill_id):
    # TODO: Filter by correct item class
    item_type = models.BaseItemType.objects.get(pk=skill_id, )
    if item_type is None:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    rewards = models.QuestReward.objects.filter(base_item_type=item_type)
    context = {"rewards": rewards,
               "item_type": item_type}
    return render(request, 'skillgem.html', context)


def skillgems(request):
    skillgems = models.BaseItemType.objects.filter((Q(item_class_id=19) | 
                                                    Q(item_class_id=20)))
    context = {"skillgems": skillgems}
    return render(request, 'skillgems.html', context)
