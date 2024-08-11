from django.db import models

#определяет модель скилл таблицей в базе данных с полями name,description
class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    url = models.URLField(blank=True)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.title
