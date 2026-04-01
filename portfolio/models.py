from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tools = models.CharField(max_length=200)
    github_link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Education(models.Model):
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    year = models.CharField(max_length=50)

    def __str__(self):
        return self.school