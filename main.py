from tkinter import *
FONT = ("Calibri", 16, "normal")


window = Tk()
window.title("Mile to KM Converter")
window.minsize(height=100, width=300)
window.config(padx=20, pady=20)
km = 0

entry = Entry(width=10)
entry.grid(row=0, column=1)


def calculate():
    global km
    user_input = float(entry.get())
    mile = user_input * 1.61
    kilo_meter.config(text=int(mile)

miles = Label(text=f"   Miles", font=FONT)
miles.grid(row=0, column=2)

equals = Label(text=f"is equal to", font=FONT)
equals.grid(row=1, column=0)

kilo_meter = Label(text=f"{km}", font=FONT)
kilo_meter.grid(row=1, column=1)
kilo_meter.config(padx=10, pady=10)

unit = Label(text=f" KM", font=FONT)
unit.grid(row=1, column=2)

button = Button(text='Submit', command=calculate)
button.grid(row=2, column=1)

window.mainloop()
