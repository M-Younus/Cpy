
from lexical import Lexical

import re

def main():

    temp="";lineNum=1

    f = open('test.txt', 'rb+')

    breakers=[ '(' , ')' , '[' , ']' , '{' , '}' , '=' , ',' , ' ' , '\n' , '\r'
        , '<' , '>' , '-' , '+' , '*' , '/' , ':' , ';' , '.' ]

    lex=Lexical()

    while True:
        ch = f.read(1)

        ch=str(ch,'utf-8')

        # print("current position", f.tell())

        if not ch: break

        if ch == '.':
            f.seek(-2, 1)
            OneLeft = str(f.read(1),'utf-8')
            f.seek(1, 1)
            OneRight = str(f.read(1),'utf-8')
            if re.match("[0-9]", OneLeft) and re.match("[0-9]", OneRight):
                f.seek(-1, 1)
                temp += ch
                continue
            else:
                f.seek(-2, 1)
                ch = f.read(1)
                ch = str(ch, 'utf-8')


        if ch in breakers:

            if lex.chk_FLT_CONST(temp, lineNum):
                printToken("FLT_CONST", temp, lineNum)
                temp = ""

            if lex.chk_keywords(temp, lineNum):
                printToken("Keyword", temp, lineNum)
                temp = ""

            elif lex.chk_ID(temp,lineNum):
                printToken("ID",temp,lineNum)
                temp = ""

            elif lex.chk_INT_CONST(temp,lineNum):
                printToken("INT_CONST",temp,lineNum)
                temp = ""

            elif lex.chk_STR_CONST(temp,lineNum):
                printToken("STR_CONST",temp,lineNum)
                temp = ""

            elif lex.chk_CHAR_CONST(temp,lineNum):
                printToken("CHAR_CONST",temp,lineNum)
                temp = ""

            elif lex.chk_falto():
                temp = ""

            else:
                print("Error at "+lineNum)
                temp=""

            if ch!='\n' and ch!=' ':
                print(ch+" at "+str(lineNum))
            if ch=='\n':
                lineNum+=1
        else:
            temp+=str(ch)

    f.close()



def printToken(CPart,VPart,line):
    print("("+CPart+","+VPart+","+str(line)+")")


if __name__=="__main__":main()

