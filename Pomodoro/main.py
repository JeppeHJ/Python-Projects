from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 10
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 7
reps = 0
work_count = 0
my_timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    reps = 0
    window.after_cancel(my_timer)
    timer.config(text="Timer")
    checkmark.config(text="")
    canvas.itemconfig(timer_text, text=f'00:00')


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        timer.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN)
    elif reps % 2 == 0:
        timer.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN)
    else:
        count_down(WORK_MIN)
        timer.config(text="Work", fg=GREEN)
        check_mark = "✔"
        checkmark.config(text=check_mark * work_count)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Jeppes Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
checkmark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
timer.grid(column=2, row=0)
checkmark.grid(column=2, row=4)

start_button = Button(text="start", command=start_timer)
reset_button = Button(text="reset", command=reset_timer)

start_button.grid(column=0, row=3)
reset_button.grid(column=3, row=3)

window.mainloop()







