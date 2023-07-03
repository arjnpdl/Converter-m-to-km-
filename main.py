import tkinter as tk
import ttkbootstrap as ttk

def convert():
	Float_input = entry_Strg.get()
	meter_input = float(Float_input)
	km_ouptut = meter_input / 1000
	output_Strg.set(km_ouptut)


#window
win = ttk.Window(themename = 'darkly')
win.title('Converter-dEfy(m to km)')
win.geometry('300x150')

#title
title_label = ttk.Label(master = win, text = 'Meters to Kilometers', font = 'Calibri 24 bold')
title_label.pack()

#input field
input_frame = ttk.Frame(master = win)
entry_Strg = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_Strg)
button = ttk.Button(master = input_frame, text = 'Convert', command = convert)
entry.pack(side = 'left',padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

#output
output_Strg = tk.StringVar()
output_label = ttk.Label(master = win, text = 'Output', font = 'Calibri 24', textvariable = output_Strg)
output_label.pack()

#run
win.mainloop()
