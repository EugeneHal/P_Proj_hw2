import random
from hw_2_modules import *

arc = ArcherMain('Sniper')
med = MedicMain('Aibolit')
fighter = InfantrymanMain('Rambo')

# ------------- Testing -------------------
# print(arc.get_name())
# print(arc.get_position())
# print(arc.get_health())
#
# arc.health_down(20)
# print(arc.get_health())
# # arc.health_up()
# # print(arc.get_health())
#
# arc.moved()
# print(arc.get_position())
#
# arc.set_position(50)
# print(arc.get_position())
#
# arc.moved()
# print(arc.get_position())
#
# print(fighter.get_name())
#
# arc.health_down(fighter_damage)
# print(arc.get_health())
#
# arc.health_up(med_heal)
# arc.health_up(med_heal)
# arc.health_down(fighter_damage)
# arc.health_up(med_heal)
# print(arc.get_health())


# ----------- Variables -------------------------
arc_name = arc.get_name()
arc.set_position(50)
arc_pos = arc.get_position()
arc_damage = arc.get_attack()
arc_health = arc.get_health()
arc_dist = arc.get_attack_dist()

fighter_name = fighter.get_name()
fighter_pos = fighter.get_position()
fighter_damage = fighter.get_attack()
fighter_health = arc.get_health()
fighter_dist = fighter.get_attack_dist()

med_heal = med.get_heal()

# ----------- Game Start -------------------------
print(f'-----$$$$ Fight {arc_name} vs {fighter_name} $$$$-----')
print('Arc health >', arc_health)
print('Fighter health >', fighter_health)
print('Archer position >', arc_pos)
print('Fighter position >', fighter_pos)

count = 0
while arc_health > 0 or fighter_health > 0:
    count += 1
    if arc_pos - fighter_pos >= 1:
        fighter.moved()
        fighter_pos = fighter.get_position()
        print(f'{count}. {fighter_name} moved to position {fighter_pos}')
    if abs(arc_pos - fighter_pos) <= arc_dist:
        fighter.health_down(arc_damage)
        fighter_health = fighter.get_health()

    if abs(arc_pos - fighter_pos) <= fighter_dist:
        arc.health_down(fighter_damage)
        arc_health = arc.get_health()
        print(f'{count}. {arc_name} -->. {fighter_name} health: {fighter_health} >< {fighter_name} |/. {arc_name} health: {arc_health}')
    # print(count, f'{fighter_name} |/. {arc_name} health: {arc_health}')

    if arc_health <= 0 or fighter_health <= 0:
        print(('{} lost in {} turns'.format(min((arc_health, arc_name), (fighter_health, fighter_name))[1], count)))
        break

    if count % 2:
        random.choices([fighter.health_up(med_heal), arc.health_up(med_heal)])

print(f'{arc_name} health = {arc_health}')
print(f'{fighter_name} health = {fighter_health}')