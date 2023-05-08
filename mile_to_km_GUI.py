import tkinter

window = tkinter.Tk()
window.title('Mile to Km Converter')
window.minsize(width=220, height=100)
window.config(padx=40, pady=20)

def mile_to_km():
    data = round(float(input_area.get()) * 1.609, 2)
    label_answer.config(text=data)


label1 = tkinter.Label(text='Miles')
label1.grid(column=2, row=0)

input_area = tkinter.Entry(width=5)
input_area.focus()
input_area.grid(row=0, column=1)

label2 = tkinter.Label(text='is equal to')
label2.grid(column=0, row=1)
label3 = tkinter.Label(text='Km')
label3.grid(column=2, row=1)
label_answer = tkinter.Label(text='', width=5)
label_answer.grid(column=1, row=1)
button = tkinter.Button(text='Calculate', command=mile_to_km)
button.grid(row=2, column=1)




window.mainloop()

