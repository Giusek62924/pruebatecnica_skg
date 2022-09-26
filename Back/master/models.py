from django.db import models

# Create your models here.
class ROLE(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField("Role Name", max_length=30)

class ENTITY(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField("Entity Name", max_length=30)

class CITY(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField("City Name", max_length=30)

class MASTER(models.Model):
    id = models.BigAutoField(primary_key=True)
    entity = models.ForeignKey(ENTITY, on_delete=models.CASCADE)
    role = models.ForeignKey(ROLE, on_delete=models.CASCADE)
    city = models.ForeignKey(CITY, on_delete=models.CASCADE)