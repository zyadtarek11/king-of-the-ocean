from enemy import Enemy
class Octopus(Enemy):
    def __init__(self, x, y):
        super().__init__("octopus/octopus", x, y)
        
        self.speed = 1 
        self.start_y = y 
        
    # octopus will move from top to left and vice versa
    def patrol(self):
        self.y += self.speed * self.direction
        if self.y < 50 or self.y > 500:
            self.direction *= -1