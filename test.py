from tkinter import *

def testMethod():
    print("do nothing")

def main():
    # print("main")

    root=Tk()
    root.iconbitmap('icon/Cpy.ico')
    root.title("Cpy")

    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    w2=width-650
    h2=height-300
    root.geometry(str(w2) + "x" + str(h2))

    menu=Menu(root)
    root.config(menu=menu)

    filemenu=Menu(menu)
    editmenu=Menu(menu)

    menu.add_cascade(label="File",menu=filemenu)
    filemenu.add_command(label="New....",command=testMethod)
    filemenu.add_command(label="Open",command=testMethod)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=testMethod)

    menu.add_cascade(label="Edit",menu=editmenu)
    editmenu.add_command(label="Copy",command=testMethod)
    editmenu.add_command(label="Cut",command=testMethod)
    editmenu.add_command(label="Paste",command=testMethod)

    menu.add_command(label="Run",command=testMethod)

    # codescroll = Scrollbar(root)
    # codescroll.pack(side=RIGHT, fill=Y)

    codeFrame=Frame(root,height=h2-300,bg="red")
    codescroll = Scrollbar(codeFrame)

    #we able to change size of frame
    codeFrame.pack_propagate(0)
    # codeFrame.pack(fill=X)

    codeT = Text(codeFrame,yscrollcommand=codescroll.set,padx=10,pady=10)
    codescroll.config(command=codeT.yview)
    codescroll.pack(side="right",fill="y")
    # codeT.config(width=10,height=10)
    codeT.pack(side="left",fill="both",expand=True)

    codeFrame.pack(fill=X)

    consoleFrame = Frame(root,bg="green")
    consolescroll = Scrollbar(consoleFrame)
    # # consoleFrame.pack_propagate(0)
    # consoleFrame.pack(fill=X,side=BOTTOM)
    #

    consoleT=Text(consoleFrame,yscrollcommand=consolescroll.set,padx=10,pady=10)
    consolescroll.config(command=consoleT.yview)
    consolescroll.pack(side="right", fill="y")
    # consoleT.config(width=10,height=15)
    # consoleT.config(state=DISABLED)
    consoleT.pack(side="left",fill="both",expand=True)

    consoleFrame.pack(fill=X)

    root.mainloop()

if __name__== "__main__": main()