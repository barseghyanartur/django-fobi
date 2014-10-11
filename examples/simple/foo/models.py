from django.db import models

class FileTest(models.Model):
    file = models.FileField(upload_to='foo/')