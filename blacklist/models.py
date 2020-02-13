import uuid
from django.db import models
from django.db.models import CharField
from django.utils import timezone


# Create your models here.

class BlackUrl(models.Model):
    class Meta:
        db_table = 'blackurl'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name: CharField = models.CharField(verbose_name='サイト名', max_length=30)
    url = models.CharField(verbose_name='URL', null=False, max_length=100)
    comment = models.CharField(verbose_name='コメント', null=False, max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
