from voluptuous import Schema, Required, In, All, Length, Email

login_schema = Schema({
    Required('phone'): All(str, ),
    Required('password'): str,
})

register_schema = Schema({
    Required('phone'): All(str, ),
    Required('sms_code'): All(str, ),
    Required('password1'): str,
    Required('password2'): str,
})


sms_schema = Schema({
    Required('phone'): All(str, ),
})


user_info_schema = Schema({
    Required('id'): int
})

