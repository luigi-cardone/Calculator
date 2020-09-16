import tkinter as tk

root = tk.Tk()
root.title("Calculator")

###########################################################################################


# DEFINING THE FUNCTIONS OF THE BUTTONS


# GET THE FIRST NUMBER
def onClickButton(number):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + str(number))

# CLEAR BUTTON
def clearButton():
    e.delete(0, tk.END)

# ADD BUTTON
def addButton():
    num1 = e.get()
    global f_num 
    global math
    math = "addition"
    f_num = int(num1)
    e.delete(0, tk.END)

# EQUAL BUTTON
def equalButton():
    num2 = e.get()
    e.delete(0, tk.END)
    if math == "addition":
        e.insert(0, f_num + int(num2))
    if math == "subtraction":
        e.insert(0, f_num - int(num2))
    if math == "multiplication":
        e.insert(0, f_num * int(num2))
    if math == "division":
        e.insert(0, f_num / int(num2))

# SUBTRATION BUTTON
def subButton():
    num1 = e.get()
    global f_num 
    global math
    math = "subtraction"
    f_num = int(num1)
    e.delete(0, tk.END)

# MULTIPLICATION BUTTON
def mulButton():
    num1 = e.get()
    global f_num 
    global math
    math = "multiplication"
    f_num = int(num1)
    e.delete(0, tk.END)

# DIVISION BUTTON
def divButton():
    num1 = e.get()
    global f_num 
    global math
    math = "division"
    f_num = int(num1)
    e.delete(0, tk.END)


# DEFINE THE WIDGES I'M GOING TO USE
e = tk.Entry(root, width=30, borderwidth=5, font= 14)
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: onClickButton(0))
button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: onClickButton(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: onClickButton(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: onClickButton(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: onClickButton(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: onClickButton(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: onClickButton(6))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: onClickButton(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: onClickButton(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: onClickButton(9))
button_add = tk.Button(root, text="+", padx=39, pady=20, command=addButton)
button_equal = tk.Button(root, text="=", padx=98, pady=20, command=equalButton)
button_minus = tk.Button(root, text="-", padx=41, pady=20, command= subButton)
button_mul = tk.Button(root, text="X", padx=40, pady=20, command= mulButton)
button_div = tk.Button(root, text="/", padx=41, pady=20, command= divButton)
button_clear = tk.Button(root, text="clear", padx=89, pady=20, command=clearButton)


# PUT THE BUTTONS ON SCREEN

e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

button_0.grid(row=4,column=0)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_add.grid(row=5, column=0)
button_equal.grid(row=4, column=1, columnspan= 2)
button_clear.grid(row=5, column=1, columnspan= 2)

button_minus.grid(row=6, column=0)
button_mul.grid(row=6, column=1)
button_div.grid(row=6, column=2)

##################################################################################################

root.mainloop()