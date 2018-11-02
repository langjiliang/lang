from django.db import models

# Create your models here.
class Students(models.Model):
    sname=models.CharField(max_length=20)
    sage=models.IntegerField()
    sgender=models.CharField(max_length=20)
    class Meta:
        db_table='students'
        ordering=['id']
    @classmethod
    def create(cls,name,age,gender):
        stu=cls(sname=name,sage=age,sgender=gender)
        return stu

