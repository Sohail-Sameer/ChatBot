import datetime
import webbrowser
import random
import pyttsx3
import matplotlib.pyplot as plt
import numpy as np
import os
import math
from fractions import Fraction
import sympy as sp

# Initialize the pyttsx3 engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Define the path to the folder on the desktop
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
saved_path = os.path.join(desktop, 'Plots')

# Create the folder if it doesn't exist
if not os.path.exists(saved_path):
    os.makedirs(saved_path)

# Logging function


def write_log(content):
    # Get the current time and date
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")

    # Create a unique filename based on the current time
    log_filename = f"log_{current_date}_{current_time.replace(':', '-')}.txt"
    log_filepath = os.path.join(saved_path, log_filename)

    # Write content to the log file
    with open(log_filepath, 'w') as log_file:
        log_file.write(f"[Time] {current_time}\n")
        log_file.write(f"[Date] {current_date}\n")
        log_file.write("######\n")
        log_file.write(content)
        log_file.write("\n######\n")

    # Manage log files (keep only the most recent 3)
    manage_logs()

# Function to manage log files


def manage_logs():
    log_files = [f for f in os.listdir(saved_path) if f.startswith("log_") and f.endswith(".txt")]
    if len(log_files) > 3:
        log_files.sort(key=lambda x: os.path.getctime(os.path.join(saved_path, x)))
        for log_file in log_files[:-3]:
            os.remove(os.path.join(saved_path, log_file))


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


def factorial(n):
    return math.factorial(n)


def permutations(n, r):
    return factorial(n) / factorial(n - r)


