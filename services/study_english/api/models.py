from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class type_question(BaseModel):
    id = models.AutoField(primary_key=True)
    content = models.TextField()


class Topic_grammar(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField(null=True)


class Passage(models.TextChoices):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    content = models.TextField()


class Question(BaseModel):
    id = models.AutoField(primary_key=True)
    difficulty = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(3)])
    explain = models.TextField()
    type_question = models.ForeignKey(type_question, on_delete=models.CASCADE)


class Question_grammar(Question):
    question = models.TextField(null=True)
    topic = models.ForeignKey(Topic_grammar, on_delete=models.CASCADE)
    question_id = models.OneToOneField(Question, on_delete=models.CASCADE, parent_link=True, primary_key=True)


class Question_passage(Question):
    question = models.TextField(null=True)
    passage = models.ForeignKey(Passage, on_delete=models.CASCADE)
    question_id = models.OneToOneField(Question, on_delete=models.CASCADE, parent_link=True, primary_key=True)


class Choice(BaseModel):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

