
import re

class Lexical():

    _keywords = ['False', 'class', 'finally', 'is', 'return', 'None', 'continue', 'for', 'lambda', 'True',
                     'def', 'while', 'elif', 'if', 'else', 'break']

    def chk_ID(self,temp,LN):

        state=0;FS=1
        if temp!="":
            for i in range(len(temp)):
                state=self.trand_ID(state,temp[i])
                if state==3:
                    return False
            return state==FS
        return False

    def trand_ID(self,state,elem):

        TT_ID = [
            [1, 2],
            [1, 1],
            [1, 1]
        ]

        if re.match("[A-Za-z]",elem):
            return TT_ID[state][0]
        elif elem=='_':
            return TT_ID[state][1]
        else:
            return 3

    def chk_keywords(self,temp,LN):
        if temp!="":
            if temp in self._keywords:
                return True
        return False

    def chk_INT_CONST(self,temp,LN):

        state=0;FS=1

        if temp!="":
            for i in range(len(temp)):
                state=self.trans_INT(state,temp[i])
                if state==3:
                    return False
            return state==FS
        return False


    def trans_INT(self,state,elem):

        TT_INT = [
            [1, 2],
            [1, 3],
            [1, 3],
            [3, 3]
        ]

        if re.match("[0-9]",elem):
            return TT_INT[state][0]
        elif elem=='+' or elem=='-':
            return TT_INT[state][1]
        else:
            return 3



    def chk_FLT_CONST(self,temp,LN):

        state=0;FS=3

        if temp!="":
            for i in range(len(temp)):
                state=self.trans_FLT(state,temp[i])
                if state==4:
                    return False
            return state==FS
        return False

    def trans_FLT(self,state,elem):

        TT_FLOAT=[
            [1,2,1],
            [1,3,4],
            [3,4,1],
            [3,4,4],
            [4,4,4]
        ]

        if re.match("[0-9]",elem):
            return TT_FLOAT[state][0]
        elif elem=='.':
            return TT_FLOAT[state][1]
        elif elem=='+' or elem=='-':
            return TT_FLOAT[state][2]
        else:
            return 4

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
        # print("bit falto stuff")
        return True