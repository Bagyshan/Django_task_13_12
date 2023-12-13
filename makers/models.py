from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50, default='John')
    last_name = models.CharField(max_length=50, default='Snow')
    email = models.EmailField()
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    students = models.ManyToManyField(
        Student,
        related_name='Courses'
    )

    def __str__(self) -> str:
        return f'{self.name}'

