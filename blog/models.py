from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')

    def __unicode__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.votes

class Entry(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')
    body = models.TextField()

    def __unicode__(self):
        return self.title