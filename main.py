
from lexical import Lexical


import re


class Main():

    _temp = "";_lineNum = 1;_codeFile="code.txt";_outputFile="output.txt";_fileData=""

    _breakers = ['(', ')', '[', ']', '{', '}', '=', ',', ' ', '\n', '\r'
        , '<', '>', '-', '+', '*', '/', '%', ':', ';', '.', '!', '&', '|', '#']

    _invalidPrint = ['=', ' ', '\n', '\r', '<', '>', '-', '+', '*', '/', '%', '!', '&', '|', '#']


    def mainMethod(self,f):
        lex = Lexical()

        while True:
            ch = str(f.read(1), 'utf-8')

            if not ch: break

            # working for separation of float and ID
            if ch == '.':
                f.seek(-2, 1)
                OneLeft = str(f.read(1), 'utf-8')
                f.seek(1, 1)
                OneRight = str(f.read(1), 'utf-8')
                if (re.match("[0-9]", OneLeft) or OneLeft in ['+', '-']) and re.match("[0-9]", OneRight):
                    f.seek(-1, 1)
                    Main._temp += ch
                    continue
                else:
                    f.seek(-2, 1)
                    ch = f.read(1)
                    ch = str(ch, 'utf-8')

            elif ch == '+' or ch == '-':
                OneRight = str(f.read(1), 'utf-8')
                f.seek(-1, 1)
                if re.match("[0-9]", OneRight) or OneRight == '.':
                    Main._temp += ch
                    continue

            if ch in Main._breakers:

                if lex.chk_FLT_CONST(Main._temp, Main._lineNum):
                    self.printToken("FLT_CONST", Main._temp, Main._lineNum)
                    Main._temp = ""

                if lex.chk_keywords(Main._temp, Main._lineNum):
                    self.printToken("Keyword", Main._temp, Main._lineNum)
                    Main._temp = ""

                elif lex.chk_ID(Main._temp, Main._lineNum):
                    self.printToken("ID", Main._temp, Main._lineNum)
                    Main._temp = ""

                elif lex.chk_INT_CONST(Main._temp, Main._lineNum):
                    self.printToken("INT_CONST", Main._temp, Main._lineNum)
                    Main._temp = ""

                elif lex.chk_STR_CONST(Main._temp, Main._lineNum):
                    self.printToken("STR_CONST", Main._temp, Main._lineNum)
                    Main._temp = ""

                elif lex.chk_CHAR_CONST(Main._temp, Main._lineNum):
                    self.printToken("CHAR_CONST", Main._temp, Main._lineNum)
                    Main._temp = ""

                if ch not in Main._invalidPrint:
                    self.printToken(str(ch), '-', Main._lineNum)
                if ch == '\n':
                    Main._lineNum += 1

                elif Main._temp != "":
                    Main._temp = "Error at " + str(Main._lineNum) + " where value is " + Main._temp
                    Main._fileData += Main._temp + "\n"
                    Main._temp = ""

            else:
                Main._temp += str(ch)

            # if ch =='#':
            #     OneRight = str(f.read(1), 'utf-8')
            #     if OneRight == '*':
            #         while True:
            #             first = str(f.read(1), 'utf-8')
            #             second = str(f.read(1), 'utf-8')
            #             if first == '*' and second == '#':
            #                 break
            #     else:
            #         f.readline()
            #         Lexical._lineNum+=1
            #
            #     continue


            if ch == '#':
                f.readline()
                Lexical._lineNum += 1
                continue

            # check for inc_DEc and add_sub and asgn
            if ch in ['+', '-', '*', '/', '%']:
                OneRight = str(f.read(1), 'utf-8')
                if ch == OneRight:
                    temp = ch + ch
                    self.printToken("INC_DEC", temp, Main._lineNum)
                    temp = ""
                elif OneRight == '=':
                    temp = ch + OneRight
                    self.printToken("ASGN_OPT", temp, Main._lineNum)
                    temp = ""
                elif ch in ['+', '-']:
                    f.seek(-1, 1)
                    self.printToken("ADD_SUB", str(ch), Main._lineNum)
                elif ch == '*':
                    f.seek(-1, 1)
                    self.printToken("MUL", str(ch), Main._lineNum)
                elif ch in ['/', '%']:
                    f.seek(-1, 1)
                    self.printToken("DIV_REM", str(ch), Main._lineNum)
                else:
                    f.seek(-1, 1)

            # check for RO
            if ch in ['<', '>', '=', '!']:
                OneRight = str(f.read(1), 'utf-8')
                if OneRight == '=':
                    temp = ch + OneRight
                    self.printToken("RO", temp, Main._lineNum)
                    temp = ""
                elif ch == '=':
                    f.seek(-1, 1)
                    self.printToken('=', '-', Main._lineNum)
                elif ch != '!':
                    f.seek(-1, 1)
                    self.printToken("RO", str(ch), Main._lineNum)
                else:
                    f.seek(-1, 1)

            # check for LO
            if ch in ['&', '|', '!']:
                OneRight = str(f.read(1), 'utf-8')
                if ch != '!' and ch == OneRight:
                    temp = ch + OneRight
                    self.printToken("LO", temp, Main._lineNum)
                    temp = ""
                elif ch != '!' and ch != OneRight:
                    temp = "Error at " + str(Main._lineNum) + " where value is " + str(ch)
                    Main._fileData += temp + "\n"
                    # print("Error at " + str(Lexical._lineNum) + " where value is " + str(ch))
                    f.seek(-1, 1)
                    temp = ""
                elif ch == '!':
                    f.seek(-1, 1)
                    self.printToken("LO", str(ch), Main._lineNum)

    def printToken(self,CPart, VPart, line):
        string = "( " + CPart + " , " + VPart + " , " + str(line) + " )"
        print(string)
        Main._fileData += string + "\n"


# root=Tk()
# ObjMain=Main(root)
# root.mainloop()