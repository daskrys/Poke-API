import tkinter 

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=400, height=300, relief='raised')
canvas.pack()

label = tkinter.Label(root, text='Pokemon Finder 3000')
label.config(font=('helvetica', 14))
canvas.create_window(200, 25, window=label)

label_two = tkinter.Label(root, text='Type a Pokemon')
label.config(font=('helvetica', 10))
canvas.create_window(200, 140, window=label_two)

entry = tkinter.Entry(root)
canvas.create_window(200, 140, window=entry)

def getter():
    x1 = entry.get()

    label3 = tkinter.Label(root, text='The Square Root of ' + x1 + ' is:', font=('helvetica', 10))
    canvas.create_window(200, 210, window=label3)
    
    label4 = tkinter.Label(root, text=float(x1)**0.5, font=('helvetica', 10, 'bold'))
    canvas.create_window(200, 230, window=label4, tags=("output",))

def clear():
    entry.delete(0, tkinter.END)
    canvas.delete("output")

button1 = tkinter.Button(text='Get Pokemon Location', command=getter, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas.create_window(200, 180, window=button1)

button2 = tkinter.Button(text='Clear', command=clear, bg='blue', fg='white', font=('helvetica', 9, 'bold'))
canvas.create_window(200, 260, window=button2)

root.mainloop()