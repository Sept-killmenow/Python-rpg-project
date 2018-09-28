from time import sleep
import random
from colorama import Fore


# Misc
max_xp = 0
xp_percent = 0
xp_print = ''
next_lvl = 750
health_percent = 0
max_health = 200
health_print_max = 10
health_print = ''
armor_percent = 0
max_armor = 100
armor_check = 0
burn_check = 0
burn_effect = 0
armor_equip = ['None', ]
temp_currency = 0
current_mobility = 0
dungeon = 1
Exit = 0

# Player
level = 0
xp = 0
health = 0
armor = 0
mobility = 0
burn = 0
weapon_equip = []
damage = 0
turn_counter = 0
currency = 150

# Enemy Variables
enemy_name = 'null'
enemy_attacks = []
enemy_quote = []
enemy_health = 0
enemy_xp = 0
enemy_mobility = 0
enemy_armor = 0
enemy_attack = 0
enemy_health_percent = 0
enemy_max_health = 0
enemy_health_print = ''
enemy_health_print_max = 10
enemy_missed = 0
move = ''
x = ''

# dungeon variables
first_loop = 0
first_loop_stop = 0
first_loop_v = 0
enemy_count = 0

# Loot pool
loot1 = ['']
loot2 = ['']
loot3 = ['']
loot4 = ['']

# Input references
Class = ''
choice = ''

# Shop
weapons_buy = [
    Fore.BLACK + '1. Iron Sword $150', '2. Steel Sword $550', '3. Obsidian Strong Sword $2500',
    '4. Obsidian Rapier $2500', '5. Obsidian Axe $2500' + Fore.BLACK
]
weapons_buy_mage = [
    Fore.BLACK + '1. Wooden Wand $550', '2. Wooden Staff $550', '3. Iron Wand $1500',
    '4. Iron Staff $1500', '5. Dark Wand' + Fore.BLACK
]
potions_buy = [
    Fore.BLACK + '6. Small Health Potion $75', '7. Medium Health Potion $125', '8. Large Health Potion $200',
    '9. Mobility Buff Vial $750', '10. Health Buff Vial $750' + Fore.BLACK
]

# Inventory
weapons = ['']
potions = ['Small Health Potion', 'Small Health Potion', 'Small Health Potion']
misc = ['']
inventory = weapons + potions + misc
inventory_count = len(inventory)
interaction_chance = ''


def leveling():
    global level, xp, next_lvl, max_health, health, health_percent, health_print_max
    while xp >= next_lvl:
        level += 1
        xp = 0
        next_lvl = round(next_lvl * 1.5)
        max_health = max_health + 10
        health = max_health
        health_print_max = health_print_max + 1
        print('You have leveled up!')


def health_print():
    global remainingHealth, current_health, health_print_max, health_print
    text_convert = int(max_health / health_print_max)
    current_health = int(health / text_convert)
    remainingHealth = health_print_max - current_health
    health_print = ''.join(['█' for x in range(current_health)])
    health_spacing = ''.join(['█' for x in range(remainingHealth)])
    print('Health:', '[' + Fore.RED + health_print + Fore.WHITE + health_spacing + Fore.BLACK + ']')


def armor_print():
    global x, remaining_armor, armor_print, current_health
    if armor > 1:
        armor_print_max = 10
        text_convert = int(max_armor / armor_print_max)
        current_armor = int(armor / text_convert)
        remaining_armor = armor_print_max - current_armor
        armor_print = ''.join(['█' for x in range(current_armor)])
        armor_spacing = ''.join(['█' for x in range(remaining_armor)])
        print('Armor: ', '[' + Fore.YELLOW + armor_print + Fore.RESET + armor_spacing + Fore.BLACK + ']')
    if armor == 0:
        print(Fore.YELLOW + 'No Armor' + Fore.BLACK)


