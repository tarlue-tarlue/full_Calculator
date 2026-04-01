import tkinter


# the window setup
window = tkinter.Tk()
window.geometry("550x680")
window.title("Calculator")
window.configure(background="#1C1C1C")
window.resizable(False, False)


# these three variables keep track of what the user is doing
current_input = ""
stored_number = None
operator = None


# the display screen at the top
screen = tkinter.Entry(window, width=22, font=("Arial", 28), background="#1C1C1C", foreground="white", borderwidth=0, justify="right")
screen.grid(row=0, column=0, columnspan=4, pady=20, padx=15, sticky="ew")


# the frame that holds all the buttons
button_tray = tkinter.Frame(window, background="#1C1C1C")
button_tray.grid(row=1, column=0, padx=10, pady=5)


# when the user presses a number, add it to the screen
def press_number(number):
    global current_input
    current_input = current_input + str(number)
    screen.delete(0, tkinter.END)
    screen.insert(0, current_input)


# when the user presses an operator like + or -, save the number and wait for the next one
def press_operator(op):
    global current_input, stored_number, operator
    if current_input == "":
        return
    stored_number = float(current_input)
    operator = op
    current_input = ""
    screen.delete(0, tkinter.END)


# when the user presses %, convert the current number to a percentage
def press_percent():
    global current_input
    if current_input == "":
        return
    result = float(current_input) / 100
    current_input = str(result)
    screen.delete(0, tkinter.END)
    screen.insert(0, current_input)


# when the user presses +/-, flip the number between positive and negative
def press_toggle_sign():
    global current_input
    if current_input == "":
        return
    if current_input.startswith("-"):
        current_input = current_input[1:]
    else:
        current_input = "-" + current_input
    screen.delete(0, tkinter.END)
    screen.insert(0, current_input)


# when the user presses =, do the math and show the answer
def press_equal():
    global current_input, stored_number, operator
    if stored_number is None or operator is None or current_input == "":
        return

    second_number = float(current_input)

    if operator == "+":
        result = stored_number + second_number

    if operator == "-":
        result = stored_number - second_number

    if operator == "x":
        result = stored_number * second_number

    if operator == "/":
        if second_number == 0:
            screen.delete(0, tkinter.END)
            screen.insert(0, "Error")
            current_input = ""
            stored_number = None
            operator = None
            return
        result = stored_number / second_number

    # if the result is a whole number, show it without the .0
    if result == int(result):
        result = int(result)

    current_input = str(result)
    stored_number = None
    operator = None
    screen.delete(0, tkinter.END)
    screen.insert(0, current_input)


# when the user presses AC, clear everything and start fresh
def press_clear():
    global current_input, stored_number, operator
    current_input = ""
    stored_number = None
    operator = None
    screen.delete(0, tkinter.END)


# row 0 - the top row: AC, +/-, %, divide
button_ac = tkinter.Button(button_tray, text="AC", width=5, height=2, background="#D4D4D2", fg="#1C1C1C", font=("Arial", 30), borderwidth=0, command=press_clear)
button_ac.grid(row=0, column=0, pady=2, padx=2)

button_sign = tkinter.Button(button_tray, text="+/-", width=5, height=2, background="#D4D4D2", fg="#1C1C1C", font=("Arial", 25), borderwidth=0, command=press_toggle_sign)
button_sign.grid(row=0, column=1, pady=2, padx=2)

button_percent = tkinter.Button(button_tray, text="%", width=5, height=2, background="#D4D4D2", fg="#1C1C1C", font=("Arial", 30), borderwidth=0, command=press_percent)
button_percent.grid(row=0, column=2, pady=2, padx=2)

button_divide = tkinter.Button(button_tray, text="÷", width=5, height=2, background="#FF9500", fg="white", font=("Arial", 30), borderwidth=0, command=lambda: press_operator("/"))
button_divide.grid(row=0, column=3, pady=2, padx=2)


