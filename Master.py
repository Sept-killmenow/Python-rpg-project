from time import sleep
import pickle
import random
Start = 0
Exit = 0
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


# Class Variables
xp = 0
level = 1
nextlvl = 750
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
potions_buy = [
    '11. Small Health Potion $75', '12. Medium Health Potion $125', '13. Large Health Potion $200',
    '14. Mobility Buff Vial $750', '15. Health Buff Vial $750'
]
misc_buy = [
    '16. Explosives x1 $250'
]
weapons = []
potions = ['Small Health Potion', 'Small Health Potion', 'Small Health Potion']
misc = ['']
inventory = weapons + potions + misc
inventory_count = len(inventory)

# Equip
Equipped = []


# Weapons


# Potions


# Misc
def leveling():
    global level, xp, nextlvl
    while xp >= nextlvl:
        level += 1
        xp = xp - nextlvl
        nextlvl = round(nextlvl * 1.5)


def inventory_drop_item():
    print('d')


def clear():
    print('\n'*40)


def menu():
        clear()
        print(BColors.Green + '[=============================================]')
        print()
        print("               Ara: The Epic Tale    ")
        print()
        print('[=============================================]')
        print('\n', '                 Instructions','\n\n', '1. To navigate menus and UI you shall type\n '
                                                             'out what the option is. Do not click on it'
                            '\n\n 2. Try not to cheat thanks\n\n 3. Type Inventory at any\n input to open the'
                            ' inventory\n\n','4. Type Start to begin', '\n\n', '5. To drop a item type Drop [item name]\n\n',
              '[=============================================]')
        print()


def loopmenu():
    global choice
    while Exit != 1:
        menu()
        choice = input("  ...")
        clear()
        if choice == 'start' or choice == 'Start':  # If Start is typed into the input loop will break and continue
            break


def player_stats():
    clear()
    clear()
    print('[================ Player Stats ===============]',)
    print('Level:', level)
    print("Health", health)
    print("Armor", armor)
    print("Mobility", mobility)
    print('[=============================================]')


def player_stats_callback():
    print('[================ Player Stats ===============]',)
    print('Level:', level)
    print("Health", health)
    print("Armor", armor)
    print("Mobility", mobility)
    print('[=============================================]')


def townhall():
    global choice
    clear()
    print('[=============================================]')
    print()
    print(
        'You stand at the town hall entrance and'
        )
    print(
        ' see a notice board and a Receptionist. '
        )
    print(
        'what do you do.'
        )
    print()
    print('[================== CHOICES ==================]')
    print()
    print('  1. Check the notice board')
    print('  2. Talk to the Receptionist')
    print('  3. Go Back to the Town square')
    print()
    print('[=============================================]')
    print()
    print('Use your number keys to choose')
    choice = input('...')
    while Exit != 1:
        if choice == '1':
            clear()
            notice()
            break
        if choice == '2':
            clear()
            receptionist()
            break
        if choice == '3':
            clear()
            woke_loop()
            break


def notice():
    global choice
    clear()
    print('[=============================================]')
    print()
    print('              TOWN NOTICE BOARD')
    print()
    print('      [The Valkyrie]  [Hydra of Lerna]')
    print('     [Polyphemus The Cyclops] [Drakontos]')
    print('           [Explore the wilderness]')
    print()
    print('[=============================================]')
    print()
    print('[================== CHOICES ==================]')
    print()
    print('  1. Attempt to Banish the Valkyrie')
    print('  2. Try to Slay The Hydra of Lerna')
    print('  3. Go off and Destroy Polyphemus The Cyclops')
    print('  4. Try and Behead the feared Drakontos')
    print('  5. Explore the wilderness')
    print('  6. Walk back to the entrance ')
    print()
    print('[=============================================]')
    print()
    print('Use your number keys to choose')
    choice = input('...')
    while Exit != 1:
        if choice == '6' or choice == 'Back' or choice == 'back':
            clear()
            townhall()
            break
        repeated()


def receptionist():
    global choice
    clear()
    print('[=============================================]')
    print()
    print('  Hey there what would you like to know?')
    print()
    print('[=============================================]')
    print()
    print('[================== CHOICES ==================]')
    print()
    print('  1. Where am i?')
    print('  2. What can i do around here?')
    print('  3. Im fine thank you.')
    print()
    print('[=============================================]')
    print()
    print('Use your number keys to choose')
    choice = input('...')
    while Exit != 1:
        if choice == '1':
            clear()
            re_reply1()
        if choice == '2':
            clear()
            re_reply2()
        if choice == '3':
            clear()
            woke_loop()
            break
    repeated()


