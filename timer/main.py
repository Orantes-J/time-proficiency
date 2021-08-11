from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
CHECK_MARK = "✔"
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    pop_screen.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    check_button.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 8:
        print(f"You get a long break, number is 2 {reps}")
        countdown(long_break_sec)
        timer_label.config(text="Break Time 2", fg=PINK)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break Time 1", fg=PINK)
        print(f"short break, number is {reps}")
    else:
        print(f"work time, number is {reps}")
        timer_label.config(text="Work Time", fg=GREEN)
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(count):
    global timer
    count_min = math.floor(count/60)
    seconds_left = count % 60
    if seconds_left < 10:
        seconds_left = f"0{seconds_left}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{seconds_left}")
    if count > 0:
        timer = pop_screen.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks += "✔"
        check_button.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

# SCREEN SETTINGS
pop_screen = Tk()
pop_screen.title("My Timer")
pop_screen.config(padx=100, pady=50, bg=YELLOW)

# TIMER LABEL
timer_label = Label(text="Timer", font=(FONT_NAME, 40, 'bold'), bg=YELLOW, fg=GREEN)
timer_label.grid(row=1, column=1)

# START BUTTON
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=3, column=0)

# CHECK BUTTON
check_button = Label(font=(FONT_NAME, 10, "bold"), bg=YELLOW, fg=GREEN)
check_button.grid(row=3, column=1)

#  RESTART BUTTON
restart_button = Button(text="Reset", command=reset_timer)
restart_button.grid(row=3, column=2)

# CANVAS SETTINGS
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# in order to set an image as a background you must get it read by the PhotoImage class
# and then save it into a variable to pass as a argument
tomato_pic = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_pic)
timer_text = canvas.create_text(100, 130,  fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=1)
pop_screen.mainloop()
