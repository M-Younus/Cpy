
from lexical import Lexical

def main():

    temp="";lineNum=1

    f = open('test.txt', 'r')

    breakers=['(',')','[',']','{','}','=',',',' ','\n']

    lex=Lexical()

    while True:
        ch = f.read(1)

        if not ch: break

        if ch in breakers:
            lex.chk_Id(temp)
            temp=""
            if ch!='\n' and ch!=' ':
                print(ch)
            if ch=='\n':
                lineNum+=1
        else:
            temp+=ch


main()