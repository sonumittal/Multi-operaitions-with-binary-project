import tkinter as t
def G():
    w = t.Toplevel()
    w.title("BCD Addition and Subtraction")
    w.geometry("444x234")
    input1=t.Label(w,text="Enter First Value: ")
    input1.pack()
    en1 = t.Entry(w)
    en1.pack()

    input2=t.Label(w,text="Enter Second Value: ")
    input2.pack()
    en2 = t.Entry(w)
    en2.pack()
    
    add_out_dec = t.Entry(w)
    add_out_bin = t.Entry(w)
    
    sub_out_dec = t.Entry(w)
    sub_out_bin = t.Entry(w)
    
    l=t.Label(w,fg="red")
    l.pack()
    
    btn = t.Button(w,text="Calculate",command=lambda:bcd(en1.get(),en2.get(),add_out_dec,add_out_bin,sub_out_dec,sub_out_bin,l))
    #out.insert(t.END,"daskj")
    btn.pack()

    out_add=t.Label(w,text="Addition is: ")
    out_add.pack()
    add_out_dec.pack()
    add_out_bin.pack()

    out_sub=t.Label(w,text="Subtraction is: ")
    out_sub.pack()
    sub_out_dec.pack()
    sub_out_bin.pack()
    t.mainloop()




def bcd(n1,n2,add_dec,add_bin,sub_dec,sub_bin,error):
    a=n1
    if not a.isdigit():
        error.configure(text="invalid input")
        return
    b=n2
    if not b.isdigit():
        error.configure(text="invalid input")
        return
    else:
        a=int(a);
        b=int(b);
        if a<b:
            error.configure(text="invalid input, Enter 2nd value lessthan 1st value")
            return 
        c=a+b;
        d=a-b;
        c=str(c);
        d=str(d);
        l1=[]
        l2=[]
        ##-------addition----------------
        add_dec.delete(0,t.END)
        add_dec.insert(t.END,int(c))
        for x in c:
            l1.append((format(int(x),'#06b')[2:]))
        add_bin.delete(0,t.END)
        add_bin.insert(t.END,l1)
        ##----------subtraction----------
        sub_dec.delete(0,t.END)
        sub_dec.insert(t.END,int(d))
        for x in d:
            l2.append((format(int(x),'#06b')[2:]))
        sub_bin.delete(0,t.END)
        sub_bin.insert(t.END,l2)
