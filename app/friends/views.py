from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import status
from .dataloader import *
from .controllers import *


@api_view(['GET'])
@csrf_exempt
@renderer_classes([JSONRenderer])
def index(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
@csrf_exempt
@renderer_classes([JSONRenderer])
def populateData(request):
    try:
        add_users_into_db()
        add_friends_into_db()
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@csrf_exempt
@renderer_classes([JSONRenderer])
def getUsers(request):
    if request.method != "POST":
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    try:
        usersData = getAllUsers()
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(data={"data": usersData}, status=status.HTTP_200_OK, content_type="application/json")


@api_view(['POST'])
@csrf_exempt
@renderer_classes([JSONRenderer])
def getFriends(request):
    if request.method != "POST":
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    userID = request.data.get("user_id")

    try:
        friendsData = getFriendsForUserID(userID)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(data={"data": friendsData}, status=status.HTTP_200_OK, content_type="application/json")


@api_view(['POST'])
@csrf_exempt
@renderer_classes([JSONRenderer])
def getFriendsRecommendation(request):
    if request.method != "POST":
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    userID = request.data.get("user_id")

    try:
        friendsRecommendationData = getFriendsRecommendationForUserID(userID)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(data={"data": friendsRecommendationData}, status=status.HTTP_200_OK, content_type="application/json")
