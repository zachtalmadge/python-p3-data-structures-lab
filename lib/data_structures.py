spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    # for loop

#     result = []
# 
#     for food in spicy_foods:
#         result.append(food['name'])
#         
#     return result

    # list comprehension

    return [food['name'] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        rating = "🌶️" * food['heat_level']
        print( f"{food['name']} ({food['cuisine']}) | Heat Level: {rating}" )

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            print(food)

def get_average_heat_level(spicy_foods):
    total = 0

    for food in spicy_foods:
        total += food['heat_level']

    average = total / len(spicy_foods)

    return average

def create_spicy_food(spicy_foods, spicy_food):
    return [*spicy_foods, spicy_food]
