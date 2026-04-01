# 🧮 iOS Calculator — Python Tkinter

A fully functional calculator built with **Python + Tkinter**, styled to match the Apple iOS Calculator.  
Built as a learning project while studying Python GUI development.

---

## 📸 Preview

> Dark background · Orange operators · Gray number buttons — just like the real thing.

| Button Type     | Color     | Hex       |
|-----------------|-----------|-----------|
| Background      | Black     | `#1C1C1C` |
| Number buttons  | Dark Gray | `#505050` |
| Function buttons| Light Gray| `#D4D4D2` |
| Operator buttons| Orange    | `#FF9500` |
| Text            | White     | `#FFFFFF` |

---

## ✅ Features

- Addition, subtraction, multiplication, division
- Decimal point support
- Sign flip with `+/-`
- Percentage button `%`
- All Clear button `AC`
- Divide by zero error handling
- Clean whole number display — shows `6` instead of `6.0`
- iOS-style wide `0` button that spans two columns

---

## 🚀 How to Run

**Step 1 — Make sure Python is installed**

```bash
python --version
```

> You need Python 3.x. Download it at [python.org](https://www.python.org)

**Step 2 — Clone this repo**

```bash
git clone https://github.com/your-username/ios-calculator.git
cd ios-calculator
```

**Step 3 — Run the app**

```bash
python calculator.py
```

> No extra libraries needed. Tkinter comes built into Python.

---

## 📁 Project Structure

```
ios-calculator/
│
├── calculator.py     # All the code lives here
└── README.md         # You are reading this
```

---

## 🧠 What I Learned Building This

This was my first GUI project as a beginner Python developer. Here's what I practiced:

- **`tkinter.Button`** — creating and styling buttons
- **`grid()`** — placing widgets in rows and columns
- **`columnspan`** — making the `0` button span two columns
- **`global` variables** — sharing memory between functions
- **`lambda`** — passing arguments to button `command=`
- **Functions** — writing one `make_button()` instead of repeating code 16 times
- **Error handling** — catching divide-by-zero before it crashes the app
- **`fresh_start` flag** — clearing the screen after an operator is pressed

---

## 🔧 How the Logic Works

```
User types  →  number_clicked()   saves digit to screen
User presses +  →  operator_clicked()  saves first number + operator
User types more  →  screen clears, user types second number
User presses =  →  equals_clicked()  calculates and shows result
```

---

## 🗺️ What I Want to Add Next

- [ ] Keyboard support (press `+` on keyboard instead of clicking)
- [ ] Calculation history log
- [ ] Scientific mode (sin, cos, square root)
- [ ] Animations on button press

---

## 🛠️ Built With

- [Python 3](https://www.python.org/) — programming language
- [Tkinter](https://docs.python.org/3/library/tkinter.html) — built-in Python GUI library
- Apple iOS Calculator — design inspiration

---

## 👤 Author

**Preston Tarlue**  
🐍 Beginner Python Developer  
📍 Learning GUI development with Tkinter

---

## 📄 License

This project is open source and free to use for learning purposes.
