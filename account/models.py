from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Contract(models.Model):
    user_from = models.ForeignKey(
        to=User,
        related_name='from_set',
        on_delete=models.CASCADE
    )

    user_to = models.ForeignKey(
        to=User,
        related_name='to_set',
        on_delete=models.CASCADE
    )

    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)
