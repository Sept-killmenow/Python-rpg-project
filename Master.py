from time import sleep
import random
from colorama import Fore
import pickle
Start = 0
Exit = 0

dungeon = 0
# Class Variables
xp = 0
max_xp = 0
xp_percent = 0
xp_print = ''
level = 0
next_lvl = 750
health = 0
health_percent = 0
max_health = 200
health_print_max = 10
health_print = ''


armor = 0
armor_percent = 0
max_armor = 100
armor_check = 0

mobility = 0
damage = 0
burn = 0
burn_effect = 0
weapon_equip = []
armor_equip = ['None', ]
currency = 150
temp_currency = 0



# Enemy Variables
enemy_name = 'null'
enemy_attacks = []
enemy_quote = []
enemy_health = 0
enemy_mobility = 0
enemy_armor = 0
enemy_attack = 0
enemy_health_percent = 0
enemy_max_health = 0
enemy_health_print = ''

# Loot pool
loot1 = []
loot2 = []
loot3 = []
loot4 = []
# Input references
Class = ''
choice = ''

# Inventory
weapons_buy = [
    Fore.YELLOW + '1. Sharpened Iron Sword $150', '2. Iron Axe $200', '3. Sharpened Iron Axe $250',
    '4. Steel Sword $550', '5. Sharpened Steel Sword $750', '6. Steel Axe $1000', '7. Sharpened Steel Axe $1500',
    '8. Obsidian Strong Sword $2500', '9. Obsidian Rapier $2500', '10.Obsidian Axe $2500' + Fore.RESET
]
potions_buy = [
    Fore.YELLOW + '11. Small Health Potion $75', '12. Medium Health Potion $125', '13. Large Health Potion $200',
    '14. Mobility Buff Vial $750', '15. Health Buff Vial $750' + Fore.RESET
]
misc_buy = [
    Fore.YELLOW + '16. Explosives x1 $250' + Fore.RESET
]
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
        xp = xp - next_lvl
        next_lvl = round(next_lvl * 1.5)
        max_health = max_health + 10
        health = max_health
        health_print_max = health_print_max + 1
        print('You have leveled up!')


def health_print():
    global x, remainingHealth, health_print, current_health, health_print_max
    text_convert = int(max_health / health_print_max)
    current_health = int(health / text_convert)
    remainingHealth = health_print_max - current_health
    health_print = ''.join(['█' for x in range(current_health)])
    health_spacing = ''.join(['░' for x in range(remainingHealth)])
    print('Health:', '[' + Fore.RED + health_print + Fore.WHITE + health_spacing + Fore.RESET + ']')


def armor_print():
    global x, remainingarmor, armor_print, current_health
    if armor > 1:
        armor_print_max = 10
        text_convert = int(max_armor / armor_print_max)
        current_armor = int(armor / text_convert)
        remainingarmor = armor_print_max - current_armor
        armor_print = ''.join(['█' for x in range(current_armor)])
        armor_spacing = ''.join(['░' for x in range(remainingarmor)])
        print('Armor: ', '[' + Fore.YELLOW + armor_print + Fore.WHITE + armor_spacing + ']')
    if armor == 0:
        print(Fore.YELLOW + 'No Armor' + Fore.RESET)


def inventory_drop_item():
    if choice == 'drop small health potion' or choice == 'drop Small Health Potion' \
            or choice == 'Drop Small Health Potion' or choice == 'Drop small health potion':
        potions.remove('Small Health Potion')
        print('You Dropped a Small Health Potion')


def equip():
    global choice, damage, armor, mobility
    if choice == 'equip sharpened iron sword' or choice == 'equip sharpened iron sword' \
            or choice == 'Equip sharpened iron sword' or choice == 'Equip Sharpened Iron Sword':
        damage = 10
        mobility = mobility - 1.5
        weapon_equip.append('Sharpened Iron Sword')
        print('You have equipped a Sharpened Iron Sword')


def clear():
    print('\n'*40)


def menu():
        clear()
        print(Fore.RESET + '████████████████████████████████')
        print()
        print("               Ara: The Epic Tale    ")
        print()
        print('████████████████████████████████')
        print('\n', '                 Instructions','\n\n', '1. To navigate menus and UI you shall type\n '
                                                             'out what the option is. Do not click on it'
                            '\n\n 2. Try not to cheat thanks\n\n 3. Type Inventory at any\n input to open the'
                            ' inventory\n\n', '4. Type Start to begin', '\n\n',
              '5. To drop a item type Drop [item name]\n\n',
              )
        print('████████████████████████████████')
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
    print('████████████████████████████████')
    print('Level:', level)
    health_print()
    armor_print()
    print('XP:', xp)
    print('████████████████████████████████')


