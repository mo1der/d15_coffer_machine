# from tkinter import *
#
#
# def button_clicked():
#     new_tekst = float(input.get())
#     km = new_tekst * 1.60934
#     my_label3.config(text=f"{km}")
#
#
# window = Tk()
# window.title("Mile to Km Converter")
# window.minsize(width=250, height=100)
# window.config(padx=20, pady=20)
#
# my_label = Label(text="is equal to", font=("Arial", 14, "bold"))
# # my_label.config(padx=20, pady=20)
# my_label.grid(row=2, column=1)
#
# input = Entry(width=7)
# input.grid(row=1, column=2)
# # input.config(padx=5, pady=5)
#
# my_label2 = Label(text="Miles", font=("Arial", 14, "bold"))
# # my_label2.config(padx=20, pady=20)
# my_label2.grid(row=1, column=3)
#
# my_label3 = Label(text="0", font=("Arial", 8, "bold"))
# # my_label3.config(width=5, padx=20, pady=20)
# my_label3.grid(row=2, column=2)
#
#
# my_label4 = Label(font=("Arial", 14, "bold"))
# # my_label4.config(padx=20, pady=20)
# my_label4.grid(row=2, column=2)
#
# button = Button(text="Calculate", command=button_clicked)
# button.grid(row=3, column=2)
#
#
# window.mainloop()


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
from tkinter import *
reps = 0
check_marks_string = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #




# ---------------------------- UI SETUP ------------------------------- #

import math

def button_reset():
    global reps
    global timer
    reps = 0
    title_label.config(text="Timer")
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")



def button_start():
    global reps

    work_sec = WORK_MIN * 1
    short_break_sec = SHORT_BREAK_MIN * 1
    long_break_sec = LONG_BREAK_MIN * 1

    if reps == 0 or reps == 2 or reps == 4 or reps == 6:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
        reps += 1
    elif reps == 1 or reps == 3 or reps == 5:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
        reps += 1
    else:
        title_label.config(text="Long break", fg=RED)
        count_down(long_break_sec)
        reps = 0
        global check_marks_string
        check_marks_string = ""
        check_marks.config(text=check_marks_string)

def count_down(count):
    minutes = math.floor(count/60)
    seconds = count - minutes * 60
    global check_marks_string

    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}") # po zmiennej argumenty jakie chcemy zmienić
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1) # po wywołaniu funkcji dajemy wartości parametrów
    else:
        button_start()
        if (reps - 1) % 2 == 0:
            check_marks_string += "✔"
            check_marks.config(text=check_marks_string)

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", font=(FONT_NAME, 29, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 134, text="00:00", fill="white", font=(FONT_NAME, 29, "bold"))
canvas.grid(row=1, column=1)


start_button = Button(text="Start", command=button_start, width=10, highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=button_reset, width=10, highlightthickness=0)
reset_button.grid(row=2, column=2)


check_marks = Label(font=(FONT_NAME, 12, "bold"), fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)

window.mainloop()
