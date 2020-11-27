import tkinter as tk
import binary_to_gray as btg
import gray_to_binary as gtb
import bcd as bcd
import excis_3_add_sub as excis

root = tk.Tk()
root.geometry("644x434")
btn = tk.Button(text="Binary to Gray",command=btg.G)
btn.pack()

btn = tk.Button(text="Gray to Binary",command=gtb.G)
btn.pack()

btn = tk.Button(text="BCD Addition and Subtraction",command=bcd.G)
btn.pack()

btn = tk.Button(text="Excies 3 Addition and Subtraction",command=excis.G)
btn.pack()
root.mainloop()
