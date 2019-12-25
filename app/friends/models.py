# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class users(models.Model):
    name = models.CharField(max_length=32)
    last_seen_ts = models.DateTimeField()
    created_at_ts = models.DateTimeField()


class friend_relation(models.Model):
    user_id = models.ForeignKey(users, on_delete=models.CASCADE, related_name='user_id')
    friend_id = models.ForeignKey(users, on_delete=models.CASCADE, related_name='friend_id')
    status = models.IntegerField(default=0)
    created_at_ts = models.DateTimeField()
