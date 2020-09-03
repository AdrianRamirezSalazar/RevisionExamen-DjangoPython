import datetime


from django.db import models
from django.utils import timezone


class Question(models.Model):
    classification = models.ForeignKey("Classification", on_delete=models.CASCADE, null=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
        
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
    
    
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text



class Classification(models.Model):
    classifications = (('A', 'Abierta'), ('M', 'Multiple'))
    name_classification = models.CharField(max_length=250)
    type_choice = models.CharField(max_length=1, choices=classifications, default="A")


    def __str__(self):
        return self.name_classification


    def retorno_questions(self):
        return self.question_set.all()


    

    


