from django.db import models
from django.conf import settings

class Trip(models.Model):
    name = models.CharField(max_length=100, default=settings.DEFAULT_NAME, null=True)
    start_date = models.DateTimeField(auto_now=False, null=False)
    end_date = models.DateTimeField(auto_now=False, null=True)
    current = models.BooleanField(null=False, default=settings.DEFAULT_CURRENT)
    day_count = models.IntegerField(null=False, default=settings.DEFAULT_DAY_COUNT)

    def __str__(self):
        return f'Trip: {self.name} = {self.start_date} - {self.end_date} = {self.day_count}'