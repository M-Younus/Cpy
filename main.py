
from lexical import Lexical


import re


class Main():

    _temp = "";_lineNum = 1;_codeFile="code.txt";_outputFile="output.txt";_fileData=""

    _breakers = ['(', ')', '[', ']', '{', '}', '=', ',', ' ', '\n', '\r'
        , '<', '>', '-', '+', '*', '/', '%', ':', ';', '.', '!', '&', '|', '#' , '"' , '\'' , '\t']

    _invalidPrint = ['=', ' ', '\n', '\r', '<', '>', '-', '+', '*', '/', '%', '!', '&', '|', '#' , '"' , '\'' , '\t']


    def __init__(self):
        Main._fileData=""
        Main._lineNum=1

    def mainMethod(self,f):
        lex = Lexical()

        self.flagStr=0;self.flagChar=0;self.flagFloat=0

        while True:
            ch = str(f.read(1), 'utf-8')

            if not ch: break

            # working for separation of float and ID

            if ch == '.':
                if self.flagFloat:
                    if lex.chk_FLT_CONST(Main._temp, Main._lineNum):
                        self.printToken("FLT_CONST", Main._temp, Main._lineNum)
                        f.seek(-1,1)
                        Main._temp = ""
                        self.flagFloat=0
                        continue
                elif Main._temp=="":
                    OneRight = str(f.read(1), 'utf-8')
                    if re.match("[0-9]",OneRight):
                        self.flagFloat=1
                        Main._temp+=ch+OneRight
                        continue
                    else:
                        f.seek(-1,1)
                elif Main._temp!="":
                    f.seek(-2, 1)
                    OneLeft = str(f.read(1), 'utf-8')
                    f.seek(1, 1)
                    OneRight = str(f.read(1), 'utf-8')
                    if (re.match("[0-9]", OneLeft) or OneLeft in ['+', '-']) and re.match("[0-9]", OneRight):
                        self.flagFloat=1
                        Main._temp += ch+OneRight
                        continue
                    else:
                        f.seek(-1,1)

            elif ch == '+' or ch == '-':
                OneRight = str(f.read(1), 'utf-8')
                TwoRight = str(f.read(1), 'utf-8')
                f.seek(-2, 1)
                if re.match("[0-9]", OneRight) or re.match("[0-9]", TwoRight):
                    Main._temp += ch
                    continue

            if ch in Main._breakers:

                if ch =='"' and self.flagStr==1:
                    Main._temp+=ch


                if lex.chk_FLT_CONST(Main._temp, Main._lineNum):
                    self.printToken("FLT_CONST", Main._temp, Main._lineNum)
                    self.flagFloat=0
                    Main._temp = ""

                if lex.chk_keywords(Main._temp, Main._lineNum):
                    self.printToken(Main._temp,"-", Main._lineNum)
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
                    self.printToken("STR_CONST", Main._temp[1:-1], Main._lineNum)
                    Main._temp = ""

                elif Main._temp != "":
                    Main._temp = "Error at " + str(Main._lineNum) + " where value is " + Main._temp
                    Main._fileData += Main._temp + "\n"
                    Main._temp = ""

                if ch not in Main._invalidPrint and ch!='':
                    self.printToken(str(ch), '-', Main._lineNum)
                if ch == '\n':
                    Main._lineNum += 1


            else:
                Main._temp += str(ch)

            if ch == '"':
                Main._temp+=ch
                while True:
                    ch = str(f.read(1), 'utf-8')
                    if ch =='\\':
                        OneRight = str(f.read(1), 'utf-8')
                        if OneRight=='"' or OneRight=='\\':
                            Main._temp += OneRight
                        else:
                            f.seek(-1, 1)
                            Main._temp += ch
                    elif ch not in ['"','\n']:
                        Main._temp+=ch
                    elif ch == '"':
                        f.seek(-1,1)
                        self.flagStr = 1
                        break
                    elif ch == '\n':
                        f.seek(-1, 1)
                        break

            if ch == '\'':
                Main._temp+=ch
                char1 = str(f.read(1), 'utf-8')
                char2 = str(f.read(1), 'utf-8')

                if char1=='\\':
                    char3 = str(f.read(1), 'utf-8')
                    if char2=='\'':
                        Main._temp += char2 + char3
                    elif char3!='\n':
                        Main._temp += char1 + char2 + char3
                    else:
                        Main._temp += char1
                    if char3=='\n':
                        Main._lineNum+=1
                elif char2!='\n':
                    Main._temp += char1 + char2
                elif char2 == '\n':
                    Main._lineNum += 1


                if lex.chk_CHAR_CONST(Main._temp, Main._lineNum):
                    self.printToken("CHAR_CONST", Main._temp[1:-1], Main._lineNum)
                    Main._temp = ""
                else:
                    Main._temp = "Error at " + str(Main._lineNum) + " where value is " + Main._temp
                    Main._fileData += Main._temp + "\n"
                    Main._temp = ""


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
                elif ch == '!':
                    f.seek(-1, 1)
                    self.printToken("LO", str(ch), Main._lineNum)
                    # self.printToken("LO", str(ch), Main._lineNum)

            # check for LO
            if ch in ['&', '|']:
                OneRight = str(f.read(1), 'utf-8')
                if ch == OneRight:
                    Main._temp = ch + OneRight
                    self.printToken("LO", Main._temp, Main._lineNum)
                    Main._temp = ""
                elif ch != OneRight:
                    temp = "Error at " + str(Main._lineNum) + " where value is " + str(ch)
                    Main._fileData += temp + "\n"
                    f.seek(-1, 1)
                    Main._temp = ""


    def printToken(self,CPart, VPart, line):
        string = "( " + CPart + " , " + VPart + " , " + str(line) + " )"
        print(string)
        Main._fileData += string + "\n"

