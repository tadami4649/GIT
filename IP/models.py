from django.db import models
import datetime
from django.utils import timezone

class List(models.Model):
        AVAILABLE = 'Y'
        USED = 'N'
        STATUS_FOR_NOW = ((AVAILABLE, 'Available'), (USED, 'Used'),)
        ip = models.CharField('IP Address', max_length=20)
        status = models.CharField('Status', max_length=1, choices = STATUS_FOR_NOW, default=AVAILABLE)
        user = models.CharField('User Name', max_length=30)
        machine = models.CharField('Machine Name', max_length=50)
        location = models.CharField('location', max_length=50)
        note = models.CharField('Note', max_length=100)
        date = models.DateTimeField('Date started using')
        def __unicode__(self):
                return self.ip

