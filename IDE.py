from tkinter import *

from syntax import Syntax

from semantic import Semantic

from main import Main

class IDE():

    def Run(self,event=0):

        self.objMain=Main()

        self.consoleT.delete(1.0,END)

        #open file and write all the IDE code text area content
        self.codeFile = open(Main._codeFile, 'w')
        self.codeFile.write(self.codeT.get('1.0', END))
        self.codeFile.close()

        #open file for reading
        self.codeFile = open(Main._codeFile, 'rb+')
        self.objMain.mainMethod(self.codeFile)
        self.codeFile.close()

        #write tokens to console area
        self.consoleT.insert(1.0, Main._fileData)

        #write tokens to test file
        self.outputFile = open(Main._outputFile, 'w')
        self.outputFile.write(Main._fileData)
        self.outputFile.close()

        #call syntax
        # self.objMain.PROG()

        self.objSyntax=Syntax(Main._tokens)
        self.objSemantic = Semantic(Main._tokens)

        if self.objSyntax.PROG():
            print("Code is parsedxxc")
        else:
            print("there is error in code")

        # if self.objSyntax.PROG():
        #     if self.objSemantic.PROG():
        #         print("Code is parsed")
        #     else:
        #         print("there is error in code")
        # else:
        #     print("there is error in code")


    def newFunc(self):
        self.codeT.delete(1.0,END)
        self.consoleT.delete(1.0, END)


    def falto(self):
        pass

    def yourFunction(self,event):
        print('left')

    def __init__(self,root):

        root.iconbitmap('icon/Cpy.ico')
        root.title("Cpy")

        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()
        self.w2=self.width-650
        self.h2=self.height-300
        root.geometry("700x650")

        self.menu=Menu(root)
        root.config(menu=self.menu)

        self.filemenu=Menu(self.menu)
        self.editmenu=Menu(self.menu)

        self.menu.add_cascade(label="File",menu=self.filemenu)
        self.filemenu.add_command(label="New....",command=self.newFunc)
        self.filemenu.add_command(label="Open",command=self.falto)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit",command=lambda :root.quit())

        self.menu.add_cascade(label="Edit",menu=self.editmenu)
        self.editmenu.add_command(label="Copy",command=self.falto)
        self.editmenu.add_command(label="Cut",command=self.falto)
        self.editmenu.add_command(label="Paste",command=self.falto)

        self.menu.add_command(label="Run",command=self.Run)

        self.codeFrame = Frame(root, height=400, bg="red")

        #bind F5 key to Run method
        root.bind("<F5>", self.Run)

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