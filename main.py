import datetime
import webbrowser
import random
import pyttsx3
import matplotlib.pyplot as plt
import numpy as np
import os


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y


def square(x):
    return x ** 2


def cube(x):
    return x ** 3


def exponential(x, n):
    return x ** n


def get_unique_filename(base_path, base_filename, extension):
    counter = 1
    filename = f"{base_filename}{extension}"
    full_path = os.path.join(base_path, filename)
    while os.path.exists(full_path):
        filename = f"{base_filename}_{counter}{extension}"
        full_path = os.path.join(base_path, filename)
        counter += 1
    return full_path


def plot_quadratic(save_path):
    pyttsx3.speak("Enter coefficient a")
    a = float(input("Enter coefficient a: "))
    pyttsx3.speak("Enter coefficient b")
    b = float(input("Enter coefficient b: "))
    pyttsx3.speak("Enter constant c")
    c = float(input("Enter constant c: "))

    x = np.linspace(-10, 10, 400)
    y = a * x ** 2 + b * x + c

    discriminant = b ** 2 - 4 * a * c

    if discriminant >= 0:
        x1 = (-b + np.sqrt(discriminant)) / (2 * a)
        x2 = (-b - np.sqrt(discriminant)) / (2 * a)
        y1, y2 = 0, 0
    else:
        x1 = (-b + np.sqrt(discriminant)) / (2 * a)
        x2 = (-b - np.sqrt(discriminant)) / (2 * a)
        y1, y2 = np.imag(x1), np.imag(x2)
        x1, x2 = np.real(x1), np.real(x2)

    plt.plot(x, y, label=f'{a}x^2 + {b}x + c')
    plt.scatter([x1, x2], [y1, y2], color='red', label='X-Intercepts')
    plt.text(x1, y1, f'({round(x1, 2)}, {round(y1, 2)})', fontsize=15, ha='left', color='green')
    plt.text(x2, y2, f'({round(x2, 2)}, {round(y2, 2)})', fontsize=15, ha='right', color='green')

    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()

    # Save plot to the specified path
    unique_filename = get_unique_filename(save_path, 'quadratic_plot', '.png')
    plt.savefig(unique_filename)
    plt.close()


def plot_linear(saved_path):
    pyttsx3.speak("Enter coefficient a")
    a = float(input("Enter coefficient a: "))
    pyttsx3.speak("Enter coefficient b")
    b = float(input("Enter coefficient b: "))
    pyttsx3.speak("Enter constant c")
    c = float(input("Enter constant c: "))

    if b != 0:
        m = -a / b
        x_intercept = -c / a
        y_intercept = -c / b
    else:
        m = "Vertical line (undefined slope)"
        x_intercept = "Vertical line (no x-intercept)"
        y_intercept = -c / b

    x = np.linspace(-10, 10, 400)
    y = (-a * x - c) / b

    plt.plot(x, y, label=f'{a}x + {b}y + {c} = 0')
    plt.scatter(x_intercept, 0, color='red', label='X-Intercept')
    plt.scatter(0, y_intercept, color='blue', label='Y-Intercept')
    plt.text(x_intercept, 0, f'({round(x_intercept, 2)}, 0)', fontsize=15, ha='left', color='green')
    plt.text(0, y_intercept, f'(0, {round(y_intercept, 2)})', fontsize=15, ha='right', color='green')
    plt.text(0, 5, f'Slope (m): {m}', fontsize=12, ha='right', color='purple')

    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()

    # Save plot to the specified path
    unique_filename = get_unique_filename(saved_path, 'linear_plot', '.png')
    plt.savefig(unique_filename)
    plt.close()


def greet():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        greeting = "Good Morning Sir!"
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon Sir!"
    else:
        greeting = "Good Evening Sir!"
    return greeting


def random_open_link():
    links = [
        "quickdraw.withgoogle.com",
        "elevenlabs.io",
        "teachable-snake.netlify.app",
        "musiclab.chromeexperiments.com/Song-Maker",
        "lexica.art",
        "research.google.com/semantris",
        "g.co/arts/2WST2Pqi1fXRq1kbA"
    ]

    link_to_open = random.choice(links)
    webbrowser.open(link_to_open)
    return f"Opening {link_to_open}"


