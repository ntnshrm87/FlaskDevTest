from werkzeug.security import safe_str_cmp
from appcode.models.user import UserModel


# Function to authenticate the user
def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(UserModel.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
