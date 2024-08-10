import matplotlib.pyplot as plt
import numpy as np


user_input = input("Enter a string: ")

if len(user_input) < 3:
    print("Input must have at least three characters.")
else:
    x_value = ord(user_input[2])
    x = np.linspace(0, x_value*2, x_value*50)
    y = 4 * np.sin(x) + 7
    plt.plot(x, y, label='y = 4sin(x) + 7')
    y_at_x_value = 4 * np.sin(x_value) + 7
    plt.plot(x_value, y_at_x_value, 'ro')  
    plt.text(x_value, y_at_x_value, f'({x_value}, {y_at_x_value:.2f})', fontsize=12, ha='right')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot of y = 4sin(x) + 7')
    plt.legend()
    plt.grid(True)
    plt.show()
    