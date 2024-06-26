from datetime import datetime


def get_days_left(plant):
    now = datetime.now()
    last_watered = plant.last_watered
    if last_watered is None:
        return plant.waterDate
    days_passed = (now - last_watered).days
    days_left = plant.waterDate - days_passed
    return days_left
