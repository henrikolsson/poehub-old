from django.db import models

class Character(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    
class ItemClass(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    
class BaseItemType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    item_class = models.ForeignKey(ItemClass)
    
class ItemExperiencePerLevel(models.Model):
    base_item_type = models.ForeignKey(BaseItemType)
    level = models.IntegerField()
    experience = models.BigIntegerField()

class Quest(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    
class QuestReward(models.Model):
    base_item_type = models.ForeignKey(BaseItemType)
    quest = models.ForeignKey(Quest)
    character = models.ForeignKey(Character)
    act = models.IntegerField()

class ActiveSkill(models.Model):
    name = models.TextField()
    description = models.TextField()
    image = models.TextField()
    
