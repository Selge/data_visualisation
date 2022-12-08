import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()

ax.plot(input_values, squares, linewidth=2.5)

ax.set_title("Quadratzahlen", fontsize=20)
ax.set_xlabel("Wert", fontsize=10)
ax.set_ylabel("Wertquadrat", fontsize=10)
ax.tick_params(axis='both', labelsize=11)

plt.show()
