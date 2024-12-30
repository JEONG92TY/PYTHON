import tkinter as tk
#from tkinter import *

root = tk.Tk()
root.title("윈도우 프로그래밍 연습")
root.geometry("640x480+600+300")
#============================================================================
#label = tk.Label(root, text="Hi")
#label.pack(side="left")

#label1 = tk.Label(root, text="TOP", bg="red", fg="white")
#label1.pack(side="top", fill="x", padx=20, pady=20)
#
#label2 = tk.Label(root, text="BOTTOM", bg="blue", fg="white")
#label2.pack(side="bottom", fill="x", padx=20, pady=20)
#
#label3 = tk.Label(root, text="LEFT", bg="green", fg="white")
#label3.pack(side="left", fill="y", padx=20, pady=20)
#
#label4 = tk.Label(root, text="RIGHT", bg="yellow", fg="black")
#label4.pack(side="right", fill="y", padx=20, pady=20)
#
#label5 = tk.Label(root, text="CNETER", bg="purple", fg="white")
#label5.pack(side="top", fill="both", expand=True, padx=20, pady=20)
#============================================================================
#label1 = tk.Label(root, text="label1", bg="red", fg="white")
#label1.grid(row=0, column=0, padx=20, pady=20)
#
#label2 = tk.Label(root, text="label2", bg="blue", fg="white")
#label2.grid(row=0, column=1, padx=20, pady=20)
#
#label3 = tk.Label(root, text="label3", bg="green", fg="white")
#label3.grid(row=1, column=0, padx=20, pady=20)
#
#label4 = tk.Label(root, text="label4", bg="purple", fg="white")
#label4.grid(row=1, column=1, padx=20, pady=20)
#
#label5 = tk.Label(root, text="label5", bg="yellow", fg="black")
#label5.grid(row=0, column=2, rowspan=2, padx=20, pady=20)
#
#label6 = tk.Label(root, text="label6", bg="black", fg="white")
#label6.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

#label1 = tk.Label(root, text="hi", font=("Pretendard", 20), fg="blue")
#label1.pack()
#============================================================================
#def on_click() :
#    print("Button Click")
#
#button = tk.Button(root, text="Click", comman=on_click)
#button.pack()
#============================================================================
def show_text() :
    entried = entry.get()
    label.config(text=f"입력된 문자는 : {entried}")
    entry.delete(0, tk.END)
    print(text.get("1.0", tk.END))

entry = tk.Entry(root, width=30)
entry.pack()
text = tk.Text(root, width=40, height=10)
text.pack()
button = tk.Button(root, text="Click", command=show_text)
button.pack(side="left")
#
label = tk.Label(root, text="")
label.pack()

#top_frame = tk.Frame(root, bg="lightblue")
#top_frame.pack(fill="x")
#tk.Label(top_frame, text="top_frame").pack(pady=30)
#
#bottom_frame = tk.Frame(root, bg="lightgreen")
#bottom_frame.pack(fill="both", expand=True)
#tk.Label(bottom_frame, text="bottom_frame").pack()
#============================================================================
#def show_choice() :
#    print("선택 : " , var.get())
#    
#var = tk.StringVar(value="option1")
#
#radio1 = tk.Radiobutton(root, text="op1", variable=var, value="option1", command=show_choice)
#radio1.pack(pady=10)
#
#radio2 = tk.Radiobutton(root, text="op2", variable=var, value="option2", command=show_choice)
#radio2.pack(pady=10)
#============================================================================
#def show_selected() :
#    selection = listbox.curselection()
#    if selection :
#        print(f"selected fruit : {listbox.get(selection[0])}")
#    
#listbox = tk.Listbox(root)
#listbox.pack(pady=10)
#
#for item in ["apple", "banana", "grape", "cherry"] :
#    listbox.insert(tk.END, item)
#
#button = tk.Button(root, text="select", command=show_selected)
#button.pack(pady=10)
#============================================================================
from tkinter import messagebox

#def show_info() :
#    messagebox.showinfo("warning", "message popup")
#button  = tk.Button(root, text="show info", command=show_info)
#button.pack(pady=10)
#============================================================================
#def new_file() :
#    messagebox.showinfo("menu", "file selected")
#
#def exit_file() :
#    root.quit()
#
#menubar = tk.Menu(root)
#
#filemenu = tk.Menu(menubar, tearoff=0)
#
#filemenu.add_command(label="New", command=new_file)
#filemenu.add_separator()
#filemenu.add_command(label="Exit", command=exit_file)
#
#menubar.add_cascade(label="file", menu=filemenu)
#
#root.config(menu=menubar)
#============================================================================






root.mainloop()
