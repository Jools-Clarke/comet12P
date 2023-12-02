import numpy as np
import matplotlib.pyplot as plt
import utils as ut

#12P

#eccentricity
e = 0.954591
#perihelion
peri_h = 0.780784 #AU

R_sun = 696340E3 / 1.5E11 #AU
i = 74.1911

a = peri_h / (1 - e)
b = a * np.sqrt(1 - e**2)

fp = (a / 2) - peri_h
# (x**2/a**2) + (y**2/b**2) = 1

x, y, fp_x, fp_y = ut.generate_ellipse_coordinates_fp(a, b, angle = np.deg2rad(i))
x_earth, y_earth = ut.generate_ellipse_coordinates(1, 1, angle = np.deg2rad(i)) #earth

plt.figure(figsize=(5,5)) 
plt.plot(x, y, 'k--', markersize=1)  # plot the ellipse
plt.plot(x_earth+fp_x, y_earth+fp_y, 'b--', markersize=1)  # plot earths orbit
plt.axis('equal') # set the x and y axes to the same scale

plt.plot(fp_x, fp_y, 'yo')
plt.ylim(fp_y-20, fp_y+20)
plt.xlim(fp_x - 20, fp_x + 20)

plt.savefig('orbit.png')