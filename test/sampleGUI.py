import tkinter as tk
import tkinter.messagebox as msg

root = tk.Tk()

# buttonClick
def showAlert():
    res = msg.askokcancel("タイトル", edt.get())
    if (res == True):
        lbl["text"] = "ok"
    else:
        lbl["text"] = "cancel"

root.title("MyGUIApp")
root.geometry("300x200")

btn = tk.Button(root, text="click!", width="5", command=showAlert)
lbl = tk.Label(root, text="Label!", foreground="#ff0000", background="#0000ff")
edt = tk.Entry(root, width="5")
valB = tk.BooleanVar()
valB.set(True)
chk = tk.Checkbutton(root, text="チェック", variable=valB)
valI = tk.IntVar()
valI.set(0)
rdo1 = tk.Radiobutton(root, text="項目１",variable=valI, value=0)
rdo2 = tk.Radiobutton(root, text="項目２",variable=valI, value=1)
rdo3 = tk.Radiobutton(root, text="項目３",variable=valI, value=2)

btn.place(x=100, y=100)
lbl.grid(row=0,column=0)
edt.grid(row=1,column=0)
chk.grid(row=1,column=1)
rdo1.grid(row=2,column=0)
rdo2.grid(row=2,column=1)
rdo3.grid(row=2,column=2)

root.mainloop()