from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.core.cache import cache
from dealer.git import git
from . import models

def index(request):
    context = {"git_tag": git.tag,
               "git_revision": git.revision,
               "content_timestamp": models.Meta.objects.get(pk="content_timestamp").value}
    if request.method == 'POST':
        if not 'query' in request.POST:
            context['error'] = 'Invalid query'
        elif len(request.POST['query']) < 3:
            context['error'] = 'Query must be at least 3 characters'
        else:
            query = request.POST['query']
            context['result'] = cache.get(query)
            if context['result'] is None:
                items = models.BaseItemType.objects.filter(name__icontains=request.POST['query'])
                quests = models.Quest.objects.filter(title__icontains=request.POST['query'])
                mods = models.Mod.objects.filter(name__icontains=request.POST['query'])
                result = {"items": items,
                          "quests": quests,
                          "mods": mods}
                context["result"] = result
                cache.set(query, result)
    return render(request, 'index.html', context)

def skillgem(request, skill_name):
    # TODO: Filter by correct item class
    try:
        item_type = models.BaseItemType.objects.get(Q(name=skill_name))
    except models.BaseItemType.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    rewards = models.QuestReward.objects.filter(base_item_type=item_type)
    meta = models.ActiveSkill.objects.filter(name=skill_name)
    if len(meta) > 0:
        meta = meta[0]
    else:
        meta = None
    levels = models.ItemExperiencePerLevel.objects.filter(base_item_type=item_type).order_by('level')
    if meta is not None:
        effects = models.GrantedEffectsPerLevel.objects.filter(activeskill_id=meta.id).order_by('level')
    else:
        effects = []
    context = {"rewards": rewards,
               "item_type": item_type,
               "meta": meta,
               "levels": levels,
               "effects": effects}
    return render(request, 'skillgem.html', context)


def skillgems(request):
    skillgems = models.BaseItemType.objects.filter((Q(item_class_id=19) | 
                                                    Q(item_class_id=20))).order_by('name')
    context = {"skillgems": skillgems}
    return render(request, 'skillgems.html', context)

def itemclasses(request):
    context = {"item_classes": models.ItemClass.objects.all().order_by('name')}
    return render(request, 'itemclasses.html', context)


def itemclass(request, item_class):
    items = models.BaseItemType.objects.filter(item_class__name = item_class)
    if len(items) == 0:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    context = {"items": items}
    return render(request, 'itemclass.html', context)

def mod(request):
    tags = models.Tag.objects.all().order_by('key')
    context = {"tags": tags}
    return render(request, 'mod.html', context)

def mods(request, tag_key):
    prefixes = models.Mod.objects.filter(Q(generation_type=1) &
                                         Q(modtag__tag__key=tag_key)).distinct()
    suffixes = models.Mod.objects.filter(Q(generation_type=2) &
                                         Q(modtag__tag__key=tag_key)).distinct()
    context = {"prefixes": prefixes,
               "suffixes": suffixes}
    return render(request, 'mods.html', context)

def quest(request, quest_name):
    try:
        quest = models.Quest.objects.filter(Q(title=quest_name)).first()
    except models.Quest.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    states = models.QuestState.objects.filter(quest_id=quest.id).order_by('-id')
    context = {"quest": quest,
               "states": states}
    return render(request, 'quest.html', context)


def quests(request):
    context = {"quests": models.Quest.objects.all().order_by("title")}
    return render(request, 'quests.html', context)
