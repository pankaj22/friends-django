from __future__ import unicode_literals

from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=32)
    last_seen_ts = models.DateTimeField(auto_now_add=True)
    created_at_ts = models.DateTimeField(auto_now_add=True)


class FriendRelation(models.Model):
    class Meta:
        unique_together = (('user', 'friend'),)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user')
    friend = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='friend')
    status = models.IntegerField(default=1)
    created_at_ts = models.DateTimeField(auto_now_add=True)