def inventory_drop_item():
    if choice == 'drop small health potion' or choice == 'drop Small Health Potion' \
            or choice == 'Drop Small Health Potion' or choice == 'Drop small health potion':
        if 'Medium Health Potion' in potions:
            potions.remove('Small Health Potion')
            print('You Dropped a Small Health Potion')
        else:
            print('You do not have this item')

    if choice == 'drop medium health potion' or choice == 'drop Medium Health Potion' \
            or choice == 'Drop Medium Health Potion' or choice == 'Drop medium health potion':
        if 'Medium Health Potion' in potions:
            potions.remove('Medium Health Potion')
            print('You Dropped a Medium Health Potion')
        else:
            print('You do not have this item')

    if choice == 'drop large health potion' or choice == 'drop Large Health Potion' \
            or choice == 'Drop Large Health Potion' or choice == 'Drop large health potion':
        if 'Large Health Potion' in potions:
            potions.remove('Large Health Potion')
            print('You Dropped a Large Health Potion')
        else:
            print('You do not have this item')

    if choice == 'drop Iron Sword' or choice == 'drop Iron Sword' \
            or choice == 'Drop iron sword' or choice == 'Drop Iron sword':
        if 'Iron Sword' in weapons:
            weapons.remove('Iron Sword')
            print('You Dropped a Iron Sword')
        else:
            print('You do not have this item')

    if choice == 'drop large health potion' or choice == 'drop Large Health Potion' \
            or choice == 'Drop Large Health Potion' or choice == 'Drop large health potion':
        potions.remove('Small Health Potion')
        print('You Dropped a Large Health Potion')
    else:
        print('You do not have this item')


def equip():
    global choice, damage, armor, mobility, current_mobility
    if choice == 'equip iron sword' or choice == 'equip iron sword' \
            or choice == 'Equip iron sword' or choice == 'Equip Iron Sword':
        mobility = current_mobility
        damage = 10
        current_mobility = mobility
        mobility = mobility - 1.5
        weapon_equip.append('Iron Sword')
        print('You have equipped a Iron Sword')


def clear():
    print('\n'*80)


def menu():
        clear()
        print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
        print()
        print(Fore.BLACK + "               Ara: The Epic Tale    ")
        print()
        print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
        print(Fore.BLACK + '\n', '                 Instructions', '\n\n', '1. To navigate menus and UI you shall type\n' 
                                                                          'out what the option is. Do not click on it '
                                                                          '\n\n 2. Try not to cheat thanks\n\n 3. Type '
                                                                          'Inventory at any\n '
                                                                          'input to open the inventory\n\n',
              '4. Type Start to begin', '\n\n',
              '5. To drop a item type Drop [item name]\n\n',
              )
        print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
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
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
    print('Level:', level)
    health_print()
    armor_print()
    print('XP:', xp)
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)


def townhall():
    global choice
    clear()
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
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
    print(Fore.BLUE + '█████████████' + Fore.BLACK + ' CHOICES ' + Fore.BLUE
          + '█████████████' + Fore.BLACK)
    print()
    print('  1. Check the notice board')
    print('  2. Talk to the Receptionist')
    print('  3. Go Back to the Town square')
    print()
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
    print()
    print('Use your number keys to choose')
    choice = input('...')
    while Exit != 1:
        if choice == '':
            townhall()
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
    global choice, dungeon
    clear()
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
    print()
    print('              TOWN NOTICE BOARD')
    print()
    print('      [The Valkyrie]  [Hydra of Lerna]')
    print('     [Polyphemus The Cyclops] [Drakontos]')
    print('           [Explore the wilderness]')
    print()
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
    print()
    print(Fore.BLUE + '█████████████' + Fore.BLACK + ' CHOICES ' + Fore.BLUE
          + '█████████████' + Fore.BLACK)
    print()
    print('  1. Attempt to Banish the Valkyrie')
    print('  2. Try to Slay The Hydra of Lerna')
    print('  3. Go off and Destroy Polyphemus The Cyclops')
    print('  4. Try and Behead the feared Drakontos')
    print('  5. Explore the wilderness')
    print('  6. Walk back to the entrance ')
    print()
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
    print()
    print('Use your number keys to choose')
    choice = input('...')
    while Exit != 1:
        if choice == '':
            notice()
        if choice == '1':
            if level >= 0:
                dungeon = 1
                interaction()
                break
        if choice == '2':
            if level < 5:
                print('You must be level 5 to try this quest yet')
            if level >= 5:
                dungeon = 2
                interaction()
                break
        if choice == '6' or choice == 'Back' or choice == 'back':
            clear()
            townhall()
            break
        repeated()


