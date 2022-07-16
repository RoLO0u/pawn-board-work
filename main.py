import pygame
import json
import sys

from code.game import Game

with open("settings.json") as file:
    settings = json.load(file)

def main():
    game = Game(settings)
    game.run()

if __name__ == "__main__":
    main()