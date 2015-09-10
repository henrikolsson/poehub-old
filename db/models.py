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
    id = models.IntegerField(primary_key=True)
    base_item_type = models.ForeignKey(BaseItemType)
    level = models.IntegerField()
    experience = models.BigIntegerField()

class Quest(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    
class QuestReward(models.Model):
    id = models.IntegerField(primary_key=True)
    base_item_type = models.ForeignKey(BaseItemType)
    quest = models.ForeignKey(Quest)
    character = models.ForeignKey(Character)
    difficulty = models.IntegerField()

class ActiveSkill(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    image = models.TextField()

class Mod(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    domain = models.IntegerField()
    generation_type = models.IntegerField()
    key = models.TextField()
    
class Stat(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.TextField()
    
class ModStat(models.Model):
    index = models.IntegerField()
    mod = models.ForeignKey(Mod)
    stat_min = models.IntegerField()
    stat_max = models.IntegerField()
    stat = models.ForeignKey(Stat, null=True)

class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    key = models.TextField()
    
class ModTag(models.Model):
    mod = models.ForeignKey(Mod)
    tag = models.ForeignKey(Tag)
    
