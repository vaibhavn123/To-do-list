from django.db import models

# Create your models here.
class tbl_todolist(models.Model):
    taskid=models.IntegerField(primary_key=True)    #Primary Key
    task=models.CharField(max_length=50)
    day=models.CharField(max_length=50)
    time=models.TimeField(max_length=50)
    deadline=models.DateField(max_length=50)
    mentor=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    class Meta:
        db_table='tbl_todolist'