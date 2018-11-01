from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=256)
    RPwd = models.CharField(max_length=256)


class Base(models.Model):
    img = models.CharField(max_length=100)
    trackid = models.CharField(max_length=10)

    class Meta:
        abstract = True

class Wheel(Base):
    class Meta:
        db_table = "app_wheel"