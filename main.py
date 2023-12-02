import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

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

def ellipse(r = 1, a = 1, b = 1, x_c = 0, y_c = 0):
    if a == 1:
        x = np.arange(-r, r, 0.00001)
    elif r == 1:
        x = np.arange(-a, a, 0.00001)
    else:
        raise ValueError()
    y_p = np.sqrt(y_c + b**2*r**2 - (((x - x_c)**2 * b**2) / a**2))
    y_n = -np.sqrt(y_c + b**2*r**2 - (((x - x_c)**2 * b**2) / a**2))
    return x, y_p, y_n

c = ellipse(R_sun, 1, 1,-fp, 0)
e = ellipse(1, a, b, 0, 0)

plt.figure( dpi = 100)
plt.plot(e[0], e[1], 'k-', markersize=1)
plt.plot(e[0], e[2], 'k-', markersize=1)
plt.plot(c[0], c[1], 'y-', markersize=50)
plt.plot(c[0], c[2], 'y-', markersize=50)
plt.ylim(-7, 7)
plt.xlim(-fp - 10, -fp + 10)

plt.savefig('12P.png')  # save the figure to file