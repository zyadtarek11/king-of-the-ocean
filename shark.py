from enemy import Enemy
class Shark(Enemy):
    def __init__(self, x, y):
        
        super().__init__("shark/shark", x, y)
        
        self.speed = 4 
    def patrol(self):

        # shark will move from left to right and vice versa
        self.x += self.speed * self.direction
        if self.x < 50 or self.x > 718:
            self.direction *= -1
    