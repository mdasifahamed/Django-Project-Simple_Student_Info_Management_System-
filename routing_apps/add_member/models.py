from django.db import models


class Students(models.Model):

    name = models.CharField(max_length=255)
    b_date = models.DateTimeField()
    reg_no = models.IntegerField()
    department = models.CharField(max_length=255)
    session = models.CharField(max_length=255)
