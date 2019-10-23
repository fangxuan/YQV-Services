from voluptuous import Schema, Required, All, Length

user_login_schema = Schema({
    Required('account'): All(str, Length(max=11)),
    Required('password'): str,
})
