from api.models.farm import Plant, UserPlant

plant_basic_ser = [
    Plant.id,
    Plant.name,
    Plant.category,
    Plant.created_at,
    Plant.updated_at,
    Plant.needs,
]

user_plant_basic_ser = [
    UserPlant.plant_id,
    UserPlant.active_flag,
    UserPlant.water,
    UserPlant.fertilizer,
    UserPlant.pesticide,
    UserPlant.price,
    UserPlant.harvest_at,
    UserPlant.status,
    UserPlant.image,
    UserPlant.created_at,
    Plant.name,
    Plant.category,
]
