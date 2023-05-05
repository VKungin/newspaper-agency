from django.contrib.auth.models import AbstractUser
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        verbose_name = "Redactor"
        verbose_name_plural = "Redactors"

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    published_date = models.DateField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    redactors = models.ManyToManyField(Redactor, related_name="newspapers")

    def __str__(self):
        return self.title
