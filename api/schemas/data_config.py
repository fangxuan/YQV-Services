from voluptuous import Schema, All, Required, Optional, Length, Boolean

data_source_schema = Schema({
    Required('ismodify'): Boolean(),
    Optional('datasourceid'): int,
    Required('datasourcename'): All(str, Length(max=200)),
})