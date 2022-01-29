import matplotlib.pyplot as plt
import math

a = 9.8  # Acceleration due to gravity,  m/s^2
theta = []
v = 50
m = 10
c = 1.29
vt = (m * 9.8) / c  # terminal velocity #151.93
time = []
horizontal_range = []
vertical_range = []

for th in range(10,50,5):
    for t in range(0, 500):
        var = (-a * t) / vt
        z = (vt / 9.8) * (v * 0.866 + vt) * (1 - (2.718 ** var)) - vt * t
        # while r>= 0:
        x = ((1 - math.exp(var)) * (v * vt * math.cos(th))) / a
        horizontal_range.append(x)
        vertical_range.append(z)
        time.append(t)

    theta.append(th)
    # break
plt.plot(horizontal_range, vertical_range, color='red')
plt.xlabel('x')
plt.ylabel('z')
plt.ylim(0)
plt.xlim(0)
plt.title('Projectile')
plt.show()