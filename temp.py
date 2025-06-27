import matplotlib.pyplot as plt

# Temperature readings for the week
temperatures = [20, 22, 19, 23, 21, 24, 20]
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Create the line plot
plt.plot(days, temperatures, marker='o')

# Adding title and labels
plt.title('Temperature Readings Over a Week')
plt.xlabel('Days of the Week')
plt.ylabel('Temperature (°C)')

# Show grid
plt.grid()

# Display the plot
plt.show()
