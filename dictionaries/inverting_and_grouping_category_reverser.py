# Goal: Practice the logic of inverting a dictionary where values are lists (like the code you were just reviewing) to group items by their shared property.

"""
Task: Write a function group_by_cuisine(restaurants) that takes 
a dictionary where keys are restaurant names and values are their 
cuisine type (e.g., 'Italian'). Invert this to create a new dictionary 
where keys are cuisine types and values are lists of restaurant names.
"""

from collections import defaultdict

restaurant_cuisines = {
    'The Golden Spoon': 'American Comfort',
    'Chai Palace': 'Indian',
    'El Fuego': 'Mexican',
    'Bistro Lumière': 'French',
    'Sushi Zen': 'Japanese',
    'Mama Mia Pizzeria': 'Italian',
    'The Smokehouse': 'Barbecue',
    'Pho Saigon': 'Vietnamese',
    'The Green Bowl': 'Vegetarian',
    'Café Del Sol': 'Spanish',
    'Tandoori Nights': 'Indian',          # Repeat: Indian
    'La Trattoria': 'Italian',             # Repeat: Italian
    'The Waffle Stop': 'American Diner',
    'Kimchi House': 'Korean',
    'Taco Fiesta': 'Mexican',               # Repeat: Mexican
    'The Burger Joint': 'American Comfort', # Repeat: American Comfort
    'Wok Master': 'Chinese',
    'Curry Spot': 'Indian',                 # Repeat: Indian
    'Pasta Fresca': 'Italian',              # Repeat: Italian
    'Taqueria Grande': 'Mexican'            # Repeat: Mexican
}


def group_by_cuisine(restaurants):
	grouped_restaurants = defaultdict(list)

	for restaurant, cuisine in restaurants.items():
		grouped_restaurants[cuisine].append(restaurant)

	# Convert back to a standard dict before returning
	return dict(grouped_restaurants)

print(group_by_cuisine(restaurant_cuisines))