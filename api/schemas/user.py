from voluptuous import Schema, Required, All, Length

user_login_schema = Schema({
    Required('phone'): All(str, Length(max=11)),
    Required('password'): str,
})
