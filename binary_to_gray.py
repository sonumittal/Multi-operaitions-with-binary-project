import tkinter as t
def G():
    w = t.Toplevel()
    w.title("Binary To Gray")
    w.geometry("444x234")
    en = t.Entry(w)
    en.pack()
    out = t.Entry(w)
    l=t.Label(w,fg="red")
    l.pack()
    btn = t.Button(w,text="Calculate",command=lambda:binary_to_gray(en.get(),out,l))
    #out.insert(t.END,"daskj")
    btn.pack()
    out.pack()
    t.mainloop()
def binary_to_gray(n,out,error):
    if not n.isdigit():
        error.configure(text="invalid input")
        return
    for x in n:
        if(x!='1' and x!='0'):
            error.configure(text="invalid input")
            return
            
    error.configure(text="")
    """Convert Binary to Gray codeword and return it."""
    n = int(n, 2) # convert to int mean convert binary to decimal
    n ^= (n >> 1)
  
    # bin(n) returns n's binary representation with a '0b' prefixed
    # the slice operation is to remove the prefix
    out.delete(0,t.END)
    out.insert(t.END,bin(n)[2:])
