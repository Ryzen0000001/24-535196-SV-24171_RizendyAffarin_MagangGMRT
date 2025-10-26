import numpy as np
import matplotlib.pyplot as plt

# Rizendy Affarin

L1 = float(input("nn/nnnn**/nn/nnnnn: "))
L2 = float(input("nn/nnnnnn/nn/nnn**: "))

theta1 = float(input("Femur (40): "))
theta2 = float(input("Tibia (30): "))
theta1 = np.deg2rad(theta1)
theta2 = np.deg2rad(theta2)
x = L1 * np.cos(theta1) + L2 * np.cos(theta1 + theta2)
y = L1 * np.sin(theta1) + L2 * np.sin(theta1 + theta2)

x0, y0 = 0, 0
x1 = L1 * np.cos(theta1)
y1 = L1 * np.sin(theta1)

plt.figure()
plt.plot([x0, x1, x], [y0, y1, y], '-o', color='purple')
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis('equal')
plt.show()
print(f"Posisi End-Effector: x = {x:.2f}, y = {y:.2f}")