def receptionist():
    global choice
    clear()
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
    print()
    print('  Hey there what would you like to know?     ')
    print()
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
    print()
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
    print()
    print('  1. Where am i?')
    print('  2. What can i do around here?')
    print('  3. Im fine thank you.')
    print()
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
    print()
    print('Use your number keys to choose')
    choice = input('...')
    while Exit != 1:
        if choice == '':
            receptionist()
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
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
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
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
    sleep(5)
    notice()


def re_reply2():
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
    print()
    print('  Well you could start by taking a look')
    print('  at the notice board.')
    print()
    print('  We would appreciate any help you are able to')
    print('  give.')
    print()
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
    sleep(5)
    notice()


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
    print(Fore.BLUE + '█████████████' + Fore.BLACK + ' CHOICES ' + Fore.BLUE
          + '█████████████' + Fore.BLACK)
    print()
    print('Where would you like to go:')
    print('1. The Market')
    print('2. The Town Hall')
    print()
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
    while Exit != 1:  # Choices from Woke() loop
        choice = input('...')
        print()
        if choice == '':
            woke()
        if choice == '1' or choice == 'market':
            shop()
            break
        elif choice == '2':
            townhall()
            break
        repeated()


def woke_loop():
    global choice, currency, temp_currency
    currency = temp_currency + currency
    temp_currency = 0
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
    print()
    print('You walk back to the Town square')
    print()
    print(Fore.BLUE + '█████████████' + Fore.BLACK + ' CHOICES ' + Fore.BLUE
          + '█████████████' + Fore.BLACK)
    print()
    print('Where would you like to go:')
    print('1. The Market')
    print('2. The Town Hall')
    print()
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
    print('Use your number keys to choose')
    while Exit != 1:  # Choices from Woke() loop
        choice = input('...')
        print()
        if choice == '':
            woke_loop()
        if choice == '1':
            shop()
            break
        elif choice == '2':
            townhall()
            break
        repeated()


def inventory():
    global inventory_count, xp, weapon_equip

    clear()
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
    print()
    print(Fore.YELLOW + 'Equipped Weapon: ' + Fore.BLACK)
    for weapon_e in weapon_equip:
        print(Fore.CYAN + weapon_e + Fore.BLACK)
    print()
    print(Fore.YELLOW + 'Equipped Armor:' + Fore.BLACK)
    for armor_e in armor_equip:
        print(Fore.CYAN + armor_e + Fore.BLACK)
    print()
    print(Fore.BLUE + '███████████ Your Inventory ██████████' + Fore.BLACK)
    print(Fore.YELLOW + 'Weapons:' + Fore.BLACK)
    for weapon in weapons:
        print(Fore.BLACK + weapon + Fore.BLACK)
    print(Fore.YELLOW + 'Potions:' + Fore.BLACK)
    for potion in potions:
        print(Fore.BLACK + potion + Fore.BLACK)
    print(Fore.YELLOW + 'Misc:' + Fore.BLACK)
    for other in misc:
        print(other + Fore.BLACK)
    print(Fore.BLUE + '█████████████████████' + Fore.BLACK, inventory_count,  '/ 25', Fore.BLUE + '█████' + Fore.BLACK)


