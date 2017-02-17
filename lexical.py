
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
            print("Identifiers found "+temp+" at "+str(LN))
        return True

    def chk_STR_CONST(self,temp,LN):
        if temp!="":
            print("string found "+temp+" at "+str(LN))
        return True

    def chk_falto(self):
        print("bit falto stuff")
        return True