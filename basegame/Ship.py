#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random, time
from random import randint

gameCollector = []
maleNames = [
    "Alex",
    "Bob",
    "Charles",
    "Davis",
    "Eric",
    "Fergus"
]
femaleNames = [
    "Alice",
    "Beata",
    "Clementine",
    "Donna",
    "Elisa",
    "Fiona"
]


def create_new_game(game_id):
    machines = {
        "power": 0,
        "health": 0,
        "water": 0,
        "food": 0
    }
    # set the starting rations
    cache = {
        "water": randint(1, 10),
        "food": randint(1, 7)
    }
    game = {}
    game["machines"] = machines
    game["crew"] = [create_character()]
    game["id"] = game_id
    game["created"] = time.time()
    game["cache"] = cache
    game["days"] = 0

    # check if a game with this ID already exists
    if get_game(game_id) is not None:
        gameCollector.remove(get_game(game_id))
    gameCollector.append(game)
    # TODO create game intro message
    return game


def get_game(game_id):
    for g in gameCollector:
        if g["id"] == game_id:
            return g
    print("No game found with given ID: " + game_id)
    return None


def create_character():
    gender = randint(0, 1)
    character = {
        "gender": gender,
        "age": randint(20, 40),
        "name": get_random_name(gender),
        "water_needed": 0,
        "food_needed": 0
    }
    print("Created character "+character["name"])
    return character


def get_random_name(gender):
    random.shuffle(maleNames)
    random.shuffle(femaleNames)
    if gender == 0:
        return maleNames.pop()
    else:
        return femaleNames.pop()


def pass_day(game_id):
    game = get_game(game_id)
    game["days"] += 1
    text = "The day has passend. Day "+str(game["days"])+" has started."
    for char in game["crew"]:
        if game["cache"]["food"] >= 1:
            if char["food_needed"] > 0:
                char["food_needed"] -= 1
            game["cache"]["food"] -= 1
        else:
            char["food_needed"] = char["food_needed"] + 1
        if game["cache"]["water"] >= 1:
            if char["water_needed"] > 0:
                char["water_needed"] -= 1
            game["cache"]["water"] -= 1
        else:
            char["water_needed"] += 1
        # TODO kill the character if food_needed or water_needed pass the limit
    return text


def explore(game_id):
    game = get_game(game_id)
    # get a random element from the exploration table
