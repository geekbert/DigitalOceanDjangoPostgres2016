from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

from django.db import models

import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    qty = models.IntegerField(default=0)
    cost = models. IntegerField(default=0)
    
    def _get_total(self): 
        return self.qty * self.cost
    total = property(_get_total)	


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
