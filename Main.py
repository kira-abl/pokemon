import requests
import json

def get_list():
    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=3&offset=0")
    data = response.json()
    #print(data)
    return data

def get_random_number():
    from random import randint
    random_number = randint(0, 2)
    return random_number

def select_pokemon(data, number):
    basic_info = data['results'][number]
    name = basic_info['name']
    url  = basic_info['url']
    print(name, url, basic_info)
    return name, url, basic_info

def get_pokemon_info(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)
    data = response.json()
    cries = data['cries']
    weight = data['weight']
    experience = data['base_experience']
    return cries, weight, experience

def read_file():
    try:
        with open("pokemon_list.json", "r") as file:
            data_in_json = json.load(file)
    except FileNotFoundError:
        data_in_json = {}
    return data_in_json

def update_file(item):
    with open("pokemon_list.json", "w") as file:
        json.dump(item, file, indent = 4)

def retrieve_details_and_update(name, data):
    if not data or not name in data:
        pokemon_details = get_pokemon_info(name)
        data[name] = {
        "cries": pokemon_details[0],
        "experience": pokemon_details[1],
        "weight": pokemon_details[2]
    }
        answer = data[name]
        print("Answer from API")
        update_file(data)
    else:
        answer = data[name]
        print("Answer from JSON")
    return answer

def display_to_user(name, info):
    number_of_cries = len(info['cries'])
    print(f"Hello, my name is {name.capitalize()}.")
    print(f"My weight is {info['weight']}.")
    print(f"My level of experience is {info['experience']}.")
    print(f"I have {number_of_cries} cries:\nGet my latest cry here: {info['cries']['latest']}.\nGet my legacy cry here: {info['cries']['legacy']}.")

def main():
    data = get_list()
    number = get_random_number()
    pokemon_basics = select_pokemon(data, number)
    data_json = read_file()
    pokemon_full_data = retrieve_details_and_update(pokemon_basics[0], data_json)
    display_to_user(pokemon_basics[0], pokemon_full_data)

main()
