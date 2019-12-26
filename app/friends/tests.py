# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from rest_framework.test import APIClient
import random


class APITest(TestCase):
    def getFriends(self):
        userID = random.randrange(1, 1000)
        client = APIClient()
        response = client.post(path="/getFriends", data={"user_id": userID}, format="json")
        assert response.status_code == 200

        for friends in response.body.data:
            self.assertNotEqual(friends.id, userID, msg="Friend id can't be equal to user_id")
        return

    def getFriendsRecommendation(self):
        userID = random.randrange(1, 1000)
        client = APIClient()
        response = client.post(path="/getFriendsRecommendation$", data={"user_id": userID}, format="json")
        assert response.status_code == 200

        for friends in response.body.data:
            self.assertNotEqual(friends.friend_id, userID, msg="Recommended Friend id can't be equal to user_id")
        return
