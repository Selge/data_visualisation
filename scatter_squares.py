import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8-darkgrid')

fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.PuBuGn, s=1)
ax.axis([0, 1100, 0, 1_100_000])

ax.set_title("Quadratzahlen", fontsize=20)
ax.set_xlabel("Wert", fontsize=10)
ax.set_ylabel("Wertquadrat", fontsize=10)
ax.tick_params(axis='both', which='major', labelsize=11)

plt.savefig('quadratzahlen.png', bbox_inches='tight')
