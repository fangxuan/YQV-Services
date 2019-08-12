from voluptuous import Schema, Required, All

buy_plant_schema = Schema(
    {
        Required('plant_id'): int,
        Required('quantity'): All(int, )
    }
)
