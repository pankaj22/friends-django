from .models import Users, FriendRelation


def getAllUsers():
    try:
        userData = Users.objects.all()
    except Exception as e:
        raise Exception(e)

    response = []
    for user in userData:
        response.append({
            "id": user.id,
            "name": user.name,
        })
    return response


def getFriendsForUserID(user_id):
    try:
        friendsData = FriendRelation.objects.filter(user=user_id)
    except Exception as e:
        raise Exception(e)

    response = []
    for friend in friendsData:
        response.append({
            "id": friend.friend.id,
            "name": friend.friend.name
        })
    return response


def getFriendsOfFriends(user_id):
    try:
        friendsOfFriendData = FriendRelation.objects.raw(
            'SELECT f1.id, f1.friend_id, f1.user_id FROM friends_friendrelation as f1 '
            'INNER JOIN friends_friendrelation as self ON self.friend_id=f1.user_id '
            'WHERE self.user_id=%s '
            'AND f1.friend_id NOT IN (SELECT friend_id from friends_friendrelation where user_id=%s);', [user_id, user_id])
    except Exception as e:
        raise Exception(e)

    response = []
    for data in friendsOfFriendData:
        response.append({
            "friend_id": data.friend_id,
        })
    return response


# constructing recommendations only using friends of friend.
def getFriendsRecommendationForUserID(user_id):
    return getFriendsOfFriends(user_id)
