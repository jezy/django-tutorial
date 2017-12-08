from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='qqs')
    choice_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    votes = models.IntegerField(default=0)
    def __str__(self):
        return "{} {}".format(self.choice_text, self.votes)