def inventory_use_item():
    global health, mobility, max_health, choice
    if choice == 'use small health potion' or choice == 'use Small Health Potion' \
            or choice == 'Use Small Health Potion' or choice == 'Use small health potion':
        if 'Small Health Potion' in potions:
            if health >= max_health:
                print('You cannot use this now')
            if health < 200:
                health = health + 25
                potions.remove('Small Health Potion')
                print('You used a Small health potion')
                if health > max_health:
                    health = max_health
                choice = ''
        else:
            print('You do not have a Small health potion')

    if choice == 'use medium health potion' or choice == 'use medium Health Potion' \
            or choice == 'Use Medium Health Potion' or choice == 'Use medium health potion':
        if 'Medium Health Potion' in potions:
            if health >= max_health:
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
            if health >= max_health:
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
            elif mobility >= 75:
                mobility = 75
        else:
            print('You do not have a Mobility Buff Vial')


def shop():
    global health
    clear()
    print()
    print()

    print(Fore.BLUE + '██████████████' + Fore.BLACK + 'Shop' + Fore.BLUE + '██████████████' + Fore.BLACK)
    health = health - 50
    print('How do you do stranger would '
          '\nyou like to browse my wares?')
    print('You have', currency, 'dollars')
    print(Fore.RED + 'Weapons:' + Fore.BLACK)
    # Weapons
    if Class == 'Tank' or Class == 'tank' \
            or Class == 'Warrior' or Class == 'warrior':
        for weapons_b in weapons_buy:
            print(weapons_b)
    # Mage Weapons
    if Class == 'Mage' or Class == 'mage':
        for weapons_b in weapons_buy_mage:
            print(weapons_b)
    # Potions
    print(Fore.RED + 'Potions:' + Fore.BLACK)
    if Class == 'Warrior' or Class == 'warrior' \
            or Class == 'Tank' or Class == 'tank':
        for potion_buy in potions_buy:
            print(potion_buy)
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
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
        if choice == '':
            shop()
        if choice == 'back' or choice == 'back':
            woke_loop()
            break
        elif choice == '1':
            if currency >= 150:
                weapons.append('Sharpened Iron Sword')
                currency -= 150
                clear()
                print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.BLACK)
                print()
                woke_loop()

        elif choice == '2':
            if currency >= 200:
                weapons.append('Iron Axe')
                currency -= 200
                clear()
                print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.BLACK)
                print()
                woke_loop()
        elif choice == '3':
            if currency >= 250:
                weapons.append('Sharpened Iron Axe')
                currency -= 250
                clear()
                print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.BLACK)
                print()
                woke_loop()
        elif choice == '4':
            if currency >= 550:
                weapons.append('Steel Sword')
                currency -= 550
                clear()
                print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.BLACK)
                print()
                woke_loop()
        elif choice == '5':
            if currency >= 750:
                weapons.append('Sharpened Steel Sword')
                currency -= 750
                clear()
                print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.BLACK)
                print()
                woke_loop()
        elif choice == '6':
            if currency >= 1000:
                weapons.append('Steel Axe')
                currency -= 1000
                clear()
                print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.BLACK)
                print()
                woke_loop()
        elif choice == '7':
            if currency >= 1500:
                weapons.append('Sharpened Steel Axe')
                currency -= 1500
                clear()
                print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.BLACK)
                print()
                woke_loop()
        elif choice == '8':
            if currency >= 2500:
                weapons.append('Obsidian Strong Sword')
                currency -= 2500
                clear()
                print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.BLACK)
                print()
                woke_loop()
        elif choice == '9':
            if currency >= 2500:
                weapons.append('Obsidian Strong Sword')
                currency -= 2500
                clear()
                print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.BLACK)
                print()
                woke_loop()
        elif choice == '10':
            if currency >= 2500:
                weapons.append('Obsidian Axe')
                currency -= 2500
                clear()
                print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.BLACK)
                print()
                woke_loop()
        elif choice == '11':
            if currency >= 75:
                potions.append('Small Health Potion')
                currency -= 75
                clear()
                print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.BLACK)
                print()
                woke_loop()
        elif choice == '12':
            if currency >= 125:
                potions.append('Medium Health Potion')
                currency -= 125
                clear()
                print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.BLACK)
                print()
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
                print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.BLACK)
                print()
                woke_loop()
        elif choice == '15':
            if currency >= 750:
                potions.append('Health Buff Vial')
                currency -= 750
                clear()
                print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.BLACK)
                print()
                woke_loop()
        elif choice == '16':
            if currency >= 250:
                potions.append('Explosives')
                currency -= 250
                clear()
                print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.BLACK)
                print()
                woke_loop()
        elif choice == 'Inventory' or choice == 'inventory':
            inventory()


