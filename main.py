#libs
import random
import rarities
import roll
import keyboard
import time
import os
import prices

#vars
roll_cooldown = 1
bulk_roll = 1
current_rarity = 'Easy Cube'
cash = 0
vers = 'ALPHA'

#funcs
def shop():
    print('Welcome to the shop!')
    print('You have ' + str(roll_cooldown) + ' seconds of roll cooldown.')
    print('You have ' + str(bulk_roll) + ' rolls per bulk roll.')
    print('You have ' + current_rarity + ' as your current rarity.')
    print('Press 1 to upgrade your roll cooldown.')
    print('Press 2 to upgrade your bulk roll.')
    print('Press 3 to sell your current rarity.')
    print('You currently have ' + str(cash) + ' cash.')

def controls():
    print('[R] - Roll, [S] - Shop, [Q] - Quit, [H] - Stats, [G] - Sell')

def cls():
    os.system('cls')

def version():
    global vers
    print('Version - ' + vers)

def credits():
    print('Made by - v4nixd')
    print('Github - https://github.com/v4nixd')
    print('Discord - v4nixd#0001')
    print('Made in - Python 3.11.1')
    print('Made using - Visual Studio Code')
    print('Made in - 2023')

def main():
    cls()
    print('Welcome to Cube Simulator!')
    controls()
    print('[C] - Credits')
    print('[WARNING] This game is in early development, so there may be bugs!]')
    version()
    while True:
        global current_rarity
        global cash
        if keyboard.is_pressed('r'):
            time.sleep(roll_cooldown)
            result = roll.roll(bulk_roll)
            current_rarity = result[0]
            cls()
            print('You rolled a ' + result[0])
            controls()
        elif keyboard.is_pressed('s'):
            cls()
            shop()
            controls()
        elif keyboard.is_pressed('q'):
            cls()
            print('Goodbye!')
            time.sleep(1)
            break
        elif keyboard.is_pressed('h'):
            cls()
            print('You have ' + str(roll_cooldown) + ' seconds of roll cooldown.')
            print('You have ' + str(bulk_roll) + ' rolls per bulk roll.')
            print('You have ' + current_rarity + ' as your current rarity.')
            print('You currently have ' + str(cash) + ' cash.')
            controls()
        elif keyboard.is_pressed('c'):
            cls()
            credits()
            controls()
        elif keyboard.is_pressed('g'):
            cls()
            
main()