from enemy import Enemy
from settings import *
from math import sin, cos, hypot, radians, atan2, degrees

class Enemy_6(Enemy):
    """Enemy 6 - moves in a circular pattern 90 degrees, pauses for some time, and do it again."""
    
    def __init__(self, x, y, angular_speed, game, trajectory_center, pause_time):
        super().__init__(x, y, angular_speed, game)

        self.trajectory_center = trajectory_center
        self.trajectory_radius = hypot(self.x - trajectory_center[0], self.y - trajectory_center[1])
        self.angle = self.starting_angle()
        self.inicial_angle = self.angle
        self.last_pause_angle = self.angle
        self.pause_time = pause_time
        self.timer = 0
        self.pause = True
        
    def starting_angle(self):
        return round(degrees(atan2(self.hitbox.centery - self.trajectory_center[1], self.hitbox.centerx - self.trajectory_center[0])))
    
    def pause_movement(self):
        self.pause = True
        self.timer = 0   
    
    def movement(self):
        if self.angle <= self.inicial_angle - 360:
            self.angle = self.inicial_angle
            self.last_pause_angle = self.angle

        if self.pause:
            self.timer += 1 / FPS * 1000
            if self.timer >= self.pause_time:
                self.pause = False
            else:
                return

        cx, cy = self.trajectory_center
        r = self.trajectory_radius

        self.angle += self.speed
        
        theta = radians(self.angle)
        self.hitbox.centerx = cx + r * cos(theta)
        self.hitbox.centery = cy + r * sin(theta)

        if abs(self.angle - self.last_pause_angle) >= 90:
            self.last_pause_angle = self.angle
            self.pause_movement()