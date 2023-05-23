import random

class Game:
    def __init__(self):
        self.score = 0
        self.health = 3
        self.water_reservoirs = 1
        self.map_width = 10
        self.map_height = 5
        self.trees = []
        self.rivers = []
        self.hospital = (random.randint(0, self.map_width - 1), random.randint(0, self.map_height - 1))
        self.shop = (random.randint(0, self.map_width - 1), random.randint(0, self.map_height - 1))

    def generate_map(self):
        for _ in range(self.map_width):
            self.trees.append((random.randint(0, self.map_width - 1), random.randint(0, self.map_height - 1)))
        for _ in range(self.map_height):
            self.rivers.append((random.randint(0, self.map_width - 1), random.randint(0, self.map_height - 1)))

    def play(self):
        print("Welcome to the Firefighter Game!")
        self.generate_map()

        while True:
            self.display_game_status()
            choice = input("Enter your choice (1 - Move, 2 - Extinguish, 3 - Visit Hospital, 4 - Visit Shop): ")
            
            if choice == "1":
                self.move()
            elif choice == "2":
                self.extinguish()
            elif choice == "3":
                self.visit_hospital()
            elif choice == "4":
                self.visit_shop()
            else:
                print("Invalid choice. Try again.")

            self.update_game_state()
            if self.is_game_over():
                break

    def display_game_status(self):
        print("Score: ", self.score)
        print("Health: ", self.health)
        print("Water Reservoirs: ", self.water_reservoirs)
        print("Hospital: ", self.hospital)
        print("Shop: ", self.shop)
        print("Trees: ", self.trees)
        print("Rivers: ", self.rivers)

    def move(self):
        print("Moving...")

    def extinguish(self):
        print("Extinguishing...")

    def visit_hospital(self):
        print("Visiting hospital...")

    def visit_shop(self):
        print("Visiting shop...")

    def update_game_state(self):
        print("Updating game state...")

    def is_game_over(self):
        return False

game = Game()
game.play()