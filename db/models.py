from django.db import models

class Character(models.Model):
    name = models.TextField()
    
class ItemClass(models.Model):
    name = models.TextField()
    
class BaseItemType(models.Model):
    name = models.TextField()
    item_class = models.ForeignKey(ItemClass)
    
class Quest(models.Model):
    title = models.TextField()
    
class QuestReward(models.Model):
    base_item_type = models.ForeignKey(BaseItemType)
    quest = models.ForeignKey(Quest)
    character = models.ForeignKey(Character)
    act = models.IntegerField()


    
