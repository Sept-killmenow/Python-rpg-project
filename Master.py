import os
from time import sleep
import random
# UI
Start = 0
Exit = 0
ui = '='
currency = 150


class BColors:
    # Regular Colors
    Black = "\033[0;30m"  # Black
    Red = "\033[0;31m"  # Red
    Green = "\033[92m"  # Green
    Yellow = "\033[0;33m"  # Yellow
    Blue = "\033[0;34m"  # Blue
    Purple = "\033[0;35m"  # Purple
    Cyan = "\033[0;36m"  # Cyan
    White = "\033[0;37m"  # White

    # Underline
    UBlack = "\033[4;30m"  # Black
    URed = "\033[4;31m"  # Red
    UGreen = "\033[4;32m"  # Green
    UYellow = "\033[4;33m"  # Yellow
    UBlue = "\033[4;34m"  # Blue
    UPurple = "\033[4;35m"  # Purple
    UCyan = '\033[4;36m'  # Cyan
    UWhite = "\033[4;37m"  # White

    # Background
    On_Black = "\033[40m"  # Black
    On_Red = "\033[41m"  # Red
    On_Green = "\033[42m"  # Green
    On_Yellow = "\033[43m"  # Yellow
    On_Blue = "\033[44m"  # Blue
    On_Purple = "\033[45m"  # Purple
    On_Cyan = "\033[46m"  # Cyan
    On_White = "\033[47m"  # White


# Class Variables
xp = 0

health = 0
armor = 0
mobility = 0


# Input references
Class = ''
choice = ''

# Inventory
weapons_buy = [
    '1. Sharpened Iron Sword $150', '2. Iron Axe $200', '3. Sharpened Iron Axe $250', '4. Steel Sword $550',
    '5. Sharpened Steel Sword $750', '6. Steel Axe $1000', '7. Sharpened Steel Axe $1500',
    '8. Obsidian Strong Sword $2500', '9. Obsidian Rapier $2500', '10.Obsidian Axe $2500'
]
weapons_buy_scout = [
    '1. Sharpened Iron Dagger $150', '2. Iron Short Sword $200', '3. Steel Dagger $400',
    '4. Sharpened Steel Dagger $650', '5. Steel Short Sword $500', '6. Sharpened Steel Short Sword $750',
    '7. Obsidian Dagger $2000', '8. Obsidian Rapier $2000'
]
potions_buy = [
    '11. Small Health Potion $75', '12. Medium Health Potion $125', '13. Large Health Potion $200',
    '14. Mobility Buff Vial $750', '15. Health Buff Vial $750'
]
potions_buy_scout = [
    '9. Small Health Potion $75', '10. Medium Health Potion $125', '11. Large Health Potion $200',
    '12. Mobility Buff Vial $750', '13. Health Buff Vial $750'
]
misc_buy = []
misc_buy_scout = []
weapons = []
potions = ['Small Health Potion', 'Small Health Potion', 'Small Health Potion']
misc = []
inventory = weapons + potions + misc
inventory_count = len(inventory)

# Equip
Equipped = []

# Weapons


# Potions


# Misc


def menu():

        print(BColors.Green + ui*30)
        print()
        print(
            "           ARA RPG   "
        )
        print()
        print(ui*30)
        print()
        print(
            "            Start    "
        )
        print(
            "         Instructions "
        )
        print()
        print(ui*30)


def loopmenu():

    while Exit != 1:
        menu()
        nav = input("...")
        if nav == 'start' or nav == 'Start':  # If Start is typed into the input loop will break and continue
            break

        elif nav == 'Instructions' or nav == 'instructions':  # If Instructions is typed into the input it will run
            instructions()  # The Instructions function
            break


def instructions():  # Loop that displays the games instructions until the user types Back
    global choice
    print()
    print('\n', ui * 30, '\n\n', '1. To navigate menus and UI \n you shall type out what the \n option is not click on'
                                 ' it\n\n 2. Try not to cheat thanks\n\n 3. Type Inventory at any\n input to open the'
                                 ' inventory\n\n', ui * 30, '\n If you would like to return\n type Back')
    while Exit != 1:
        choice = input(' ...')
        if choice == 'Back' or choice == 'back':
            loopmenu()
        break


def player_stats():
    print(ui * 15, player.lstrip(), ui * 15)
    print("Health", health)
    print("Armor", armor)
    print("Mobility", mobility)
    count = len(player)
    print(ui * count + ui * 32)


