from django.db import models


class Ask(models.Model):
    by = models.CharField(max_length=200)
    descendants = models.IntegerField()
    id_articles = models.IntegerField(primary_key=True)
    kids = models.TextField(default='')
    score = models.IntegerField()
    text = models.TextField(blank=True)
    time = models.IntegerField()
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=100)

    def __str__(self):
        return str(self.by).capitalize() + '`s' + ' article'

    class Meta:
        verbose_name = 'Ask'
        verbose_name_plural = 'Asks'


class Job(models.Model):
    by = models.CharField(max_length=200)
    id_articles = models.IntegerField(default=0, primary_key=True)
    score = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return str(self.by).capitalize() + '`s' + ' article'

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'


class Story(models.Model):
    by = models.CharField(max_length=200)
    descendants = models.IntegerField(default=0)
    id_articles = models.IntegerField(default=0, primary_key=True)
    kids = models.TextField(default='')
    score = models.IntegerField(default=0)
    text = models.TextField(blank=True)
    time = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return str(self.by).capitalize() + '`s' + ' article'

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'