'''
Elastic Collisions Simulation using Pygame (Python).
Jake Teeter
12/15/2023

This script simulates elastic collisions between 2 circle (particles) using Pygame.
'''
import pygame
import sys


class Particle:
    def __init__(self, x, y, radius, mass, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.color = color
        self.vx = 0
        self.vy = 0

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)


class ParticleSimulation:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.dt = 0.1
        self.particles = []

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Collisions Simulation")

    def add_particle(self, x, y, radius, mass, color, vx=0, vy=0):
        particle = Particle(x, y, radius, mass, color)
        particle.vx = vx
        particle.vy = vy
        self.particles.append(particle)

    def handle_collisions(self):
        """
        For each pair of particles, it calculates the distance between their centers
        and checks if they collide based on their radii. If a collision is detected,
        it applies the elastic collision logic to update their velocities.
        Logic:
        - Calculate the new velocities (v1 and v2) for the colliding particles.
        - Update the velocities of the particles accordingly.
        """
        for i in range(len(self.particles)):
            for j in range(i + 1, len(self.particles)):
                dx = self.particles[j].x - self.particles[i].x
                dy = self.particles[j].y - self.particles[i].y
                distance = ((dx ** 2) + (dy ** 2)) ** 0.5

                if distance < self.particles[i].radius + self.particles[j].radius:
                    m1, m2 = self.particles[i].mass, self.particles[j].mass
                    u1, u2 = self.particles[i].vx, self.particles[j].vx
                    v1 = ((m1 - m2) * u1 + 2 * m2 * u2) / (m1 + m2)
                    v2 = ((m2 - m1) * u2 + 2 * m1 * u1) / (m1 + m2)

                    self.particles[i].vx, self.particles[j].vx = v1, v2

    def update_positions(self):
        for particle in self.particles:
            particle.x += particle.vx * self.dt
            particle.y += particle.vy * self.dt

    def run_simulation(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.handle_collisions()
            self.update_positions()

            # Draw particles
            self.screen.fill((255, 255, 255))
            for particle in self.particles:
                particle.draw(self.screen)

            pygame.display.flip()
            pygame.time.delay(10)


if __name__ == "__main__":
    pygame.init()

    simulation = ParticleSimulation(800, 600)
    simulation.add_particle(100, 300, 20, 1, (0, 255, 255), vx=4) #vx is the initial velocity of the circle(s)
    simulation.add_particle(700, 300, 30, 2, (0, 0, 0), vx=-1)

    simulation.run_simulation()