def townhall():
    global choice
    clear()
    print('████████████████████████████████')
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
    print('█████████████ CHOICES █████████████')
    print()
    print('  1. Check the notice board')
    print('  2. Talk to the Receptionist')
    print('  3. Go Back to the Town square')
    print()
    print('████████████████████████████████')
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
    print('████████████████████████████████')
    print()
    print('              TOWN NOTICE BOARD')
    print()
    print('      [The Valkyrie]  [Hydra of Lerna]')
    print('     [Polyphemus The Cyclops] [Drakontos]')
    print('           [Explore the wilderness]')
    print()
    print('████████████████████████████████')
    print()
    print('█████████████ CHOICES █████████████')
    print()
    print('  1. Attempt to Banish the Valkyrie')
    print('  2. Try to Slay The Hydra of Lerna')
    print('  3. Go off and Destroy Polyphemus The Cyclops')
    print('  4. Try and Behead the feared Drakontos')
    print('  5. Explore the wilderness')
    print('  6. Walk back to the entrance ')
    print()
    print('████████████████████████████████')
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
                print('You are not level 5 yet')
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
    print('████████████████████████████████')
    print()
    print('  Hey there what would you like to know?     ')
    print()
    print('████████████████████████████████')
    print()
    print('████████████████████████████████')
    print()
    print('  1. Where am i?')
    print('  2. What can i do around here?')
    print('  3. Im fine thank you.')
    print()
    print('████████████████████████████████')
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
    print('████████████████████████████████')
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
    print('████████████████████████████████')
    sleep(5)
    notice()


def re_reply2():
    print('████████████████████████████████')
    print()
    print('  Well you could start by taking a look')
    print('  at the notice board.')
    print()
    print('  We would appreciate any help you are able to')
    print('  give.')
    print()
    print('████████████████████████████████')
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
    print('█████████████ CHOICES █████████████')
    print()
    print('Where would you like to go:')
    print('1. The Market')
    print('2. The Town Hall')
    print()
    print('████████████████████████████████')
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
    print('████████████████████████████████')
    print()
    print('You walk back to the Town square')
    print()
    print('█████████████ CHOICES █████████████')
    print()
    print('Where would you like to go:')
    print('1. The Market')
    print('2. The Town Hall')
    print()
    print('████████████████████████████████')
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
    print('████████████████████████████████')
    print()
    print(Fore.YELLOW + 'Equipped Weapon: ' + Fore.RESET)
    for weapon_e in weapon_equip:
        print(Fore.CYAN + weapon_e + Fore.RESET)
    print()
    print(Fore.YELLOW + 'Equipped Armor:' + Fore.RESET)
    for armor_e in armor_equip:
        print(Fore.CYAN + armor_e + Fore.RESET)
    print()
    print('███████████ Your Inventory ██████████')
    print(Fore.YELLOW + 'Weapons:' + Fore.RESET)
    for weapon in weapons:
        print(Fore.RED + weapon + Fore.RESET)
    print(Fore.YELLOW + 'Potions:' + Fore.RESET)
    for potion in potions:
        print(Fore.RED + potion + Fore.RESET)
    print(Fore.YELLOW + 'Misc:' + Fore.RESET)
    for other in misc:
        print(other + Fore.RESET)
    print('█████████████████████', inventory_count, '/ 25', '█████')


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
        else:
            print('You do not have a Mobility Buff Vial')


