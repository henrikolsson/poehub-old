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
        cursor.execute("ALTER SEQUENCE db_character_id_seq RESTART")
        for idx in range(len(characters)):
            character = Character(id=idx, name=characters[idx]['Name'])
            character.save()
        
        item_classes = dat.parse("Data/ItemClassesDisplay.dat")
        ItemClass.objects.all().delete()
        cursor.execute("ALTER SEQUENCE db_itemclass_id_seq RESTART")
        for item_class in item_classes:
            item = ItemClass(id=item_class['Unknown3'], name=item_class["Name"])
            item.save()
        
        base_items = dat.parse("Data/BaseItemTypes.dat")
        BaseItemType.objects.all().delete()
        cursor.execute("ALTER SEQUENCE db_baseitemtype_id_seq RESTART")
        for idx in range(len(base_items)):
            item = BaseItemType(id=idx, name=base_items[idx]["Name"], item_class_id=base_items[idx]["ItemClass"])
            item.save()
                    
        quests = dat.parse("Data/Quest.dat")
        Quest.objects.all().delete()
        cursor.execute("ALTER SEQUENCE db_quest_id_seq RESTART")
        for idx in range(len(quests)):
            item = Quest(id=idx, title=quests[idx]["Title"])
            item.save()
            
        quest_rewards = dat.parse("Data/QuestRewards.dat")
        QuestReward.objects.all().delete()
        cursor.execute("ALTER SEQUENCE db_questreward_id_seq RESTART")
        for reward in quest_rewards:
            if reward['Unknown4'] < 0:
                print("weird character reference: %s" % reward['Unknown4'])
                continue
            item = QuestReward(base_item_type_id=reward['ItemKey'],
                               quest_id=reward['QuestKey'],
                               act=reward['Unknown2'],
                               character_id=reward['Unknown4'])
            item.save()
            
if __name__ == "__main__":
    main()