def townhall():
    global choice
    print(ui*30)
    print()
    print(
        'You enter the town hall and'
        )
    print(
        ' see a notice board and a '
        )
    print(
        'Receptionist. what do you do:'
        )
    print()
    print('1. Check the notice board')
    print('2. Talk to the Receptionist')
    print('3. Go back to the Town square')
    print(ui*30)
    print()
    print('Use your number keys to choose')
    choice = input('')
    while Exit != 1:
        if choice == '3':
            woke_loop()
            break


def woke():
    global choice
    print(
        'You wake up in the middle '

    )
    print(
        'of a town square, surrounded'
    )
    print(
        'by a large market a Town hall.'
    )
    print()
    print('Where would you like to go:')
    print('1. The Market')
    print('2. The Town Hall')
    print()
    print('Use your number keys to choose')
    while Exit != 1:  # Choices from Woke() loop
        choice = input('...')
        print()
        if choice == '1' or choice == 'market':
            shop()
            break
        elif choice == '2':
            townhall()
            break


def woke_loop():
    global choice
    print('You walk back to the Town square')
    print('Where would you like to go now:')
    print('1. The Market')
    print('2. The Town Hall')
    print()
    print('Use your number keys to choose')
    while Exit != 1:  # Choices from Woke() loop
        choice = input('...')
        print()
        if choice == '1':
            shop()
            break
        elif choice == '2':
            townhall()
            break


def inventory():
    global inventory, inventory_count
    print('=============== Inventory ===============')
    print('Weapons:')
    for weapon in weapons:
        print(weapon)
    print('Potions:')
    for potion in potions:
        print(potion)
    print('Misc:')
    for other in misc:
        print(other)
    print('============================', inventory_count, '/25', '======')


def shop():
    global weapon_buy, weapon_buy_scout
    inventory()
    print()
    print()
    print('=============== Shop ===============')
    print('How do you do stranger would you like to buy anything?')
    print('You have', currency, 'dollars')
    print('Weapons:')
    if Class == 'Tank' or Class == 'tank' or Class == 'Warrior' or Class == 'warrior':
        for weapons_b in weapons_buy:
            print(weapons_b)
    if Class == 'Scout' or Class == 'scout':
        for weapons_bs in weapons_buy_scout:
            print(weapons_bs)

    if Class == 'Warrior' or Class == 'warrior' or Class == 'Tank' or Class == 'tank':
        for potion_buy in potions_buy:
            print(potion_buy)
    print('Misc:')
    for miscs_buy in misc_buy:
        print(miscs_buy)
    print('====================================')
    print('If you would like to buy something')
    print('Or if you would like to return to the Town square type back')
    buy()


def buy():
    global choice
    global currency
    while Exit != 1:
        choice = input('...')
        if choice == 'back' or choice == 'back':
            woke_loop()
            break
        elif choice == '1' and Class == 'Warrior' or Class == 'warrior' or Class == 'Tank' or Class == 'tank':
            if currency >= 150:
                weapons.append('Sharpened Iron Sword')
                currency = currency - 150
                print('You have', currency, 'dollars remaining')
                print('You now own a Sharpened Iron Sword')
                print()
                woke_loop()

        elif choice == '2' and Class == 'Warrior' or Class == 'warrior' or Class == 'Tank' or Class == 'tank':
            if currency >= 200:
                weapons.append('Iron Axe')
                currency = currency - 200
                print('You have', currency, 'dollars remaining')
                print('You now own a Iron Axe')
                print()
                woke_loop()


loopmenu()
player = input(
    "Please enter your name..."
)
while Exit != 1:
    print(ui * 30)
    print(
        "  Please Select a class"
    )
    print(
        " [Warrior] [Tank] [Scout]"
    )
    print(ui * 30)
    Class = input("...")
    if Class == 'Warrior' or Class == 'warrior':
        health = 125
        armor = 25
        mobility = 15
        weapons.append('Iron Sword')

        break
    elif Class == 'Tank' or Class == 'tank':
        health = 200
        armor = 50
        mobility = 5
        weapons.append('Dull Iron Sword')
        break
    elif Class == 'Scout' or Class == 'scout':
        health = 80
        armor = 0
        mobility = 30
        weapons.append('Iron Dagger')
        weapons.append('Short Bow')
        misc.append('Arrow'*5)
        break
    elif Class == 'Test' or Class == 'test':
        health = 200
        armor = 100
        mobility = 100
        weapons.append('Iron Dagger')
        weapons.append('Short Bow')
        break
player_stats()
woke()
