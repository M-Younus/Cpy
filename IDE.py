from tkinter import *


class IDE():

    def consoleOutput(self):
        self.consoleT.config(state=NORMAL)
        self.consoleT.delete(1.0,END)
        self.consoleT.insert(1.0,self.codeT.get('1.0',END))
        self.consoleT.config(state=DISABLED)

    def __init__(self,root):

        root.iconbitmap('icon/Cpy.ico')
        root.title("Cpy")

        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()
        self.w2=self.width-650
        self.h2=self.height-300
        root.geometry(str(self.w2) + "x" + str(self.h2))

        self.menu=Menu(root)
        root.config(menu=self.menu)

        self.filemenu=Menu(self.menu)
        self.editmenu=Menu(self.menu)

        self.menu.add_cascade(label="File",menu=self.filemenu)
        self.filemenu.add_command(label="New....",command=self.testMethod)
        self.filemenu.add_command(label="Open",command=self.testMethod)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit",command=lambda :root.quit())

        self.menu.add_cascade(label="Edit",menu=self.editmenu)
        self.editmenu.add_command(label="Copy",command=self.testMethod)
        self.editmenu.add_command(label="Cut",command=self.testMethod)
        self.editmenu.add_command(label="Paste",command=self.testMethod)

        self.menu.add_command(label="Run",command=self.testMethod)

        self.codeFrame=Frame(root,height=self.h2-300,bg="red")
        self.codescroll = Scrollbar(self.codeFrame)

        #we able to change size of frame
        self.codeFrame.pack_propagate(0)

        self.codeT = Text(self.codeFrame,yscrollcommand=self.codescroll.set,padx=10,pady=10)
        self.codescroll.config(command=self.codeT.yview)
        self.codescroll.pack(side="right",fill="y")
        self.codeT.pack(side="left",fill="both",expand=True)

        self.codeFrame.pack(fill=X)

        self.consoleFrame = Frame(root,bg="green")
        self.consolescroll = Scrollbar(self.consoleFrame)

        self.consoleT=Text(self.consoleFrame,yscrollcommand=self.consolescroll.set,padx=10,pady=10)
        self.consolescroll.config(command=self.consoleT.yview)
        self.consolescroll.pack(side="right", fill="y")
        self.consoleT.pack(side="left",fill="both",expand=True)

        self.consoleFrame.pack(fill=X)



root=Tk()

ObjIde=IDE(root)

root.mainloop()