from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import BaseInlineFormSet

from .models import *


class QuestionForm(forms.ModelForm):
    difficulty = forms.ChoiceField(
        choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard')],
        widget=forms.RadioSelect
    )

    class Meta:
        model = Question_grammar
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        default_question, created = type_question.objects.get_or_create(
            content="question grammars"
        )
        # Set a default value for a specific field, e.g., 'field_name'
        self.fields['type_question'].initial = default_question.id

        # Disable the field to make it read-only
        self.fields['type_question'].disabled = True

    def clean(self):
        cleaned_data = super().clean()
        total_choice = int(self.data.get('choice_set-TOTAL_FORMS', '0'))
        choice_is_correct = [key for key in self.data if key.endswith('-is_correct')]
        if total_choice != 4:
            raise forms.ValidationError('Question grammars must have 4 choices')
        for i in range(4):
            if self.data.get('choice_set-{0}-content'.format(i)).strip() == "":
                raise forms.ValidationError('Choice can not be empty.')
        if len(choice_is_correct) != 1:
            raise forms.ValidationError('Question grammars must have 1 choices correct')
        return cleaned_data


class QuestionPassageForm(forms.ModelForm):
    difficulty = forms.ChoiceField(
        choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard')],
        widget=forms.RadioSelect
    )

    class Meta:
        model = Question_passage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(QuestionPassageForm, self).__init__(*args, **kwargs)
        default_question, created = type_question.objects.get_or_create(
            content="question passage"
        )
        # Set a default value for a specific field, e.g., 'field_name'
        self.fields['type_question'].initial = default_question.id

        # Disable the field to make it read-only
        self.fields['type_question'].disabled = True

    def clean(self):
        cleaned_data = super().clean()
        total_choice = int(self.data.get('choice_set-TOTAL_FORMS', '0'))
        choice_is_correct = [key for key in self.data if key.endswith('-is_correct')]
        if total_choice != 4:
            raise forms.ValidationError('Question grammars must have 4 choices')
        for i in range(4):
            if self.data.get('choice_set-{0}-content'.format(i)).strip() == "":
                raise forms.ValidationError('Choice can not be empty.')
        if len(choice_is_correct) != 1:
            raise forms.ValidationError('Question grammars must have 1 choices correct')
        return cleaned_data


class PassageForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        total_question = int(self.data.get('question_set-TOTAL_FORMS', '0'))
        if total_question != 5:
            raise forms.ValidationError('Passage must have 5 question')
        return cleaned_data