def shop():
    global health
    clear()
    print()
    print()

    print('██████████████ Shop ██████████████')
    health = health - 50
    print('How do you do stranger would '
          '\nyou like to browse my wares?')
    print('You have', currency, 'dollars')
    print(Fore.RED + 'Weapons:' + Fore.RESET)
    if Class == 'Tank' or Class == 'tank' \
            or Class == 'Warrior' or Class == 'warrior' or Class == 'Mage' or Class == 'mage':
        for weapons_b in weapons_buy:
            print(weapons_b)

    if Class == 'Warrior' or Class == 'warrior' \
            or Class == 'Tank' or Class == 'tank' or Class == 'Mage' or Class == 'mage':
        print(Fore.RED + 'Potions:' + Fore.RESET)
        for potion_buy in potions_buy:
            print(potion_buy)
    print(Fore.RED + 'Misc:' + Fore.RESET)
    for miscs_buy in misc_buy:
        print(miscs_buy)
    print('████████████████████████████████')
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
                print('████████████████████████████████')
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.RESET)
                print()
                woke_loop()

        elif choice == '2':
            if currency >= 200:
                weapons.append('Iron Axe')
                currency -= 200
                clear()
                print('████████████████████████████████')
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.RESET)
                print()
                woke_loop()
        elif choice == '3':
            if currency >= 250:
                weapons.append('Sharpened Iron Axe')
                currency -= 250
                clear()
                print('████████████████████████████████')
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.RESET)
                print()
                woke_loop()
        elif choice == '4':
            if currency >= 550:
                weapons.append('Steel Sword')
                currency -= 550
                clear()
                print('████████████████████████████████')
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.RESET)
                print()
                woke_loop()
        elif choice == '5':
            if currency >= 750:
                weapons.append('Sharpened Steel Sword')
                currency -= 750
                clear()
                print('████████████████████████████████')
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.RESET)
                print()
                woke_loop()
        elif choice == '6':
            if currency >= 1000:
                weapons.append('Steel Axe')
                currency -= 1000
                clear()
                print('████████████████████████████████')
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.RESET)
                print()
                woke_loop()
        elif choice == '7':
            if currency >= 1500:
                weapons.append('Sharpened Steel Axe')
                currency -= 1500
                clear()
                print('████████████████████████████████')
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.RESET)
                print()
                woke_loop()
        elif choice == '8':
            if currency >= 2500:
                weapons.append('Obsidian Strong Sword')
                currency -= 2500
                clear()
                print('████████████████████████████████')
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.RESET)
                print()
                woke_loop()
        elif choice == '9':
            if currency >= 2500:
                weapons.append('Obsidian Strong Sword')
                currency -= 2500
                clear()
                print('████████████████████████████████')
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.RESET)
                print()
                woke_loop()
        elif choice == '10':
            if currency >= 2500:
                weapons.append('Obsidian Axe')
                currency -= 2500
                clear()
                print('████████████████████████████████')
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.RESET)
                print()
                woke_loop()
        elif choice == '11':
            if currency >= 75:
                potions.append('Small Health Potion')
                currency -= 75
                clear()
                print('████████████████████████████████')
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.RESET)
                print()
                woke_loop()
        elif choice == '12':
            if currency >= 125:
                potions.append('Medium Health Potion')
                currency -= 125
                clear()
                print('████████████████████████████████')
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.RESET)
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
                print('████████████████████████████████')
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.RESET)
                print()
                woke_loop()
        elif choice == '15':
            if currency >= 750:
                potions.append('Health Buff Vial')
                currency -= 750
                clear()
                print('████████████████████████████████')
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.RESET)
                print()
                woke_loop()
        elif choice == '16':
            if currency >= 250:
                potions.append('Explosives')
                currency -= 250
                clear()
                print('████████████████████████████████')
                print()
                print(Fore.YELLOW, 'Purchase successful', Fore.RESET)
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
    global enemy_health, enemy_mobility, enemy_armor, enemy_attack, enemy_max_health, enemy_name, enemy_attacks, level, \
        enemy_quote
    enemy_name = 'Skeletal Knight'
    enemy_attacks = ['SKULL SMASH', 'NUMB SKULL', 'SPOOK']
    enemy_quote = ['NYEH HEH HEH HEH', 'I HOPE YOUR IN A SKELETONNE OF PAIN', 'I JUST SMACKED YOU INTO TOMARROW',
                   'CUT TO THE BONE', 'BONE APE TETE']
    enemy_max_health = 35
    enemy_health = enemy_max_health
    enemy_mobility = 20
    random.randint(0, 10)

    clear()
    print('████████████████████████████████')
    print()
    print('As you get closer you realise that these are')
    print('not knights but undead knights.')
    print('They notice you and start to move towards you')
    print()
    print('████████████████████████████████')
    sleep(5)
    clear()
    attack()
    repeated()
    game_over()


def interaction():
    global interaction_chance, choice, dungeon
    interaction_chance = random.randint(1, 5)
    if interaction_chance == 1 or interaction_chance == 2 or interaction_chance == 3 or interaction_chance == 4 \
            or interaction_chance == 5:
        clear()
        print('████████████████████████████████')
        print()
        print('As you set off on your adventure you see the')
        print('small town disappear almost instantaneously.')
        print('You soon find a convey of what appears to be')
        print('knights on horses.')
        print()
        print('████████████████████████████████')
        print()
        print('█████████████ CHOICES █████████████')
        print()
        print('What would you like to do:')
        print('1. Attack the knights')
        print('2. Approach the knights')
        print('3. Ignore the knights')
        print()
        print('████████████████████████████████')
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
    print('████████████████████████████████')
    print()
    print('   You continue to your destination. safely')
    print()
    print('████████████████████████████████')
    if dungeon == 1:
        valkyrie()


