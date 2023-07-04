import time
import os
import json

from pynput import keyboard

from map import Map
from helicopter import Helicopter as Helico
from clouds import Clouds

MAP_W, MAP_H = 20, 10
THREE_UPDATE = 50
FIRE_UPDATE = 100
CLOUDS_UPDATE = 100
TICK_SLEEP = 0.1
field = Map(MAP_W, MAP_H)
helico = Helico(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)
tick = 1


MOVES = {'w': (-1,0), 'd': (0,1), 's': (1,0), 'a': (0,-1)}
# f - save, g - load
def process_key(key):
    global helico, tick, clouds, field
    c = key.char.lower()
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]  
        helico.move(dx, dy)
    if (c == 'g'):
        with open('level.json', 'r') as lvl:
            data = json.load(lvl)
            helico.import_data(data["helicopter"]),
            clouds.import_data(data["clouds"]),
            field.import_data(data["field"]),
            tick = data["tick"] or 1
    if (c == 'f'): 
        data = {
            "helicopter": helico.export_data(),
            "clouds": clouds.export_data(),
            "field": field.export_data(),
            "tick": tick
        }

        with open("level.json", "w") as lvl:
            json.dump(data, lvl)

    
    # if key.char == "a" or key.char == "A":
    #     print ("top");
    

listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)

listener.start()




while True:
    os.system("clear")
    print ("TICK", tick)
    field.process_helicopter(helico, clouds)

    helico.print_menu()
    field.print_map(helico, clouds)
 
    tick += 1
    time.sleep(TICK_SLEEP)   
    if (tick % THREE_UPDATE == 0):
        field.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        field.update_fire()
    if (tick % CLOUDS_UPDATE == 0):
        clouds.update()

