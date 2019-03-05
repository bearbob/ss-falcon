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
    game = {}
    game["machines"] = machines
    game["crew"] = [create_character()]
    game["id"] = game_id
    game["created"] = time.time()

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
