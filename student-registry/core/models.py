from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    course = models.CharField(max_length=80)

    def __str__(self):
        return self.name
