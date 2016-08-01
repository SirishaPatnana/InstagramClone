from __future__ import unicode_literals
from django.db import models

class posts(models.Model):
    image=models.ImageField(upload_to='myfiles')
    status=models.CharField(max_length=200,blank=True, null=True)
    # def __unicode__(self):
    #     return self.status