# row 1 - numbers 7, 8, 9 and multiply
button_7 = tkinter.Button(button_tray, text="7", width=5, height=2, background="#505050", fg="white", font=("Arial", 30), borderwidth=0, command=lambda: press_number("7"))
button_7.grid(row=1, column=0, pady=2, padx=2)

button_8 = tkinter.Button(button_tray, text="8", width=5, height=2, background="#505050", fg="white", font=("Arial", 30), borderwidth=0, command=lambda: press_number("8"))
button_8.grid(row=1, column=1, pady=2, padx=2)

button_9 = tkinter.Button(button_tray, text="9", width=5, height=2, background="#505050", fg="white", font=("Arial", 30), borderwidth=0, command=lambda: press_number("9"))
button_9.grid(row=1, column=2, pady=2, padx=2)

button_multiply = tkinter.Button(button_tray, text="×", width=5, height=2, background="#FF9500", fg="white", font=("Arial", 30), borderwidth=0, command=lambda: press_operator("x"))
button_multiply.grid(row=1, column=3, pady=2, padx=2)


# row 2 - numbers 4, 5, 6 and subtract
button_4 = tkinter.Button(button_tray, text="4", width=5, height=2, background="#505050", fg="white", font=("Arial", 30), borderwidth=0, command=lambda: press_number("4"))
button_4.grid(row=2, column=0, pady=2, padx=2)

button_5 = tkinter.Button(button_tray, text="5", width=5, height=2, background="#505050", fg="white", font=("Arial", 30), borderwidth=0, command=lambda: press_number("5"))
button_5.grid(row=2, column=1, pady=2, padx=2)

button_6 = tkinter.Button(button_tray, text="6", width=5, height=2, background="#505050", fg="white", font=("Arial", 30), borderwidth=0, command=lambda: press_number("6"))
button_6.grid(row=2, column=2, pady=2, padx=2)

button_subtract = tkinter.Button(button_tray, text="−", width=5, height=2, background="#FF9500", fg="white", font=("Arial", 30), borderwidth=0, command=lambda: press_operator("-"))
button_subtract.grid(row=2, column=3, pady=2, padx=2)


# row 3 - numbers 1, 2, 3 and add
button_1 = tkinter.Button(button_tray, text="1", width=5, height=2, background="#505050", fg="white", font=("Arial", 30), borderwidth=0, command=lambda: press_number("1"))
button_1.grid(row=3, column=0, pady=2, padx=2)

button_2 = tkinter.Button(button_tray, text="2", width=5, height=2, background="#505050", fg="white", font=("Arial", 30), borderwidth=0, command=lambda: press_number("2"))
button_2.grid(row=3, column=1, pady=2, padx=2)

button_3 = tkinter.Button(button_tray, text="3", width=5, height=2, background="#505050", fg="white", font=("Arial", 30), borderwidth=0, command=lambda: press_number("3"))
button_3.grid(row=3, column=2, pady=2, padx=2)

button_add = tkinter.Button(button_tray, text="+", width=5, height=2, background="#FF9500", fg="white", font=("Arial", 30), borderwidth=0, command=lambda: press_operator("+"))
button_add.grid(row=3, column=3, pady=2, padx=2)


# row 4 - zero (wide), decimal point, and equals
button_0 = tkinter.Button(button_tray, text="0", width=11, height=2, background="#505050", fg="white", font=("Arial", 30), borderwidth=0, command=lambda: press_number("0"))
button_0.grid(row=4, column=0, columnspan=2, pady=2, padx=2, sticky="ew")

button_dot = tkinter.Button(button_tray, text=".", width=5, height=2, background="#505050", fg="white", font=("Arial", 30), borderwidth=0, command=lambda: press_number("."))
button_dot.grid(row=4, column=2, pady=2, padx=2)

button_equal = tkinter.Button(button_tray, text="=", width=5, height=2, background="#FF9500", fg="white", font=("Arial", 30), borderwidth=0, command=press_equal)
button_equal.grid(row=4, column=3, pady=2, padx=2)


window.mainloop()