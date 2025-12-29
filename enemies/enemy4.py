from enemy import Enemy
from settings import *
from math import sin, cos, hypot, radians, atan2, degrees

class Enemy_4(Enemy):
    """Enemy 4 - moves in a circular pattern."""
    
    def __init__(self, x, y, angular_speed, game, trajectory_center):
        super().__init__(x, y, angular_speed, game)

        self.trajectory_center = trajectory_center
        self.trajectory_radius = hypot(self.x - trajectory_center[0], self.y - trajectory_center[1])
        self.angle = self.starting_angle()
        
    def starting_angle(self):
        return degrees(atan2(self.hitbox.centery - self.trajectory_center[1], self.hitbox.centerx - self.trajectory_center[0]))
    
    def movement(self):
        (cx, cy) = self.trajectory_center
        r = self.trajectory_radius
        theta = radians(self.angle)

        self.hitbox.centerx = cx + r * cos(theta)
        self.hitbox.centery = cy + r * sin(theta)
        
        if self.trajectory_radius != 0:
            self.angle += self.speed