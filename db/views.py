from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.core.cache import cache
from . import models

def index(request):
    context = {}
    if request.method == 'POST':
        if not 'query' in request.POST:
            context['error'] = 'Invalid query'
        elif len(request.POST['query']) < 3:
            context['error'] = 'Query must be at least 3 characters'
        else:
            query = request.POST['query']
            context['result'] = cache.get(query)
            if context['result'] is None:
                context['result'] = models.BaseItemType.objects.filter(name__icontains=request.POST['query'])
                cache.set(query, context['result'])
    return render(request, 'index.html', context)

def skillgem(request, skill_id):
    # TODO: Filter by correct item class
    try:
        item_type = models.BaseItemType.objects.get(pk=skill_id)
    except models.BaseItemType.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    rewards = models.QuestReward.objects.filter(base_item_type=item_type)
    meta = models.ActiveSkill.objects.filter(name=item_type.name)
    if len(meta) > 0:
        meta = meta[0]
    else:
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
    return render(request, 'itemclasses.html', context)


def itemclass(request, item_class_id):
    items = models.BaseItemType.objects.filter(item_class_id = item_class_id)
    if len(items) == 0:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    context = {"items": items}
    return render(request, 'itemclass.html', context)

def mods(request):
    prefixes = models.Mod.objects.filter(Q(generation_type=1) &
                                         Q(modtag__isnull=False)).distinct()
    suffixes = models.Mod.objects.filter(Q(generation_type=2) &
                                         Q(modtag__isnull=False)).distinct()
    context = {"prefixes": prefixes,
               "suffixes": suffixes}
    return render(request, 'mods.html', context)

def quest(request, quest_id):
    try:
        quest = models.Quest.objects.get(pk=quest_id)
    except models.Quest.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    states = models.QuestState.objects.filter(quest_id=quest_id).order_by('-id')
    context = {"quest": quest,
               "states": states}
    return render(request, 'quest.html', context)
