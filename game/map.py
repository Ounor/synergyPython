
import os
from utils import randbool, randcell, randcell2
THREE_BONUS = 5
UPGRADE_COST = 25
HEALTH_COST = 15
CELL_TYPES = "🟩🌲🔹🏥🏪🔥"
class Map:
        
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]
        self.generate_forest(3, 10)
        self.generate_river(10)
        self.generate_river(10)
        self.generate_upgrade_shop()

    def check_bounds(self, x, y):
        if (x < 0 or y < 0 or x >= self.w or y >= self.h):
            return False    
        return True
    
    def print_map(self, helico, clouds):
        print("🔲" * (self.w + 2))
        for ri in range(self.h):
            print("🔲", end='')
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if (clouds.cells[ri][ci] == 1):
                    print('⬜', end='');
                elif (clouds.cells[ri][ci] == 2):
                    print('🟥', end='');
                elif (helico.x == ri and helico.y == ci):
                    print('🚁', end='')
                elif (cell >= 0 and cell < len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end='')
            print("🔲")
        print("🔲" * (self.w + 2) )
 
    def generate_river(self, len):
        rc = randcell(self.w, self.h)
        rx, ry = rc[0], rc[1]
        if (self.check_bounds(rx, ry)):
            self.cells[rx][ry] = 2
            while len > 0:
                rc2 = randcell2(rx, ry)
                rx2,ry2 = rc2[0], rc2[1]
                if (self.check_bounds(rx2, ry2)):
                    self.cells[rx2][ry2] = 2
                    rx, ry = rx2,ry2
                    len -= 1
        else:
            self.generate_river(len)

    def generate_forest(self, r, mxr):
        for ri in range (self.h):
            for ci in range (self.w):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1

    def generate_upgrade_shop(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.check_bounds(cx, cy) and self.cells[cx][cy] == 0):
            self.cells[cx][cy] = 4

    def generate_medical(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.check_bounds(cx, cy) and self.cells[cx][cy] != 4):
            self.cells[cx][cy] = 3
        else:
            self.generate_medical()

    def generate_tree(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.check_bounds(cx, cy) and self.cells[cx][cy] == 0):
            self.cells[cx][cy] = 1


    def add_fire(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.check_bounds(cx, cy) and self.cells[cx][cy] == 1):
            self.cells[cx][cy] = 5

    def update_fire(self):
        for ri in range (self.h):
            for ci in range (self.w):
                cell = self.cells[ri][ci]
                if (cell == 5):
                    self.cells[ri][ci] = 0
        for ri in range(10):
            self.add_fire() 

    def process_helicopter(self, helico, clouds):
        c = self.cells[helico.x][helico.y]   
        d = clouds.cells[helico.x][helico.y] 
        if (c == 2):
            helico.tank = helico.mxtank
        elif (c == 5 and helico.tank > 0):
            helico.tank -= 1
            helico.score += THREE_BONUS
            self.cells[helico.x][helico.y]  = 1
        elif (c == 4 and helico.score >= UPGRADE_COST):
            helico.mxtank += 1
            helico.score -= UPGRADE_COST
        elif (c == 3 and helico.health <= 1):
            helico.health += 1000
            helico.score -= HEALTH_COST
        elif (d == 2):
            helico.health -= 1
            if (helico.health == 0) :
                os.system("clear")
                print ("GAME OVER, YOUR SCORE IS", helico.score)
                exit (0)
    

    def export_data(self):
        return { "cells": self.cells}
  
    def import_data(self, data):
        self.cells = data["cells"] or [[0 for i in range(self.w)] for j in range(self.h)]
       
