from utils import randcell
class Helicopter:

    def __init__(self, w, h):
        rc = randcell(w, h)
        rx,ry = rc[0], rc[1]
        self.x = rx
        self.y = ry   
        self.h = h
        self.w = w
        self.tank = 0
        self.mxtank = 1
        self.health = 100
        self.mxhealth = 100
        self.score = 0

    def move(self, dx, dy):
        nx, ny = dx + self.x, dy + self.y
        if(nx >= 0 and ny >= 0 and nx < self.h and ny < self.w):
            self.x, self.y = nx, ny

    def print_menu(self):
        print("TANK: ", self.tank, "|", self.mxtank, sep='')
        print("HEALTH: ", self.health, "|", self.mxhealth, sep='')
        print("SCORE: ", self.score, sep='')


    def export_data(self):
        return { "score": self.score,
                "health": self.health,
                "x": self.x,
                "y": self.y,    
                "tank": self.tank,
                "mxtank": self.mxtank}
    

    def import_data(self, data):
        self.score = data["score"] or 0
        self.health =data["health"] or 1000
        self.x = data["x"] or 0
        self.y = data["y"] or 0
        self.tank =data["tank"] or 0
        self.mxtank =data["mxtank"] or 1