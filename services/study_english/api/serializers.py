from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import Question_grammar, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        exclude = ['question']


class QuestionSerializer(serializers.ModelSerializer):
    choices = SerializerMethodField()

    class Meta:
        model = Question_grammar
        fields = '__all__'

    def get_choices(self,obj):
        choices = Choice.objects.filter(question=obj.id)
        return ChoiceSerializer(choices, many=True).data
