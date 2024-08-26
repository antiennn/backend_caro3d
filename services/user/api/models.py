from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class User(BaseModel):
    class Ranking(models.TextChoices):
        BEGINNER = "beginner"
        INTERMEDIATE = "intermediate"
        ADVANCED = "advanced"
        EXPERT = "expert"
        MASTER = "master"

    id = models.CharField(max_length=20, primary_key=True)
    display_name = models.TextField(max_length=100)
    rank = models.CharField(max_length=12, choices=Ranking.choices,null=False,default=Ranking.BEGINNER)