def repeated():
    global choice
    leveling()
    inventory_use_item()
    inventory_drop_item()
    equip()
    if choice == 'Inventory' or choice == 'inventory':
        inventory()
    elif choice == 'Stats' or choice == 'stats':
        player_stats()


def skeletal_knights():
    global enemy_health, loot1, loot2, loot3, loot4, enemy_mobility, enemy_armor, enemy_attack, enemy_max_health, \
        enemy_name, enemy_attacks, level, enemy_quote, enemy_xp
    enemy_name = 'Skeletal Knight'
    enemy_xp = 25
    enemy_attacks = ['SKULL SMASH', 'NUMB SKULL', 'SPOOK']
    enemy_quote = ['NYEH HEH HEH HEH', 'I HOPE YOUR IN A SKELETONNE OF PAIN', 'I JUST SMACKED YOU INTO TOMARROW',
                   'CUT TO THE BONE', 'BONE APE TETE']
    enemy_max_health = 35
    enemy_health = enemy_max_health
    enemy_mobility = 20
    enemy_attack = random.randint(20, 30)
    loot1 = ['Iron Axe']
    loot2 = ['Iron Axe', 'Small Health Potion']
    loot3 = ['Iron Axe', 'Medium Health Potion']
    loot4 = ['Steel Axe', 'Small Health Potion']

    clear()
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
    print()
    print('As you get closer you realise that these are')
    print('not knights but undead knights.')
    print('They notice you and start to move towards you')
    print()
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
    sleep(5)
    clear()
    attack()
    repeated()
    game_over()


def interaction():
    global interaction_chance, choice, dungeon
    interaction_chance = random.randint(1, 5)
    if interaction_chance == 1 or interaction_chance == 2 or interaction_chance == 3 or interaction_chance == 4:
        clear()
        print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
        print()
        print('As you set off on your adventure you see the')
        print('small town disappear almost instantaneously.')
        print('You soon find a convey of what appears to be')
        print('knights on horses.')
        print()
        print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
        print()
        print(Fore.BLUE + '█████████████' + Fore.BLACK + ' CHOICES ' + Fore.BLUE
              + '█████████████' + Fore.BLACK)
        print()
        print('What would you like to do:')
        print('1. Attack the knights')
        print('2. Approach the knights')
        print('3. Ignore the knights')
        print()
        print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
        print('Use your number keys to choose')
        interaction_chance = 0
        while Exit != 1:
            choice = input('...')
            print()
            if choice == '':
                interaction()
            if choice == '1':
                skeletal_knights()
                break
            elif choice == '2':
                skeletal_knights()
                break
            elif choice == '3':
                interaction_chance = random.randint(1, 2)
                if interaction_chance == 1:
                    safe_travel()
                    break
                elif interaction_chance == 2:
                    skeletal_knights()
                    break
            repeated()
            game_over()
    elif interaction_chance == 5:
        safe_travel()


def safe_travel():
    global first_loop_v
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
    print()
    print('   You continue to your destination. safely')
    print()
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
    first_loop_v = 0
    if dungeon == 1:
        valkyrie()


