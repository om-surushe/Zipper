from django.db import models

# Create your models here.

class Data(models.Model):
    id = models.AutoField(primary_key=True)
    encoded_string = models.TextField(null=False, blank=False)

    def _str_(self):
        return str(self.pk)
