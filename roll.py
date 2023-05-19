import random
import rarities

def roll(bulk_roll):
    result = random.choices(rarities.keys, rarities.values, k=bulk_roll)
    return result