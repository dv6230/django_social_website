from hashlib import md5

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils import timezone


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

    created = models.DateTimeField(db_index=True, default=timezone.now)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)


User.add_to_class(
    'following',
    models.ManyToManyField(
        'self',
        through=Contract,
        related_name='followers',
        symmetrical=False,  # 非對稱結構
    )
)

def avatar(self, size=80):
    md5_digest = md5(self.email.lower().encode('UTF-8')).hexdigest()
    return "https://www.gravatar.com/avatar/{}?d=identicon&s={}".format(md5_digest, size)


User.add_to_class(
    'avatar', avatar
)