def attacks():
    clear()
    global choice, damage, armor, turn_counter, burn, burn_check, armor_check, burn_effect, armor_count, move, \
        attack_1, attack_2, attack_3
    if Class == 'Warrior' or Class == 'warrior':
        print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
        print()
        print('    [Sword Throw]   [WhirlWind]   [Defense]')
        print()
        print(Fore.BLUE + '█████████████' + Fore.BLACK + 'CHOICES' + Fore.BLUE + '█████████████' + Fore.BLACK)
        print()
        print('1. Sword Throw')
        print('2. Whirlwind')
        print('3. Defense')
        print('4. Back')
        print()
        print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
        choice = input('...')
        while Exit != 1:
            if choice == '1' or choice == 'Sword throw' or choice == 'sword throw':
                move = 'Sword Throw'
                damage = attack_1
                attack_turn()
                break
            if choice == '2' or choice == 'Whirlwind' or choice == 'whirlwind':
                move = 'Whirlwind'
                damage = attack_2
                attack_turn()
                break
            if choice == '3' or choice == 'Defense' or choice == 'defense':
                armor = armor + 15
                damage = 0
                armor_count = 0
                armor_check = 1
                move = 'Defense'
            if choice == '':
                attacks()
            if choice == '4' or 'Back' or 'back':
                attack()
                break
    if Class == 'Tank' or Class == 'tank':
        print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
        print()
        print('      [Ground Smash]   [Rage]   [Brace]')
        print()
        print(Fore.BLUE + '█████████████' + Fore.BLACK + ' CHOICES ' + Fore.BLUE
              + '█████████████' + Fore.BLACK)
        print()
        print('1. Ground smash')
        print('2. Rage')
        print('3. Brace')
        print('4. Back')
        print()
        print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
        choice = input('...')
        while Exit != 1:
            if choice == '1' or choice == 'Ground smash' or choice == 'ground smash':
                move = 'Ground Smash'
                damage = attack_1
                attack_turn()
                break
            if choice == '2' or choice == 'Rage' or choice == 'rage':
                damage = attack_2
                attack_turn()
                break
            if choice == '3' or choice == 'Brace' or choice == 'brace':
                armor = armor + 30
                damage = 0
                armor_count = 0
                armor_check = 1
            if choice == '':
                attacks()
            if choice == '4' or 'Back' or 'back':
                attack()
                break
    if Class == 'Mage' or Class == 'mage':
        print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
        print()
        print('   [Fire Ball]   [Fire Storm]   [Healing touch]')
        print()
        print(Fore.BLUE + '█████████████' + Fore.BLACK + ' CHOICES ' + Fore.BLUE
              + '█████████████' + Fore.BLACK)
        print()
        print('1. Fire Ball')
        print('2. Fire Storm')
        print('3. Healing Touch')
        print('4. Back')
        print()
        print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
        choice = input('...')
        while Exit != 1:
            if choice == '1' or choice == 'Fire Ball' or choice == 'fire ball':
                damage = attack_1
                move = 'Fire Ball'
                attack_turn()
                break
            if choice == '2' or choice == 'Fire Storm' or choice == 'fire storm':
                damage = attack_2
                move = 'Fire Storm'
                burn = random.randint(1, 10)
                if burn == 1 or burn == 2 or burn == 3 or burn == 4 or burn == 5:
                    burn_check = 1
                    burn_effect = 1
                if burn == 6 or burn == 7 or burn == 8 or burn == 9 or burn == 10:
                    burn_effect = 0
                attack_turn()
                break
            if choice == '3' or choice == 'Healing Touch' or choice == 'healing touch':
                move = 'Healing Touch'
                damage = 0
                turn_counter = 0
            if choice == '':
                attacks()
            if choice == '4' or 'Back' or 'back':
                attack()
                break


