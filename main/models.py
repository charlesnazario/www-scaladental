from django.db import models

class StaffMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    photo_src = models.CharField(max_length=255)

    def __str__(self):
        return self.name