def attacks():
    clear()
    global choice, damage, armor, turn_counter, armor_check, burn_effect, armor_count, move, attack_1, attack_2, attack_3
    if Class == 'Warrior' or Class == 'warrior':
        print('████████████████████████████████')
        print()
        print('    [Sword Throw]   [WhirlWind]   [Defense]')
        print()
        print('█████████████ CHOICES █████████████')
        print()
        print('1. Sword Throw')
        print('2. Whirlwind')
        print('3. Defense')
        print('4. Back')
        print()
        print('████████████████████████████████')
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
        print('████████████████████████████████')
        print()
        print('      [Ground Smash]   [Rage]   [Brace]')
        print()
        print('█████████████ CHOICES █████████████')
        print()
        print('1. Ground smash')
        print('2. Rage')
        print('3. Brace')
        print('4. Back')
        print()
        print('████████████████████████████████')
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
        print('████████████████████████████████')
        print()
        print('   [Fire Ball]   [Fire Storm]   [Healing touch]')
        print()
        print('█████████████ CHOICES █████████████')
        print()
        print('1. Fire Ball')
        print('2. Fire Storm')
        print('3. Healing Touch')
        print('4. Back')
        print()
        print('████████████████████████████████')
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
                burn = random.randint(1,10)
                if burn == 1 or burn == 2 or burn == 3 or burn == 4 or burn == 5:
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


def turn_counter():
    global turn_counter, armor, burn_effect, armor_count, armor_check
    if turn_counter >= 3:
        turn_counter = 0
        burn_effect = 0
        armor = max_armor
    if armor_check == 1:
        if armor_count <= 3:
            armor_count = armor_count + 1
        if armor_count >= 3:
            if Class == 'tank' or Class == 'Tank':
                armor = armor - 30
                armor_count = 0
                armor_check = 0


def attack():
    global enemy_health, enemy_name, enemy_attacks, health, xp, choice
    game_over()
    turn_counter()
    if enemy_health <= 0:
        clear()
        print('████████████████████████████████')
        print()
        print('        The', enemy_name, 'has perished')
        print()
        leveling()
        print('You now have', xp)
        health_print()
        print('████████████████████████████████')
        if dungeon == 1:
            valkyrie()
    clear()
    print('████████████████████████████████')
    print()
    print(enemy_name, 'Health:', enemy_health)
    print('Your health:', health)
    print()
    print('█████████████ CHOICES █████████████')
    print()
    print('1. Attack')
    print('2. Inventory')
    print()
    print('████████████████████████████████')
    choice = input('...')
    while Exit != 1:
        if choice == '':
            attack()
        if choice == '1':
            attacks()
            break
        if choice == '2':
            clear()
            inventory()
            inventory_use_item()
            choice = input('Type back to go to the previous screen')
            if choice == 'Back' or 'back':
                attack()
                break


def attack_turn():
    global enemy_health, enemy_attack, health, damage
    game_over()
    enemy_attack = 20
    if burn_effect == 1:
        damage = damage + 4
    if burn_effect == 0:
        damage = damage - 4
    if damage < 0:
        damage = 0
    health = health - enemy_attack
    enemy_health = enemy_health - damage
    if enemy_health <= 0:
        clear()
        print('████████████████████████████████')
        print()
        print('        The', enemy_name, 'has perished')
        print()
        leveling()
        print('You now have', xp)
        print('HP:', health)
        print('You found', loot1)
        print('████████████████████████████████')
        if dungeon == 1:
            valkyrie()
    clear()
    print('████████████████████████████████')
    print(move, 'damaged', enemy_name, 'for', damage)
    if burn_effect == 1:
        print('The', enemy_name, 'is burning')
        print('Burn did 4 Damage')
    print('████████████████████████████████')
    print()
    health_print
    print()
    print('████████████████████████████████')
    print('The', enemy_name, 'used', random.choice(enemy_attacks))
    print(enemy_name, ':', random.choice(enemy_quote))
    print('████████████████████████████████')
    input('Press enter to continue')
    repeated()
    attack()


def valkyrie():
    clear()
    print('████████████████████████████████')
    print()
    print('Valkyrie fight')
    print()
    print('████████████████████████████████')
    choice = input('...')


def game_over():
    global health, currency, temp_currency
    if health <= 0:
        health = health + 100
        temp_currency = 0
        clear()
        print('████████████████████████████████')
        print()
        print('                You have DIED')
        print()
        print('████████████████████████████████')
        sleep(5)
        woke()


loopmenu()
print('████████████████████████████████')
print()
player = input(
    "Please enter your name..."
)
print()
while Exit != 1:
    clear()
    print('████████████████████████████████')
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
    print('████████████████████████████████')
    print()
    Class = input("...")
    clear()
    if Class == 'Warrior' or Class == 'warrior':
        health = 125
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
        attack_1 = random.randint(1, 3)
        attack_2 = random.randint(1, 4)
        mobility = 5
        weapons.append('Dull Iron Sword')
        weapon_equip.append('Dull Iron Sword')
        break
    elif Class == 'Mage' or Class == 'mage':
        health = 80
        armor = 0
        max_armor = 0
        attack_1 = random.randint(4, 5)
        attack_2 = random.randint(1, 7)
        mobility = 30
        weapons.append('Iron Dagger')
        weapon_equip.append('Iron Dagger')
        break
player_stats()
woke()
