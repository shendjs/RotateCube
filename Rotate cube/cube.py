import numpy as np
import pygame
import sys

# Pygame initialization
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rotating Cube")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Cube settings
cube_size = 200
A, B, C = 0, 0, 0
increment_speed = 0.05

# Calculate 3D points of a cube
def get_cube_points():
    half = cube_size / 2
    return [
        np.array([-half, -half, -half]),
        np.array([ half, -half, -half]),
        np.array([ half,  half, -half]),
        np.array([-half,  half, -half]),
        np.array([-half, -half,  half]),
        np.array([ half, -half,  half]),
        np.array([ half,  half,  half]),
        np.array([-half,  half,  half]),
    ]

# Rotation matrix for X, Y, Z axes
def rotate_x(point, angle):
    matrix = np.array([
        [1, 0, 0],
        [0, np.cos(angle), -np.sin(angle)],
        [0, np.sin(angle),  np.cos(angle)]
    ])
    return np.dot(matrix, point)

def rotate_y(point, angle):
    matrix = np.array([
        [ np.cos(angle), 0, np.sin(angle)],
        [0, 1, 0],
        [-np.sin(angle), 0, np.cos(angle)]
    ])
    return np.dot(matrix, point)

def rotate_z(point, angle):
    matrix = np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle),  np.cos(angle), 0],
        [0, 0, 1]
    ])
    return np.dot(matrix, point)

# Project 3D point to 2D
def project(point):
    distance = 400
    factor = distance / (distance + point[2])
    x = int(point[0] * factor + width // 2)
    y = int(point[1] * factor + height // 2)
    return x, y

# Draw edges of the cube
def draw_cube(points):
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]
    for edge in edges:
        start, end = edge
        pygame.draw.line(screen, WHITE, points[start], points[end], 2)

# Main loop
clock = pygame.time.Clock()
cube_points = get_cube_points()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear screen
    screen.fill(BLACK)

    # Rotate cube
    rotated_points = []
    for point in cube_points:
        rotated = rotate_x(point, A)
        rotated = rotate_y(rotated, B)
        rotated = rotate_z(rotated, C)
        rotated_points.append(project(rotated))

    # Draw cube
    draw_cube(rotated_points)

    # Update rotation angles
    A += increment_speed
    B += increment_speed
    C += increment_speed

    # Update display
    pygame.display.flip()
    clock.tick(60)
