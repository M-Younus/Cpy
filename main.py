
from lexical import Lexical

import re


def main():

    temp="";lineNum=1

    f = open('testingcode.txt', 'rb+')

    breakers=[ '(' , ')' , '[' , ']' , '{' , '}' , '=' , ',' , ' ' , '\n' , '\r'
            , '<' , '>' , '-' , '+' , '*' , '/' , ':' , ';' , '.' ]

    lex=Lexical()

    while True:
        ch = f.read(1)

        ch=str(ch,'utf-8')

        # print("current position", f.tell())

        if not ch: break

        #working for separation of float and ID
        if ch == '.':
            f.seek(-2, 1)
            OneLeft = str(f.read(1),'utf-8')
            f.seek(1, 1)
            OneRight = str(f.read(1),'utf-8')
            if (re.match("[0-9]", OneLeft) or OneLeft in ['+','-'] ) and re.match("[0-9]", OneRight):
                f.seek(-1, 1)
                temp += ch
                continue
            else:
                f.seek(-2, 1)
                ch = f.read(1)
                ch = str(ch, 'utf-8')

        elif ch == '+' or ch == '-':
            OneRight = str(f.read(1),'utf-8')
            if  re.match("[0-9]", OneRight) or OneRight=='.':
                f.seek(-1, 1)
                temp += ch
                continue



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

            # elif lex.chk_falto():
            #     temp = ""

            else:
                print("Error at "+str(lineNum) + " where value is "+temp)
                temp=""

            if ch!='\n' and ch!=' ':
                print(ch+" at "+str(lineNum))
            if ch=='\n':
                lineNum+=1

        #check for inc_DEc and add_sub
        if ch == '+' or ch == '-':
            OneRight = str(f.read(1),'utf-8')
            if  ch==OneRight:
                temp+=ch+ch
                printToken("INC_DEC",temp,lineNum)
                continue
            else:
                printToken("ADD_SUB", temp, lineNum)


        else:
            temp+=str(ch)

    f.close()


fileData=""

def printToken(CPart,VPart,line):
    global fileData
    string="("+CPart+","+VPart+","+str(line)+")"
    fileData+=string+"\n"
    print(string)


if __name__=="__main__":main()

fout=open("output.txt",'w')
fout.write(fileData)
fout.close()


