import numpy as np
import matplotlib.pyplot as plt

def generate_ellipse_coordinates(a, b, x_c=0, y_c=0, num_points=1000, angle=0):
    theta = np.linspace(0, 2*np.pi, num_points)
    x = x_c + a * np.cos(theta) * np.cos(angle) - b * np.sin(theta) * np.sin(angle)
    y = y_c + a * np.cos(theta) * np.sin(angle) + b * np.sin(theta) * np.cos(angle)
    return x, y

def generate_ellipse_coordinates_fp(a, b, x_c=0, y_c=0, num_points=1000, angle=0):
    theta = np.linspace(0, 2*np.pi, num_points)
    x = x_c + a * np.cos(theta) * np.cos(angle) - b * np.sin(theta) * np.sin(angle)
    y = y_c + a * np.cos(theta) * np.sin(angle) + b * np.sin(theta) * np.cos(angle)
    
    focal_x = x_c - np.sqrt(a**2 - b**2) * np.cos(angle)
    focal_y = y_c - np.sqrt(a**2 - b**2) * np.sin(angle)
    
    return x, y, focal_x, focal_y
