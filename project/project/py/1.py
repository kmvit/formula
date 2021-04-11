import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.set_xlim((-5, 5))
ax.set_ylim((-5, 5))
ax.set_aspect("equal")
ax.grid()

ax.set_title("Заголовок")
ax.set_xlabel("X")
ax.set_ylabel("Y")

x = np.linspace(-5, 5, 100)
y = eval(input("введите формулу: "))

ax.plot(x, y)

plt.show()
