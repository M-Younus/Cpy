
import re

class Lexical():

    _keywords = ['False', 'class', 'finally', 'is', 'return', 'None', 'continue', 'for', 'lambda', 'True',
                     'def', 'while', 'elif', 'if', 'else', 'break']

    def chk_ID(self,temp,LN):
        if temp!="":
            print("Identifiers found "+temp+" at "+str(LN))
        return True

    def chk_keywords(self,temp,LN):
        if temp!="":
            if temp in self._keywords:
                return True
        return False

    def chk_INT_CONST(self,temp,LN):
        if temp!="":
            print("Identifiers found "+temp+" at "+str(LN))
        return True

    def chk_FLT_CONST(self,temp,LN):
        if temp!="":
            print("Identifiers found "+temp+" at "+str(LN))
        return True

    def chk_CHAR_CONST(self,temp,LN):
        if temp!="":
            if len(temp)==3:
                if temp[0]=='\'' and temp[2]=='\'':
                    return True
            elif len(temp)==4:
                if temp[0]=='\'' and temp[1]=='\\' and temp[3]=='\'':
                    return True
        return False

    def chk_STR_CONST(self,temp,LN):
        if temp!="":
            if temp[0]=='\"' and temp[len(temp)-1]=='\"' and temp[len(temp)-2]!='\\':
                return True
        return False


    def chk_falto(self):
        print("bit falto stuff")
        return True