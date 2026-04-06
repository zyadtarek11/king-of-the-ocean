from pgzero.actor import Actor
class Enemy(Actor):
    def __init__(self, image_prefix, x, y):
        # it's easier to save frames this way 
        super().__init__(f"{image_prefix}1", (x, y))
        self.frames = [f"{image_prefix}1", f"{image_prefix}2"] 
        self.frame_index = 0
        self.timer = 0
        self.speed = 2
        self.start_x = x
        self.direction = 1 

    def patrol(self):
        raise NotImplementedError("you forgot to implement the patrol mechanic fro you enemy character")

    def animate(self):
        # this wil loop on each frame in the list and return back again to the first frame using modulo and the oppostie
        self.timer += 1
        if self.timer > 8:
            self.timer = 0
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.image = self.frames[self.frame_index]

