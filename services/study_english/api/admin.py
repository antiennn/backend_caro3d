import nested_admin
from django.contrib import admin

from .form import *
from .models import *


class ChoiceInline(nested_admin.NestedStackedInline):  # Or use StackedInline for a different layout
    model = Choice
    fields = ('content', 'is_correct')
    can_delete = False

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 4 - obj.choice_set.count()
        return 4


class ChoicePassageInline(nested_admin.NestedStackedInline):  # Or use StackedInline for a different layout
    model = Choice
    fields = ('content', 'is_correct')
    can_delete = False
    extra = 4


class QuestionInline(nested_admin.NestedStackedInline):
    model = Question_passage
    extra = 2
    form = QuestionPassageForm
    inlines = [ChoicePassageInline]

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 5 - obj.choice_set.count()
        return 4


@admin.register(Question_grammar)
class QuestionAdmin(admin.ModelAdmin):
    form = QuestionForm
    list_display = ['question', 'topic']
    list_filter = ['topic']
    inlines = [ChoiceInline]


@admin.register(Topic_grammar)
class TopicGrammarAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(type_question)
class TypeQuestionAdmin(admin.ModelAdmin):
    list_display = ['content']


class PassageAdmin(nested_admin.NestedModelAdmin):
    form = PassageForm
    inlines = [QuestionInline]


admin.site.register(Passage, PassageAdmin)