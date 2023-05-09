"""
Exercise:
    https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
"""


def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if wall_in_front():
        turn_left()
    elif not wall_on_right():
        turn_right()
    if front_is_clear():
        move()
