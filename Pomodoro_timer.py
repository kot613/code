import tkinter

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
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    global timer, reps
    reps = 0
    window.after_cancel(timer)
    label_title.config(text='Timer', foreground=GREEN)
    canvas.itemconfig(timer_text, text='00:00')
    label_check.config(text='')


# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_start():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        label_title.config(text='Break', foreground=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        label_title.config(text='Break', foreground=PINK)

    else:
        count_down(WORK_MIN * 60)
        label_title.config(text='Work', foreground=GREEN)

    # count_down(LONG_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    text = f"{count_min:02}:{count_sec:02}" if count >= 60 else f"{count_sec:02}"
    canvas.itemconfig(timer_text, text=text)
    if count:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        timer_start()
        mark = ''
        work_sessions = reps // 2
        for _ in range(work_sessions):
            mark += '✔'
        label_check.config(text=mark, foreground=GREEN)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Pomodoro')
window.config(pady=100, padx=100, bg=YELLOW)

label_title = tkinter.Label(text='Timer', foreground=GREEN, background=YELLOW, font=(FONT_NAME, 35, 'bold'))
label_title.grid(row=0, column=1)

label_check = tkinter.Label(text='', foreground=GREEN, background=YELLOW, font=(FONT_NAME, 10, 'bold'))
label_check.grid(row=3, column=1)

button_start = tkinter.Button(text='Start', command=timer_start, width=8, highlightthickness=0)
button_start.grid(row=2, column=0)

button_reset = tkinter.Button(text='Reset', command=timer_reset, width=8, highlightthickness=0)
button_reset.grid(row=2, column=2)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = tkinter.PhotoImage(file='data/tomato_28.png')
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

window.mainloop()
