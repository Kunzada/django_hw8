from django.db import models

# Create your models here.
class todo(models.Model):
    class Status(models.TextChoices):
        done='d','done',
        process='i','in_process',
        planning='p','planning'

    image=models.ImageField(upload_to='todo/')
    title=models.CharField(max_length=255)
    status=models.CharField(max_length=1,choices=Status.choices,default=Status.done)
    created_at=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name="TODO"
        verbose_name_plural="TODOS"



