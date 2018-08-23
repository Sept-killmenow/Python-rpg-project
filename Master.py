# UI
Start = 0
Exit = 0
ui = '='

# Class Variables
xp = 0
currency = 100
health = 0
armor = 0
mobility = 0


# Input references
Class = ''
choice = ''

# Inventory
weapons = []
potions = ['Small Health Potion', 'Small Health Potion', 'Small Health Potion']
misc = []
inventory = weapons + potions + misc
inventory_count = len(inventory)


def inventory_counted():
    inventory_count = len(inventory)
# Weapons

# Potions


def lhp():
    if health <= 100:
        health = health + 100
    if health >= 100:
        health = 100


# Misc


def menu():

        print(ui*30)
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
        print(
            "            Exit"
        )
        print()
        print(ui*30)


def loopmenu():

    while Exit != 1:
        menu()
        nav = input("...")
        if nav == 'start':
            break

        elif nav == 'Start':
            break

        elif nav == 'Instructions':
            instructions()
            break

        elif nav == 'instructions':
            instructions()
            break


def instructions():  # Loop that displays the games instructions until the user types Back
    while Exit != 1:
        print()
        print(ui*30)
        print()
        print(
            "1. To navigate menus and UI you shall type out what the option is not click on it"
        )
        print(
            "2. Try not to cheat thanks"
        )
        print(
            "3. Have fun"
        )
        print()
        print(ui*30)
        print('If you would like to return type back')
        back = input('...')
        if back == 'back':
            loopmenu()
            break

        elif back == 'Back':
            loopmenu()
            break
        print()
        print()
        print()


def player_stats():

    print(ui * 15, player.lstrip(), ui * 15)
    print("Health", health)
    print("Armor", armor)
    print("Mobility", mobility)
    count = len(player)
    print(ui * count + ui * 32)


def townhall():
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
        if choice == '1':
            shop()
            break
        elif choice == '2':
            townhall()
            break


def woke_loop():
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
    print('============================', inventory_count,'/25', '======')


def shop():
    inventory()
    print()
    print()
    print('=============== Shop ===============')
    print('How do you do stranger would you like to buy anything?')
    print('You have', currency, 'dollars')
    print('Weapons:')
    print('Potions:')
    print('Misc:')
    print('====================================')
    print('If you would like to buy something')
    print('Or if you would like to return to the Town square type back')
    while Exit != 1:
        choice = input('...')
        if choice == 'back':
            woke_loop()
            break
        if choice == 'Back':
            woke_loop()
            break


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
    if Class == 'Warrior':
        health = 125
        armor = 25
        mobility = 15
        weapons.append('Iron Sword')

        break
    elif Class == 'warrior':
        health = 125
        armor = 25
        mobility = 15
        weapons.append('Iron Sword')
        break
    elif Class == 'Tank':
        health = 200
        armor = 50
        mobility = 5
        weapons.append('Dull Iron Sword')
        break
    elif Class == 'tank':
        health = 200
        armor = 50
        mobility = 5
        weapons.append('Dull Iron Sword')
        break
    elif Class == 'Scout':
        health = 80
        armor = 0
        mobility = 30
        weapons.append('Iron Dagger')
        weapons.append('Short Bow')
        misc.append('Arrow'*5)
        break
    elif Class == 'scout':
        health = 80
        armor = 0
        mobility = 35
        weapons.append('Iron Dagger')
        weapons.append('Short Bow')
        break
    elif Class == 'Test':
        health = 200
        armor = 100
        mobility = 100
        weapons.append('Iron Dagger')
        weapons.append('Short Bow')
        break
player_stats()
woke()
