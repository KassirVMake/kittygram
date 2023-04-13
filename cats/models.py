from django.db import models

# Create your models here.


class Cat(models.Model):
    class Meta:
        db_table = 'cats'

    name = models.CharField(max_length=255)
    color = models.CharField(max_length=30)
    birth_year = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f'{self.name}, {self.color}'