def combinations(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


def differentiate(degree, variable, coefficients):
    """Differentiates a polynomial of given degree with respect to a specified variable."""
    x = sp.Symbol(variable)
    polynomial = sum(coeff * x**exp for exp, coeff in enumerate(coefficients[::-1]))
    derivative = sp.diff(polynomial, x)
    return derivative

# Main Program
log_content = ""

try:
    greeting = greet()
    log_content += f"Greeting: {greeting}\n"
    print(greeting)
    pyttsx3.speak(greeting)

    while True:
        log_content += "Displaying main menu\n"
        print("Choose the function")
        pyttsx3.speak("Choose the function")
        print("1) Open Link")
        print("2) Open Random Link")
        print("3) Calculator")
        pyttsx3.speak("Enter numeric choice")
        usr_input = input("Enter 1/2/3: ")
        log_content += f"User input: {usr_input}\n"

        if usr_input == '1':
            result = open_link()
            pyttsx3.speak(result)
            log_content += f"Action: {result}\n"
        elif usr_input == '2':
            pyttsx3.speak("Do you want to open a random link?")
            user_input = input("Do you want to open a random link? (yes/no): ").strip().lower()
            log_content += f"User input: {user_input}\n"
            if user_input in ["yes", "y", "yeah"]:
                result = random_open_link()
                pyttsx3.speak(result)
                log_content += f"Action: {result}\n"
            else:
                message = "Okay sir, no link will be opened."
                print(message)
                pyttsx3.speak(message)
                log_content += f"Action: {message}\n"
        elif usr_input == '3':
            log_content += "Displaying calculator menu\n"
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
            print("10. Permutations")
            print("11. Combinations")
            print("12. Logarithmic values")
            print("13. Differentiation")
            pyttsx3.speak("Enter your choice")
            choice = input("Enter choice (1 to 13): ")
            log_content += f"User choice: {choice}\n"

            if choice in ('1', '2', '3', '4', '5', '6'):
                pyttsx3.speak("Enter your first number")
                num1 = float(input("Enter first number: "))
                log_content += f"First number: {num1}\n"
                if choice in ('5', '6'):
                    if choice == '5':
                        result = square(num1)
                    else:
                        result = cube(num1)
                    pyttsx3.speak(f"The Result is {result}")
                    print("Result:", result)
                    log_content += f"Result: {result}\n"
                else:
                    pyttsx3.speak("Enter your second number")
                    num2 = float(input("Enter second number: "))
                    log_content += f"Second number: {num2}\n"
                    if choice == '1':
                        result = add(num1, num2)
                    elif choice == '2':
                        result = subtract(num1, num2)
                    elif choice == '3':
                        result = multiply(num1, num2)
                    elif choice == '4':
                        result = divide(num1, num2)
                    pyttsx3.speak(f"The Result is {result}")
                    print("Result:", result)
                    log_content += f"Result: {result}\n"
            elif choice == '7':
                pyttsx3.speak("Enter the base number, x")
                num1 = float(input("Enter the base number (x): "))
                pyttsx3.speak("Enter the exponent, n")
                num2 = float(input("Enter the exponent (n): "))
                result = exponential(num1, num2)
                pyttsx3.speak(f"The Result is {result}")
                print("Result:", result)
                log_content += f"Exponential result: {result}\n"
            elif choice == '8':
                plot_quadratic(saved_path)
                pyttsx3.speak("Quadratic Equation Plotted and Saved")
                log_content += "Quadratic Equation Plotted and Saved\n"
            elif choice == '9':
                plot_linear(saved_path)
                pyttsx3.speak("Linear Equation Plotted and Saved")
                log_content += "Linear Equation Plotted and Saved\n"
            elif choice == '10':
                pyttsx3.speak("Enter the total number of items, n")
                n = int(input("Enter the total number of items (n): "))
                pyttsx3.speak("Enter the number of items to choose, r")
                r = int(input("Enter the number of items to choose (r): "))
                result = permutations(n, r)
                pyttsx3.speak(f"The number of permutations is {result}")
                print("Number of permutations:", result)
                log_content += f"Number of permutations: {result}\n"
            elif choice == '11':
                pyttsx3.speak("Enter the total number of items, n")
                n = int(input("Enter the total number of items (n): "))
                pyttsx3.speak("Enter the number of items to choose, r")
                r = int(input("Enter the number of items to choose (r): "))
                result = combinations(n, r)
                pyttsx3.speak(f"The number of combinations is {result}")
                print("Number of combinations:", result)
                log_content += f"Number of combinations: {result}\n"
            elif choice == '12':
                pyttsx3.speak("Enter the value of x")
                f = float(input("Enter the value of x: "))
                pyttsx3.speak("Enter the value for the base")
                g = float(input("Enter the value of base(g): "))
                result = math.log(f, g)
                print(result)
                pyttsx3.speak(f"log {f} base {g} is {result}")
                log_content += f"Log result: {result}\n"
            elif choice == '13':
                pyttsx3.speak("Enter the degree of the polynomial")
                degree = int(input("Enter the degree of the polynomial: "))
                pyttsx3.speak("Enter the variable (e.g., x)")
                variable = input("Enter the variable (e.g., x): ").strip()
                coefficients = []
                for i in range(degree, -1, -1):
                    pyttsx3.speak(f"Enter the coefficient for x^{i} (as a fraction p/q or integer)")
                    coeff_input = input(f"Enter the coefficient for x^{i} (e.g., 3/4 or 2): ").strip()
                    try:
                        coefnt = Fraction(coeff_input)  # Convert input to Fraction
                    except ValueError:
                        pyttsx3.speak("Invalid fraction format. Please enter as p/q.")
                        coefnt = Fraction(input(f"Enter the coefficient for x^{i} again: ").strip())
                    coefficients.append(coefnt)

                derivative = differentiate(degree, variable, coefficients)
                pyttsx3.speak(f"The derivative is {derivative}")
                print("Derivative:", derivative)
                log_content += f"Derivative: {derivative}\n"
            else:
                error_message = "Invalid Input"
                print(error_message)
                pyttsx3.speak(error_message)
                log_content += f"Error: {error_message}\n"
        else:
            error_message = "Invalid main menu choice"
            print(error_message)
            pyttsx3.speak(error_message)
            log_content += f"Error: {error_message}\n"

        pyttsx3.speak("Do you wish to continue?")
        continue_input = input("Do you wish to continue? (yes/no): ").strip().lower()
        log_content += f"Continue input: {continue_input}\n"
        if continue_input not in ["yes", "y", "yeah"]:
            break

    pyttsx3.speak("Thank you!")
    print("Thank you!")
    log_content += "Session ended\n"

except Exception as e:
    error_message = f"An error occurred: {e}"
    print(error_message)
    pyttsx3.speak(error_message)
    log_content += f"Error: {error_message}\n"

finally:
    # Write the session's log content to a log file
    write_log(log_content)
