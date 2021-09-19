from tkinter import *

root = Tk()
root.title("Calculator")
root.config(background="#000000")
icon = PhotoImage(file='logo.png')
root.iconphoto(True, icon)


def on_click(number):
    current = text_area.get()
    text_area.delete(0, END)
    text_area.insert(0, str(current) + str(number))


def button_clear():
    text_area.delete(0, END)


def button_add():
    first_number = text_area.get()
    global fi_num
    global math
    math = "Addition"
    fi_num = int(first_number)
    text_area.delete(0, END)


def button_sub():
    first_number = text_area.get()
    global fi_num
    global math
    math = "Subtraction"
    fi_num = int(first_number)
    text_area.delete(0, END)


def button_mul():
    first_number = text_area.get()
    global fi_num
    global math
    math = "Multiplication"
    fi_num = int(first_number)
    text_area.delete(0, END)


def button_div():
    first_number = text_area.get()
    global fi_num
    global math
    math = "Division"
    fi_num = int(first_number)
    text_area.delete(0, END)


def button_equal():
    sec_number = text_area.get()
    text_area.delete(0, END)
    if math == "Addition":
        text_area.insert(0, fi_num + int(sec_number))

    elif math == "Subtraction":
        text_area.insert(0, fi_num - int(sec_number))

    elif math == "Multiplication":
        text_area.insert(0, fi_num * int(sec_number))

    elif math == "Division":
        text_area.insert(0, fi_num / int(sec_number))


text_area = Entry(root, width=20, borderwidth=5, justify="right", font=('large,_font', 15, 'bold'), )
text_area.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

btn1 = Button(root, text="1", padx=20, pady=20, command=lambda: on_click(1), bg='#ADD8E6').grid(row=1, column=0, pady=5)
btn2 = Button(root, text="2", padx=20, pady=20, command=lambda: on_click(2), bg='#ADD8E6').grid(row=1, column=1)
btn3 = Button(root, text="3", padx=20, pady=20, command=lambda: on_click(3), bg='#ADD8E6').grid(row=1, column=2)

btn4 = Button(root, text="4", padx=20, pady=20, command=lambda: on_click(4), bg='#ADD8E6').grid(row=2, column=0, pady=5)
btn5 = Button(root, text="5", padx=20, pady=20, command=lambda: on_click(5), bg='#ADD8E6').grid(row=2, column=1)
btn6 = Button(root, text="6", padx=20, pady=20, command=lambda: on_click(6), bg='#ADD8E6').grid(row=2, column=2)

btn7 = Button(root, text="7", padx=20, pady=20, command=lambda: on_click(7), bg='#ADD8E6').grid(row=3, column=0, pady=5)
btn8 = Button(root, text="8", padx=20, pady=20, command=lambda: on_click(8), bg='#ADD8E6').grid(row=3, column=1)
btn9 = Button(root, text="9", padx=20, pady=20, command=lambda: on_click(9), bg='#ADD8E6').grid(row=3, column=2)
btn0 = Button(root, text="0", padx=20, pady=20, command=lambda: on_click(0), bg='#ADD8E6').grid(row=4, column=1, pady=5)

btn_add = Button(root, text="+", padx=20, pady=20, command=button_add, bg='#00FF00').grid(row=3, column=3)
btn_equal = Button(root, text="=", padx=20, pady=20, command=button_equal, bg='#008000').grid(row=4, column=3)
btn_dev = Button(root, text="/", padx=20, pady=20, command=button_div, bg='#00FF00').grid(row=4, column=0)
btn_mul = Button(root, text="x", padx=21, pady=20, command=button_mul, bg='#00FF00').grid(row=2, column=3)
btn_clear = Button(root, text="Clr", padx=16.5, pady=20, command=button_clear, bg='red').grid(row=1, column=3)
btn_sub = Button(root, text="-", padx=22, pady=20, command=button_sub, bg='#00FF00').grid(row=4, column=2)

root.mainloop()
