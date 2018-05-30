from uuid import uuid4
from django.db import models

class Cert(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    time_of_creation = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    file_path = models.CharField(max_length=50, blank=True)
    uuid = models.CharField(max_length=50, editable=True, null=True, blank=True)
    cert_type = models.CharField(max_length=50, blank=True)
    year = models.CharField(max_length=4, blank=True)

    def __str__(self):
        return self.year + ' - ' + self.name + ' - ' + self.cert_type