'#UI'
nav = ''
Start = 0
Exit = 0
ui = '='

#Class Variables
xp = 0
currency = 100
health = 0
armor = 0
mobility = 0

#Text references
back = 'back'
Back = 'Back'
backI = ''
Instructions = ('Instructions')
instructions = ('instructions')
Class= ''

#loop variables
loopClass = 0
ClassCheck = ''


def menu():
        backI = '0'
        print(ui*20)
        print()
        print(
            "      ARA RPG   "
        )
        print()
        print(ui*20)
        print()
        print(
            "       Start    "
        )
        print(
            "    Instructions "
        )
        print(
            "       Exit"
        )
        print()
        print(ui*20)

def loopMenu():

    while Exit != 1:
        menu()
        nav = input("...")
        if nav == 'start':
            break

        elif nav == 'Start':
            break


        if nav == 'Instructions':
            InstructionS()
            break

        elif nav == 'instructions':
            InstructionS()
            break

def InstructionS():
    while Exit != 1:
        print()
        print(ui*20)
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
        print(ui*20)
        print('If you would like to return type back')
        backI = input('...')
        if backI == back:
            loopMenu()
            break

        elif backI == Back:
            loopMenu()
            break
        print()
        print()
        print()

def playerStats():

    print (ui * 10, player.lstrip(), ui * 10)
    print("Health", health)
    print("Armor", armor)
    print("Mobility", mobility)
    count = len(player)
    print (ui * count + ui * 22)




loopMenu()
player = input(
    "Please enter your name..."
)
while Exit != 1:
    print(ui * 26)
    print(
        "  Please Select a class"
    )
    print(
        " [Warrior] [Tank] [Scout]"
    )
    print(ui * 26)
    Class = input("...")
    if Class == 'Warrior':
        health = 125
        armor = 25
        mobility = 15
        break
    if Class == 'warrior':
        health = 125
        armor = 25
        mobility = 15
        break
    if Class == 'Tank':
        health = 200
        armor = 50
        mobility = 5
        break
    if Class == 'tank':
        health = 200
        armor = 50
        mobility = 5
        break
    if Class == 'Scout':
        health = 80
        armor = 0
        mobility = 30
        break
    if Class == 'scout':
        health = 80
        armor = 0
        mobility = 35
        break
    if Class == 'Test':
        health = 200
        armor = 100
        mobility = 100
        break
playerStats()
print()
print(ui*25)
print()
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
while Exit != 1:
    choice = input('...')
    print()
    print(ui*25)
    if choice == '1':
        print('jeff')
        #Market()
        break
    if choice == '2':
        print('jeff')
        #townHall()
        break




