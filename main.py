import requests
from pprint import pprint

response = requests.get('https://akabab.github.io/superhero-api/api/all.json')

heroes = ['Hulk', 'Captain America', 'Thanos']

heroes_dict = {}
for hero in response.json():
    if hero.get('name') in heroes:
        heroes_dict[hero.get('name')] = hero.get('powerstats').get('intelligence')

max = 0
for key, val in heroes_dict.items():
    if val > max:
        max = val
        key_max = key

print(f'Наивысший интеллект у героя: {key_max} - {heroes_dict.get(key_max)}')

