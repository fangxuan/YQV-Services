from voluptuous import Schema, Required, All, In

buy_schema = Schema(
    {
        Required('item_id'): int,
        Required('type'): In(('FERTILIZER', 'PESTICIDE', 'SEED')),
        Required('quantity'): All(int, )
    }
)