def attack():
    global enemy_health, enemy_name, enemy_attacks, health, xp, choice, turn_counter,\
        armor, burn_effect, armor_count, armor_check, enemy_count, temp_currency, health_print, remainingHealth, current_health
    game_over()
    if turn_counter >= 3:
        turn_counter = 0
        burn_effect = 0
        armor = max_armor
    if armor_check == 1:
        if armor_count <= 3:
            armor_count = armor_count + 1
        if armor_count >= 3:
            armor = armor - 30
            armor_count = 0
            armor_check = 0
    if enemy_health <= 0:
        clear()
        health = health + 15
        xp = xp + enemy_xp
        if health > max_health:
            health = max_health
        print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
        print()
        print('        The', enemy_name, 'has perished')
        print()
        leveling()
        print('You now have', xp, 'XP')
        text_convert = int(max_health / health_print_max)
        current_health = int(health / text_convert)
        remainingHealth = health_print_max - current_health
        health_print = ''.join(['█' for x in range(current_health)])
        health_spacing = ''.join(['░' for x in range(remainingHealth)])
        print('Health:', '      [' + Fore.RED + health_print + Fore.WHITE + health_spacing + Fore.BLACK + ']')
        print('You found', '25$ on the', enemy_name)
        temp_currency = temp_currency + 25
        if enemy_count > 0:
            enemy_count = enemy_count - 1
        print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
        if dungeon == 1:
            valkyrie()
    clear()
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)

    text_convert = int(max_health / health_print_max)
    current_health = int(health / text_convert)
    remainingHealth = health_print_max - current_health
    health_print = ''.join(['█' for x in range(current_health)])
    health_spacing = ''.join(['░' for x in range(remainingHealth)])
    print('Health:', '      [' + Fore.RED + health_print + Fore.WHITE + health_spacing + Fore.BLACK + ']')
    text_convert = int(enemy_max_health / enemy_health_print_max)
    enemy_current_health = int(enemy_health / text_convert)
    remaining_enemy_health = enemy_health_print_max - enemy_current_health
    health_print = ''.join(['█' for x in range(enemy_current_health)])
    health_spacing = ''.join(['░' for x in range(remaining_enemy_health)])
    print('Enemy Health:', '[' + Fore.MAGENTA + health_print + Fore.WHITE + health_spacing + Fore.BLACK + ']')

    print(Fore.BLUE + '█████████████' + Fore.BLACK + ' CHOICES ' + Fore.BLUE
          + '█████████████' + Fore.BLACK)
    print()
    print('1. Attack')
    print('2. Inventory')
    print()
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
    choice = input('...')
    while Exit != 1:
        if choice == '':
            attack()
        if choice == '1':
            attacks()
            break
        if choice == '2' or choice == 'Inventory' or choice == 'inventory':
            clear()
            inventory()
            inventory_use_item()
            choice = input('Type back to go to the previous screen')
            if choice == 'Back' or 'back':
                attack()
                break
        inventory_use_item()


def attack_turn():
    global enemy_health, enemy_attack, health, damage, temp_currency, x, xp, remainingHealth, health_print, current_health, health_print_max, \
            remaining_enemy_health, enemy_health_print, enemy_count, enemy_current_health, enemy_health_print_max, first_loop_stop, first_loop_v
    game_over()
    if first_loop_stop == 0:
        if first_loop_v == 0:
            first_loop_v = 0
            first_loop_stop = 1
    if first_loop_stop == 1:
        if Class == 'Mage' or Class == 'mage':
            if burn_check == 1:
                if burn_effect == 1:
                    damage = damage + 5
                if burn_effect == 0:
                    damage = damage - 5
        enemy_missed = 1
        enemy_health = enemy_health - damage
        if enemy_health <= 0:
            clear()
            health = health + 15
            xp = xp + enemy_xp
            if health > max_health:
                health = max_health
            print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
            print()
            print('        The', enemy_name, 'has perished')
            print()
            leveling()
            print('You now have', xp, 'XP')
            text_convert = int(max_health / health_print_max)
            current_health = int(health / text_convert)
            remainingHealth = health_print_max - current_health
            health_print = ''.join(['█' for x in range(current_health)])
            health_spacing = ''.join(['░' for x in range(remainingHealth)])
            print('Health:', '      [' + Fore.RED + health_print + Fore.WHITE + health_spacing + Fore.BLACK + ']')
            print('You found', '25$ on the', enemy_name)
            temp_currency = temp_currency + 25
            if enemy_count > 0:
                enemy_count = enemy_count - 1
            print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
            if dungeon == 1:
                valkyrie()
        clear()
        print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
        if random.randint(1, 100) > mobility:
            enemy_attack_percent = enemy_attack/100*armor
            enemy_attack = enemy_attack - enemy_attack_percent
            health = health - enemy_attack
            enemy_missed = 0
        print(move, 'damaged', enemy_name, 'for', damage)
        if burn_effect == 1:
            print('The', enemy_name, 'is burning')
            print('Burn did 4 Damage')
        print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
        print()
        text_convert = int(max_health / health_print_max)
        current_health = int(health / text_convert)
        remainingHealth = health_print_max - current_health
        health_print = ''.join(['█' for x in range(current_health)])
        health_spacing = ''.join(['░' for x in range(remainingHealth)])
        print('Health:', '      [' + Fore.RED + health_print + Fore.WHITE + health_spacing + Fore.BLACK + ']')
        text_convert = int(enemy_max_health / enemy_health_print_max)
        enemy_current_health = int(enemy_health / text_convert)
        remaining_enemy_health = enemy_health_print_max - enemy_current_health
        health_print = ''.join(['█' for x in range(enemy_current_health)])
        health_spacing = ''.join(['░' for x in range(remaining_enemy_health)])
        print('Enemy Health:', '[' + Fore.MAGENTA + health_print + Fore.WHITE + health_spacing + Fore.BLACK + ']')
        print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
        if enemy_missed == 0:
            print('The', enemy_name, 'used', random.choice(enemy_attacks))
            print(enemy_name, ':', random.choice(enemy_quote))
        if enemy_missed == 1:
            print(enemy_name, 'missed')
        print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
        input('Press enter to continue')
        repeated()
        attack()


