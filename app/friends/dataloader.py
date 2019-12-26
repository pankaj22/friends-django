from .models import Users, FriendRelation
import string, random


def add_users_into_db():
    num_of_user = 1000
    users = []
    for i in range(0, num_of_user):
        name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        users.append(Users(name=name))

    try:
        Users.objects.bulk_create(users)
    except Exception as e:
        print(e)
        raise Exception(e)


def add_friends_into_db():
    num_of_user = 1000
    for i in range(1, num_of_user+1):
        offset = random.randrange(0, 10)
        numOfFriendsForUser = random.randrange(40, 50)
        friends = []
        for j in range(0, numOfFriendsForUser):
            userID = i
            friendID = (j + i + offset) % num_of_user
            friends.append(FriendRelation(user=Users.objects.filter(id=userID).first(), friend=Users.objects.filter(id=friendID).first()))
        try:
            FriendRelation.objects.bulk_create(friends)
        except Exception as e:
            print(e)
            raise Exception(e)

    # FriendRelation(user=Users.objects.filter(id=4).first(), friend=Users.objects.filter(id=1).first()).save()
    return