def re_reply1():
    print('[=============================================]')
    print()
    print('  Oh, you are in sanctuary.')
    sleep(1)
    print('  A safe place for all... atleast for now.')
    sleep(1.5)
    print('  Recently we have been attacked by creatures')
    sleep(1.5)
    print('  if you could, please take some time to look')
    print('  at the notice board and hunt down these \n  animals.')
    print()
    print('[=============================================]')
    sleep(10)
    townhall()


def re_reply2():
    print('[=============================================]')
    print()
    print('  Well you could start by taking a look')
    print('  at the notice board.')
    print()
    print('  We would appreciate any help you are able to')
    print('  give.')
    print()
    print('[=============================================]')
    sleep(8)
    townhall()


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
    print('[================== CHOICES ==================]')
    print()
    print('Where would you like to go:')
    print('1. The Market')
    print('2. The Town Hall')
    print('3. Inventory')
    print()
    print('[=============================================]')
    while Exit != 1:  # Choices from Woke() loop
        choice = input('...')
        print()
        if choice == '1' or choice == 'market':
            shop()
            break
        elif choice == '2':
            townhall()
            break
        elif choice == 'Inventory' or choice == 'inventory' or choice == '3':
            inventory()
        repeated()


def woke_loop():
    global choice
    clear()
    print('[=============================================]')
    print()
    print('You walk back to the Town square')
    print()
    print('[================== CHOICES ==================]')
    print()
    print('Where would you like to go:')
    print('1. The Market')
    print('2. The Town Hall')
    print('3. Inventory')
    print()
    print('[=============================================]')
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
        elif choice == 'Inventory' or choice == 'inventory' or choice == '3':
            inventory()
        repeated()


def inventory():
    global inventory_count, xp
    print()
    print()
    print()
    print()
    print()
    print('=============== Inventory ===============]')
    print('Weapons:')
    for weapon in weapons:
        print(weapon)
    print('Potions:')
    for potion in potions:
        print(potion)
    print('Misc:')
    for other in misc:
        print(other)
    print('[===========================', inventory_count, '/ 25', '======]')
    repeated()


def inventory_use_item():
    global health, mobility
    if choice == 'use small health potion' or choice == 'use Small Health Potion' \
            or choice == 'Use Small Health Potion' or choice == 'Use small health potion':
        if 'Small Health Potion' in potions:
            if health >= 200:
                print('You cannot use this now')
            if health < 200:
                health = health + 25
                potions.remove('Small Health Potion')
                print('You used a Small health potion')
        else:
            print('You do not have a Small health potion')

    if choice == 'use medium health potion' or choice == 'use medium Health Potion' \
            or choice == 'Use Medium Health Potion' or choice == 'Use medium health potion':
        if 'Medium Health Potion' in potions:
            if health >= 200:
                print('You cannot use this now')
            if health < 200:
                health = health + 100
                potions.remove('Medium Health Potion')
                print('You used a Medium health potion')
        else:
            print('You do not have a Medium health potion')

    if choice == 'use Large health potion' or choice == 'use Large Health Potion' \
            or choice == 'Use Large Health Potion' or choice == 'Use Large health potion':
        if 'Large Health Potion' in potions:
            if health >= 200:
                print('You cannot use this now')
            if health < 200:
                health = health + 200
                potions.remove('Large Health Potion')
                print('You used a Large health potion')
            if health > 200:
                health = 200
        else:
            print('You do not have a Large health potion')

    if choice == 'use Mobility Buff Vial' or choice == 'use Mobility Buff Vial' \
            or choice == 'Use mobility buff vial' or choice == 'Use mobility buff vial':
        if 'Mobility Buff Vial' in potions:
            if mobility >= 75:
                print('You cannot use this now')
            elif mobility < 75:
                mobility = mobility + 5
                potions.remove('Mobility Buff Vial')
                print('You used a Mobility Buff Vial')
        else:
            print('You do not have a Mobility Buff Vial')


