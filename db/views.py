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
    item_type = models.BaseItemType.objects.get(pk=skill_id)
    if item_type is None:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    rewards = models.QuestReward.objects.filter(base_item_type=item_type)
    try:
        meta = models.ActiveSkill.objects.get(name=item_type.name)
    except models.ActiveSkill.DoesNotExist:
        meta = None
    levels = models.ItemExperiencePerLevel.objects.filter(base_item_type=item_type).order_by('level')
    context = {"rewards": rewards,
               "item_type": item_type,
               "meta": meta,
               "levels": levels}
    return render(request, 'skillgem.html', context)


def skillgems(request):
    skillgems = models.BaseItemType.objects.filter((Q(item_class_id=19) | 
                                                    Q(item_class_id=20)))
    context = {"skillgems": skillgems}
    return render(request, 'skillgems.html', context)

def itemclasses(request):
    context = {"item_classes": models.ItemClass.objects.all()}
    print(context)
    return render(request, 'itemclasses.html', context)


def itemclass(request, item_class_id):
    items = models.BaseItemType.objects.filter(item_class_id = item_class_id)
    if items is None or len(items) == 0:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    context = {"items": items}
    return render(request, 'itemclass.html', context)
