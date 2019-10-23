from api.models.user import User

user_info_ser = [
    User.id,
    User.account,
    User.created_at,
    User.user_name,
    User.department_id,
    User.permission_id,
]