def valkyrie():
    global choice, enemy_count, first_loop_v
    sleep(1)
    clear()
    if first_loop_v == 0:
        enemy_count = 5
        first_loop_v = 1
        valkyrie()
    elif first_loop_v == 1:
        rand_enemy = random.randint(1, 2)
        if enemy_count > 0:
            if rand_enemy == 1:
                ancient_viking()
            if rand_enemy == 2:
                spider()
        else:
            print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
            print()
            print('You walk into a dark cave ')
            print()
            print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
            choice = input('...')


def ancient_viking():
    print('Gay')


def spider():
    
    print('As you explore the cave further you find a giant spider dangling'
          ' from the roof as it looks hungrily at its next snack')



def game_over():
    global health, currency, temp_currency
    if health <= 0:
        health = health + 100
        temp_currency = 0
        clear()
        print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
        print()
        print('                You have DIED')
        print()
        print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
        sleep(5)
        woke()


print(Fore.BLUE + '█████████████' + Fore.BLACK + ' CHOICES ' + Fore.BLUE
      + '█████████████' + Fore.BLACK)
loopmenu()
print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
print()
player = input(
    "Please enter your name..."
)
print()
while Exit != 1:
    clear()
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
    print('                                             ')
    print('             Please Select a class             ')
    print(
        "           [Warrior] [Tank] [Mage]"
    )
    print()
    print('Warrior: For people who like to play it safe')
    print()
    print('Tank: Has more health and armour but does less\n '
          'damage.')
    print()
    print('Mage: Has less health and does less damage \n'
          'but is more mobile')
    print()
    print(Fore.BLUE + '████████████████████████████████' + Fore.BLACK)
    print()
    Class = input("...")
    clear()
    if Class == 'Warrior' or Class == 'warrior':
        health = 200
        armor = 25
        max_armor = 100
        mobility = 15
        attack_1 = random.randint(5, 7)
        attack_2 = random.randint(4, 10)
        attack_3 = 0
        weapons.append('Iron Sword')
        weapon_equip.append('Iron Sword')

        break
    elif Class == 'Tank' or Class == 'tank':
        health = 200
        armor = 50
        max_armor = 100
        attack_1 = random.randint(2, 5)
        attack_2 = random.randint(1, 6)
        mobility = 5
        weapons.append('Dull Iron Sword')
        weapon_equip.append('Dull Iron Sword')
        break
    elif Class == 'Mage' or Class == 'mage':
        health = 200
        armor = 0
        max_armor = 0
        attack_1 = random.randint(7, 8)
        attack_2 = random.randint(6, 11)
        mobility = 30
        weapons.append('Iron Dagger')
        weapon_equip.append('Iron Dagger')
        break
player_stats()
woke()
