from user import User
from werkzeug.security import safe_str_cmp
# This will contains a few important functions
# For example an in memory table for users.

# Table of users
# users = [
#     {
#         "id": 1,
#         "username": "rhelyadav",
#         "password": "redhat123"
#     }
# ]

users = [
    User(1,'rhelyadav','redhat123')
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

# username_mapping = { "rhelyadav" :{
#     "id": 1,
#     "username": "rhelyadav",
#     "password": "redhat123"
# }
# }
#
# userid_mapping = username_mapping = { 1 :{
# "id": 1,
#     "username": "rhelyadav",
#     "password": "redhat123"
#     }
# }


# Function to authenticate the user
def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
