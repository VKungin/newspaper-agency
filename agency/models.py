from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Redactor"
        verbose_name_plural = "Redactors"

    def __str__(self):
        return f"{self.username}"

    def get_absolute_url(self):
        return reverse("agency:redactors-detail", kwargs={"pk": self.pk})


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    published_date = models.DateField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    redactors = models.ManyToManyField(Redactor, related_name="newspapers")

    class Meta:
        ordering = ["published_date"]
    def __str__(self):
        return self.title