def open_link():
    youtube = 'youtube.com'
    google = 'google.com'
    chatgpt = 'chat.openai.com'
    print("1) YouTube")
    print("2) Google")
    print("3) ChatGPT")
    link_input = input("Enter the link number(1/2/3): ")
    if link_input == '1':
        webbrowser.open(youtube)
        return f"Opening {youtube}"
    elif link_input == '2':
        webbrowser.open(google)
        return f"Opening {google}"
    elif link_input == '3':
        webbrowser.open(chatgpt)
        return f"Opening {chatgpt}"
    else:
        return "Enter a valid response"


# Main Program
print(greet())
pyttsx3.speak(greet())

# Define the path to the folder on the desktop
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
saved_path = os.path.join(desktop, 'Plots')

# Create the folder if it doesn't exist
if not os.path.exists(saved_path):
    os.makedirs(saved_path)

while True:
    print("Choose the function")
    pyttsx3.speak("Choose the function")
    print("1) Open Link")
    print("2) Open Random Link")
    print("3) Calculator")
    pyttsx3.speak("Enter numeric choice")
    usr_input = input("Enter 1/2/3: ")

    if usr_input == '1':
        pyttsx3.speak(open_link())
    elif usr_input == '2':
        pyttsx3.speak("Do you want to open a random link?")
        user_input = input("Do you want to open a random link? (yes/no): ").strip().lower()
        if user_input in ["yes", "y", "yeah"]:
            pyttsx3.speak(random_open_link())
        else:
            print("Okay sir, no link will be opened.")
            pyttsx3.speak("Okay sir, no link will be opened.")
    elif usr_input == '3':
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square")
        print("6. Cube")
        print("7. Exponential")
        print("8. Plot Quadratic Equation")
        print("9. Linear Equation in Two Variables")

        pyttsx3.speak("Enter your choice")
        choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ")

        if choice in ('1', '2', '3', '4', '5', '6'):
            pyttsx3.speak("Enter your first number")
            num1 = float(input("Enter first number: "))
            if choice in ('5', '6'):
                if choice == '5':
                    pyttsx3.speak(f"The Result is {square(num1)}")
                    print("Result:", square(num1))
                else:
                    pyttsx3.speak(f"The Result is {cube(num1)}")
                    print("Result:", cube(num1))
            else:
                pyttsx3.speak("Enter your second number")
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    pyttsx3.speak(f"The Result is {add(num1, num2)}")
                    print("Result:", add(num1, num2))
                elif choice == '2':
                    pyttsx3.speak(f"The Result is {subtract(num1, num2)}")
                    print("Result:", subtract(num1, num2))
                elif choice == '3':
                    pyttsx3.speak(f"The Result is {multiply(num1, num2)}")
                    print("Result:", multiply(num1, num2))
                elif choice == '4':
                    pyttsx3.speak(f"The Result is {divide(num1, num2)}")
                    print("Result:", divide(num1, num2))
        elif choice == '7':
            pyttsx3.speak("Enter the base number, x")
            num1 = float(input("Enter the base number (x): "))
            pyttsx3.speak("Enter the exponent, n")
            num2 = float(input("Enter the exponent (n): "))
            pyttsx3.speak(f"The Result is {exponential(num1, num2)}")
            print("Result:", exponential(num1, num2))
        elif choice == '8':
            plot_quadratic(saved_path)
            pyttsx3.speak("Quadratic Equation Plotted and Saved")
        elif choice == '9':
            plot_linear(saved_path)
            pyttsx3.speak("Linear Equation Plotted and Saved")
        else:
            print("Invalid Input")
            pyttsx3.speak("Invalid Input")
    else:
        print("Enter a valid response from the dropdown")
        pyttsx3.speak("Enter a valid response from the dropdown")

    pyttsx3.speak("Do you wish to continue?")
    continue_input = input("Do you wish to continue? (yes/no): ").strip().lower()
    if continue_input not in ["yes", "y", "yeah"]:
        pyttsx3.speak("Thank you!")
        print("Thank you!")
        break
