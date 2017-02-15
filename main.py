
from lexical import Lexical

def main():

    temp="";lineNum=1

    f = open('test.txt', 'r')

    breakers=[ '(' , ')' , '[' , ']' , '{' , '}' , '=' , ',' , ' ' , '\n' , '\'' , '\"'
        , '<' , '>' , '-' , '+' , '*' , '/' ]

    lex=Lexical()

    while True:
        ch = f.read(1)

        if not ch: break

        if ch in breakers:

            if lex.chk_ID(temp,lineNum):
                printToken("ID",temp,lineNum)
                temp = ""

            elif lex.chk_keywords(temp,lineNum):
                printToken("Keyword",temp,lineNum)
                temp = ""


            elif lex.chk_STR_CONST(temp,lineNum):

                if ch=="\"":
                    while True:
                        old=ch
                        ch=f.read(1)
                        if old!='\\' and ch=='\"':
                            break
                        elif old!='\\' and ch=='\n':
                            break
                        else:
                            temp+=ch

                printToken("STR_CONST",temp,lineNum)
                temp = ""

            elif lex.falto():
                temp = ""

            else:
                print("Error at "+lineNum)
                temp=""

            if ch!='\n' and ch!=' ':
                print(ch+" at "+str(lineNum))
            if ch=='\n':
                lineNum+=1
        else:
            temp+=ch


def printToken(CPart,VPart,line):
    print("("+CPart+","+VPart+","+line+")")

main()