import tkinter as t
def G():
    w=t.Toplevel()
    w.title("Gray To Binary")
    w.geometry("444x232")
    en = t.Entry(w)
    en.pack()
    out=t.Entry(w)
    l=t.Label(w,fg="red")
    l.pack()
    btn=t.Button(w,text="Calculate",command=lambda:gray_to_binary(en.get(),out,l))
    btn.pack()
    out.pack()
    t.mainloop()
def gray_to_binary(n,out,error):
    if not n.isdigit():
        error.configure(text="invalid input")
        return
    for x in n:
        if(x!='1' and x!='0'):
            error.configure(text="invalid input")
            return


    
    """Convert Gray codeword to binary and return it."""
    n = int(n, 2) # convert to int with base 2
 
    mask = n
    while mask != 0:
        mask >>= 1
        n ^= mask
 
    # bin(n) returns n's binary representation with a '0b' prefixed
    # the slice operation is to remove the prefix
    out.delete(0,t.END)
    out.insert(t.END,bin(n)[2:])
