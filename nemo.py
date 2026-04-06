from pgzero.actor import Actor
from pgzero.keyboard import keyboard
class Nemo(Actor):
    def __init__(self, x, y):
        super().__init__("nemo/nemo-idle1", (x, y))
        self.idle_frames = [
            "nemo/nemo-idle1", "nemo/nemo-idle2", "nemo/nemo-idle3", "nemo/nemo-idle4",
            "nemo/nemo-idle5", "nemo/nemo-idle6", "nemo/nemo-idle7", "nemo/nemo-idle8",
            "nemo/nemo-idle9", "nemo/nemo-idle10", "nemo/nemo-idle11"
        ]
        self.current_frame = 0  
        self.speed = 4
        self.timer = 0          

    def animate(self):
        self.timer += 1
        if self.timer > 5:
            self.timer = 0
            self.current_frame += 1
            if self.current_frame >= len(self.idle_frames):
                self.current_frame = 0
            self.image = self.idle_frames[self.current_frame]
            
    # control nemo's movement with keyboard
    def move(self):
        if keyboard.left and self.left > 0:
            self.x -= self.speed
        if keyboard.right and self.right < 768: 
            self.x += self.speed
        if keyboard.up and self.top > 0:
            self.y -= self.speed
        if keyboard.down and self.bottom < 600: 
            self.y += self.speed