def shop():
    clear()
    print()
    print()

    print('[=================== Shop ====================]')
    print('How do you do stranger would '
          '\nyou like to browse my wares?')
    print('You have', currency, 'dollars')
    print('Weapons:')
    if Class == 'Tank' or Class == 'tank' \
            or Class == 'Warrior' or Class == 'warrior' or Class == 'Scout' or Class == 'scout':
        for weapons_b in weapons_buy:
            print(weapons_b)

    if Class == 'Warrior' or Class == 'warrior' \
            or Class == 'Tank' or Class == 'tank' or Class == 'Scout' or Class == 'scout':
        for potion_buy in potions_buy:
            print(potion_buy)
    print('Misc:')
    for miscs_buy in misc_buy:
        print(miscs_buy)
    print('[=============================================]')
    print('If you would like to buy something')
    print('Or if you would like to return'
          '\nto the Town square type Back')
    buy()
    repeated()


def buy():
    global choice
    global currency
    while Exit != 1:
        choice = input('...')
        if choice == 'back' or choice == 'back':
            woke_loop()
            break
        elif choice == '1':
            if currency >= 150:
                weapons.append('Sharpened Iron Sword')
                currency -= 150
                clear()
                woke_loop()

        elif choice == '2':
            if currency >= 200:
                weapons.append('Iron Axe')
                currency -= 200
                clear()
                woke_loop()
        elif choice == '3':
            if currency >= 250:
                weapons.append('Sharpened Iron Axe')
                currency -= 250
                clear()
                woke_loop()
        elif choice == '4':
            if currency >= 550:
                weapons.append('Steel Sword')
                currency -= 550
                clear()
                woke_loop()
        elif choice == '5':
            if currency >= 750:
                weapons.append('Sharpened Steel Sword')
                currency -= 750
                clear()
                woke_loop()
        elif choice == '6':
            if currency >= 1000:
                weapons.append('Steel Axe')
                currency -= 1000
                clear()
                woke_loop()
        elif choice == '7':
            if currency >= 1500:
                weapons.append('Sharpened Steel Axe')
                currency -= 1500
                clear()
                woke_loop()
        elif choice == '8':
            if currency >= 2500:
                weapons.append('Obsidian Strong Sword')
                currency -= 2500
                clear()
                woke_loop()
        elif choice == '9':
            if currency >= 2500:
                weapons.append('Obsidian Strong Sword')
                currency -= 2500
                clear()
                woke_loop()
        elif choice == '10':
            if currency >= 2500:
                weapons.append('Obsidian Axe')
                currency -= 2500
                clear()
                woke_loop()
        elif choice == '11':
            if currency >= 75:
                potions.append('Small Health Potion')
                currency -= 75
                clear()
                woke_loop()
        elif choice == '12':
            if currency >= 125:
                potions.append('Medium Health Potion')
                currency -= 125
                clear()
                woke_loop()
        elif choice == '13':
            if currency >= 2500:
                potions.append('Large Health Potion')
                currency -= 2500
                clear()
                woke_loop()
        elif choice == '14':
            if currency >= 750:
                potions.append('Mobility Buff Vial')
                currency -= 750
                clear()
                woke_loop()
        elif choice == '15':
            if currency >= 750:
                potions.append('Health Buff Vial')
                currency -= 750
                clear()
                woke_loop()
        elif choice == '16':
            if currency >= 250:
                potions.append('Explosives')
                currency -= 250
                clear()
                woke_loop()
        elif choice == 'Inventory' or choice == 'inventory':
            inventory()


def repeated():
    global choice
    leveling()
    inventory_use_item()
    inventory_drop_item()
    if choice == 'Inventory' or choice == 'inventory':
        inventory()
    elif choice == 'Stats' or choice == 'stats':
        player_stats_callback()


loopmenu()
print('[=============================================]')
print()
player = input(
    "Please enter your name..."
)
print()
while Exit != 1:
    print('[=============================================]')
    print()
    print(
        "            Please Select a class"
    )
    print(
        "           [Warrior] [Tank] [Scout]"
    )
    print()
    print('Warrior: For people who like to play it safe')
    print()
    print('Tank: Has more health and armour but does less\n '
          'damage.')
    print()
    print('Scout: Has less health and does less damage \n'
          'but is more mobile')
    print()
    print('[=============================================]')
    print()
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
