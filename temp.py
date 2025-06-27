import matplotlib.pyplot as plt

temperatures = [20, 22, 19, 23, 21, 24, 20]
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

plt.plot(days, temperatures, marker='o')

plt.title('Temperature Readings Over a Week')
plt.xlabel('Days of the Week')
plt.ylabel('Temperature (°C)')

plt.grid()


plt.show()
