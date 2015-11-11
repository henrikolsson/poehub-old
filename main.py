#!/usr/bin/env python
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'poehub.settings'

import re
import sys
from ggpk.ggpk import GGPK
from dat.dat import Dat
from db.models import *
from django.db import transaction, connection
import django
import os.path, time

# def main():
#     if len(sys.argv) == 1:
#         print("usage: %s <file>" % sys.argv[0])
#     else:
#         fn = sys.argv[1]
#         print("parsing %s..." % fn)
#         #ggpk = GGPK(fn)
#         #ggpk.read()
#         dat = Dat()
#         for record in dat.parse(fn):
#             print(record)

def main():
    dat = Dat()
    django.setup()
    with transaction.atomic():
        cursor = connection.cursor()
        
        characters = dat.parse("Data/Characters.dat")
        Character.objects.all().delete()
        for idx in range(len(characters)):
            character = Character(id=idx, name=characters[idx]['Name'])
            character.save()
        
        item_classes = dat.parse("Data/ItemClassesDisplay.dat")
        ItemClass.objects.all().delete()
        for item_class in item_classes:
            item = ItemClass(id=item_class['Id'], name=item_class["Name"])
            item.save()
        
        base_items = dat.parse("Data/BaseItemTypes.dat")
        BaseItemType.objects.all().delete()
        for idx in range(len(base_items)):
            item = BaseItemType(id=idx, name=base_items[idx]["Name"],
                                item_class_id=base_items[idx]["ItemClass"])
            item.save()

        item_experiences = dat.parse("Data/ItemExperiencePerLevel.dat")
        ItemExperiencePerLevel.objects.all().delete()
        for idx in range(len(item_experiences)):
            ie = item_experiences[idx]
            item = ItemExperiencePerLevel(id=idx,
                                          base_item_type_id=ie['BaseItemTypesKey'],
                                          experience=ie['Experience'],
                                          level=ie['ItemCurrentLevel'])
            item.save()

        quests = dat.parse("Data/Quest.dat")
        Quest.objects.all().delete()
        for idx in range(len(quests)):
            if quests[idx]["IsQuest"] == False:
                continue
            item = Quest(id=idx,
                         title=quests[idx]["Title"])
            item.save()

        states = dat.parse("Data/QuestStates.dat")
        QuestState.objects.all().delete()
        for idx in range(len(states)):
            state = states[idx]
            item = QuestState(id=idx, quest_id=state['QuestKey'], message=state['Message'], text=state['Text'])
            item.save()

        active_skills = dat.parse("Data/ActiveSkills.dat")
        ActiveSkill.objects.all().delete()
        for idx in range(len(active_skills)):
            sk = active_skills[idx]
            item = ActiveSkill(id=idx,
                               name=sk['DisplayedName'],
                               description=sk['WebsiteDescription'],
                               image=sk['WebsiteImage'])
            item.save()

        quest_rewards = dat.parse("Data/QuestRewards.dat")
        QuestReward.objects.all().delete()
        for idx in range(len(quest_rewards)):
            reward = quest_rewards[idx]
            if reward['CharactersKey'] == 18374403900871474942:
                print("weird character reference: %s" % reward['CharactersKey'])
                continue
            item = QuestReward(id=idx,
                               base_item_type_id=reward['BaseItemTypesKey'],
                               quest_id=reward['QuestKey'],
                               difficulty=reward['Difficulty'],
                               character_id=reward['CharactersKey'])
            item.save()

        tags = dat.parse("Data/Tags.dat")
        Tag.objects.all().delete()
        for idx in range(len(tags)):
            item = Tag(id=idx,
                       key=tags[idx]["Id"])
            item.save()

        stats = dat.parse("Data/Stats.dat")
        Stat.objects.all().delete()
        for idx in range(len(stats)):
            item = Stat(id=idx,
                       text=stats[idx]["Text"])
            item.save()
            
        mods = dat.parse("Data/Mods.dat")
        ModStat.objects.all().delete()
        Mod.objects.all().delete()
        for idx in range(len(mods)):
            mod = mods[idx]
            item = Mod(id=idx,
                       name=mod["Name"],
                       domain=mod["Domain"],
                       generation_type=mod["GenerationType"],
                       key=mod["Id"])
            item.save()
            for i in range(1, 5):
                stat_key = mod["StatsKey%d" % i]
                if stat_key == 18374403900871474942:
                    stat_key = None
                stat_max = mod["Stat%dMax" % i]
                stat_min = mod["Stat%dMin" % i]
                item = ModStat(index=i,
                               stat_min=stat_min,
                               stat_max=stat_max,
                               mod_id=idx,
                               stat_id=stat_key)
                item.save()
            for tag_key_idx in range(len(mod["SpawnWeight_TagsKeys"])):
                weight = mod["SpawnWeight_Values"][tag_key_idx]
                if weight == 0:
                    continue
                elif not weight == 1000:
                    print("weight was: %d" % weight)
                tag_key = mod["SpawnWeight_TagsKeys"][tag_key_idx]
                item = ModTag(mod_id = idx,
                              tag_id = tag_key)
                item.save()

    # Assume they are all the same..
    item = Meta(key='content_timestamp',
                value=time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime(os.path.getmtime('Data/Characters.dat'))))
    item.save()


if __name__ == "__main__":
    main()

