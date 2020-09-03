from django import forms
from .models import Classification, Question

def get_questions():
    classifications = []
    for classifications in Classification.objects.all():
        classifications.append((classifications.pk, classification))
    return classifications

class QuestionForm(forms.Form):
    question_text = forms.CharField()
    Classification = forms.ChoiceField(choices=get_questions())


    def create_question(self):
        Classification = Classification.objects.get(
            id = self.cleaned_data['classification']
        )
        question = Question(
            classification=classification,
            question_text=self.cleaned_data['question_text']
        )
        question.save()