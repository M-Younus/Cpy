from tkinter import *

def testMethod():
    print("do nothing")

def main():
    print("main")

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

    # scrollbar = Scrollbar(root)
    # scrollbar.pack(side=RIGHT, fill=Y)

    # codeFrame=Frame(root,height=h2-300,bg="red")
    # codeFrame.pack_propagate(0)
    # codeFrame.pack(fill=X)
    #
    # codeT = Text(codeFrame)
    # codeT.config(width=10,height=10)
    # codeT.pack()

    consoleFrame = Frame(root,bg="green")
    # consoleFrame.pack_propagate(0)
    consoleFrame.pack(fill=X,side=BOTTOM)

    consoleT=Text(consoleFrame)
    consoleT.config(width=10,height=15)
    consoleT.pack()

    root.mainloop()

if __name__== "__main__": main()