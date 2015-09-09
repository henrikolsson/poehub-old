#!/usr/bin/env python
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'poehub.settings'

import sys
from ggpk.ggpk import GGPK
from dat.dat import Dat
from db.models import *
from django.db import transaction, connection
import django

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
            item = BaseItemType(id=idx, name=base_items[idx]["Name"], item_class_id=base_items[idx]["ItemClass"])
            item.save()

        item_experiences = dat.parse("Data/ItemExperiencePerLevel.dat")
        ItemExperiencePerLevel.objects.all().delete()
        for ie in item_experiences:
            item = ItemExperiencePerLevel(base_item_type_id=ie['BaseItemTypesKey'], experience=ie['Experience'], level=ie['ItemCurrentLevel'])
            item.save()

        quests = dat.parse("Data/Quest.dat")
        Quest.objects.all().delete()
        for idx in range(len(quests)):
            item = Quest(id=idx, title=quests[idx]["Title"])
            item.save()

        states = dat.parse("Data/QuestStates.dat")
        QuestState.objects.all().delete()
        for idx in range(len(states)):
            state = states[idx]
            item = QuestState(id=idx, quest_id=state['QuestKey'], message=state['Message'], text=state['Text'])
            item.save()

        active_skills = dat.parse("Data/ActiveSkills.dat")
        ActiveSkill.objects.all().delete()
        for sk in active_skills:
            item = ActiveSkill(name=sk['DisplayedName'], description=sk['WebsiteDescription'], image=sk['WebsiteImage'])
            item.save()

        quest_rewards = dat.parse("Data/QuestRewards.dat")
        QuestReward.objects.all().delete()
        cursor.execute("ALTER SEQUENCE db_questreward_id_seq RESTART")
        for reward in quest_rewards:
            if reward['CharactersKey'] < 0:
                print("weird character reference: %s" % reward['CharactersKey'])
                continue
            if reward['CharactersKey'] > 10:
                print("weird character reference: %s" % reward['CharactersKey'])
                continue
            item = QuestReward(base_item_type_id=reward['BaseItemTypesKey'],
                               quest_id=reward['QuestKey'],
                               act=reward['Difficulty'],
                               character_id=reward['CharactersKey'])
            item.save()

if __name__ == "__main__":
    main()

