
from lexical import Lexical


import re


class Main():

    _temp = "";_lineNum = 1;_codeFile="code.txt";_outputFile="output.txt";_fileData=""

    _breakers = ['(', ')', '[', ']', '{', '}', '=', ',', ' ', '\n', '\r'
        , '<', '>', '-', '+', '*', '/', '%', ':', ';', '.', '!', '&', '|', '#' , '"' , '\'']

    _invalidPrint = ['=', ' ', '\n', '\r', '<', '>', '-', '+', '*', '/', '%', '!', '&', '|', '#' , '"' , '\'']


    def __init__(self):
        Main._fileData=""
        Main._lineNum=1

    def mainMethod(self,f):
        lex = Lexical()

        self.flagStr=0;self.flagChar=0

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

                if ch =='"' and self.flagStr==1:
                    Main._temp+=ch

                if ch == '\'' and self.flagChar==1:
                    Main._temp+=ch

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
                    self.flagStr=0
                    ch=''
                    self.printToken("STR_CONST", Main._temp, Main._lineNum)
                    Main._temp = ""

                elif lex.chk_CHAR_CONST(Main._temp, Main._lineNum):
                    self.flagChar = 0
                    ch = ''
                    self.printToken("CHAR_CONST", Main._temp, Main._lineNum)
                    Main._temp = ""

                if ch not in Main._invalidPrint and ch!='':
                    self.printToken(str(ch), '-', Main._lineNum)
                if ch == '\n':
                    Main._lineNum += 1

                elif Main._temp != "":
                    Main._temp = "Error at " + str(Main._lineNum) + " where value is " + Main._temp
                    Main._fileData += Main._temp + "\n"
                    Main._temp = ""

            else:
                Main._temp += str(ch)

            if ch == '"':
                Main._temp+=ch
                while True:
                    # f.seek(-1,1)
                    # OneLeft = str(f.read(1), 'utf-8')
                    # Main._temp+=OneLeft
                    ch = str(f.read(1), 'utf-8')
                    if ch not in ['"','\n']:
                        Main._temp+=ch
                    elif ch == '"':
                        f.seek(-2, 1)
                        OneLeft = str(f.read(1), 'utf-8')
                        if OneLeft == '\\':
                            Main._temp += ch
                        else:
                            self.flagStr = 1
                            # f.seek(1, 1)
                            break
                    elif ch == '\n':
                        f.seek(-1, 1)
                        break

            if ch == '\'':
                Main._temp+=ch
                while True:
                    ch = str(f.read(1), 'utf-8')
                    if ch not in ['\'','\n']:
                        Main._temp+=ch
                    elif ch == '\'':
                        f.seek(-2, 1)
                        OneLeft = str(f.read(1), 'utf-8')
                        if OneLeft == '\\':
                            Main._temp += ch
                        else:
                            self.flagChar = 1
                            break
                    elif ch == '\n':
                        f.seek(-1, 1)
                        break


            if ch =='#':
                OneRight = str(f.read(1), 'utf-8')
                if OneRight == '*':
                    while True:
                        first = str(f.read(1), 'utf-8')
                        if not first:
                            break
                        if first == '*':
                            second = str(f.read(1), 'utf-8')
                            if second == '#':
                                break
                        elif first == '\n':
                            Main._lineNum+=1
                else:
                    f.readline()
                    Main._lineNum+=1

                continue



            # check for inc_DEc and add_sub and asgn
            if ch in ['+', '-', '*', '/', '%']:
                OneRight = str(f.read(1), 'utf-8')
                if ch == OneRight:
                    Main._temp = ch + ch
                    self.printToken("INC_DEC", Main._temp, Main._lineNum)
                    Main._temp = ""
                elif OneRight == '=':
                    Main._temp = ch + OneRight
                    self.printToken("ASGN_OPT", Main._temp, Main._lineNum)
                    Main._temp = ""
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
                    Main._temp = ch + OneRight
                    self.printToken("RO", Main._temp, Main._lineNum)
                    Main._temp = ""
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
                    Main._temp = ch + OneRight
                    self.printToken("LO", Main._temp, Main._lineNum)
                    Main._temp = ""
                elif ch != '!' and ch != OneRight:
                    temp = "Error at " + str(Main._lineNum) + " where value is " + str(ch)
                    Main._fileData += temp + "\n"
                    f.seek(-1, 1)
                    Main._temp = ""
                elif ch == '!':
                    f.seek(-1, 1)
                    self.printToken("LO", str(ch), Main._lineNum)


    def printToken(self,CPart, VPart, line):
        string = "( " + CPart + " , " + VPart + " , " + str(line) + " )"
        print(string)
        Main._fileData += string + "\n"

