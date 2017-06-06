
import sys

class Syntax:

    _tokens = [];_tokensIndex=0

    def __init__(self,tokens):
        Syntax._tokens=tokens
        Syntax._tokensIndex = 0


    def PROG(self):
        if Syntax._tokens[Syntax._tokensIndex].CP == "class":
            if self.CLASS():
                return True
        if Syntax._tokens[Syntax._tokensIndex].CP in ['ID', 'self', 'while', 'for', 'if', 'def']:
            if self.M_ST():
                return True

    #region Class

    def CLASS(self):
        if Syntax._tokens[Syntax._tokensIndex].CP == "class":
            Syntax._tokensIndex += 1
            if Syntax._tokens[Syntax._tokensIndex].CP == "ID":
                Syntax._tokensIndex += 1
                if self.CLASS1():
                    return True
            else:
                sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))

        else:
            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))


    def CLASS1(self):
        if Syntax._tokens[Syntax._tokensIndex].CP=='(':
            Syntax._tokensIndex += 1
            if self.PARENT():
                Syntax._tokensIndex += 1
                if Syntax._tokens[Syntax._tokensIndex].CP==')':
                    Syntax._tokensIndex += 1
                    if Syntax._tokens[Syntax._tokensIndex].CP == ':':
                        Syntax._tokensIndex += 1
                        if Syntax._tokens[Syntax._tokensIndex].CP == '{':
                            Syntax._tokensIndex += 1
                            if self.M_ST():
                                Syntax._tokensIndex += 1
                                if Syntax._tokens[Syntax._tokensIndex].CP == '}':
                                    return True
                                else:
                                    sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
                        else:
                            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
                    else:
                        sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
                else:
                    sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))


    def PARENT(self):
        if Syntax._tokens[Syntax._tokensIndex].CP == 'ID':
            Syntax._tokensIndex += 1
            if self.PARENT():
                return True
        elif Syntax._tokens[Syntax._tokensIndex].CP == ',':
            Syntax._tokensIndex += 1
            if Syntax._tokens[Syntax._tokensIndex].CP == 'ID':
                Syntax._tokensIndex += 1
                if self.PARENT():
                    return True
            else:
                sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
        else:
            Syntax._tokensIndex -= 1
            return True

    #endregion

    #region FUNC DEF

    def FUNC_DEF(self):
        if Syntax._tokens[Syntax._tokensIndex].CP == 'def':
            Syntax._tokensIndex += 1
            if Syntax._tokens[Syntax._tokensIndex].CP == 'ID':
                Syntax._tokensIndex += 1
                if Syntax._tokens[Syntax._tokensIndex].CP == '(':
                    Syntax._tokensIndex += 1
                    if self.ARGS():
                        Syntax._tokensIndex += 1
                        if Syntax._tokens[Syntax._tokensIndex].CP == ')':
                            Syntax._tokensIndex += 1
                            if Syntax._tokens[Syntax._tokensIndex].CP == ':':
                                Syntax._tokensIndex += 1
                                if Syntax._tokens[Syntax._tokensIndex].CP == '{':
                                    Syntax._tokensIndex += 1
                                    if self.M_ST():
                                        Syntax._tokensIndex += 1
                                        if self.RET():
                                            Syntax._tokensIndex += 1
                                            if Syntax._tokens[Syntax._tokensIndex].CP == '}':
                                                return True
                                            else:
                                                sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
                                else:
                                    sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
                            else:
                                sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
                        else:
                            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
                else:
                    sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
            else:
                sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))

        else:
            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))

    def ARGS(self):
        if Syntax._tokens[Syntax._tokensIndex].CP in ['self', 'ID']:
            if self.SELF():
                Syntax._tokensIndex += 1
                if self.DECL_ASGN():
                    return True
        else:
            Syntax._tokensIndex -= 1
            return True

    def SELF(self):
        if Syntax._tokens[Syntax._tokensIndex].CP=='self':
            Syntax._tokensIndex += 1
            if Syntax._tokens[Syntax._tokensIndex].CP == ',':
                return True
            else:
                sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
        else:
            Syntax._tokensIndex -= 1
            return True

    def RET(self):
        if Syntax._tokens[Syntax._tokensIndex].CP=='return':
            Syntax._tokensIndex += 1
            if self.E():
                return True
        else:
            Syntax._tokensIndex -= 1
            return True

    #endregion

    #region Statements

    def M_ST(self):
        if Syntax._tokens[Syntax._tokensIndex].CP in ['ID', 'self', 'while', 'for', 'if', 'def']:
            if self.S_ST():
                Syntax._tokensIndex += 1
                if self.M_ST():
                    return True

        else:
            Syntax._tokensIndex -= 1
            return True

    def S_ST(self):
        if Syntax._tokens[Syntax._tokensIndex].CP in ['ID','self', 'while','for','if','def']:
            if Syntax._tokens[Syntax._tokensIndex].CP =='ID':
                Syntax._tokensIndex += 1
                if self.S_ST2():
                    return True
            elif Syntax._tokens[Syntax._tokensIndex].CP == 'self':
                Syntax._tokensIndex += 1
                if Syntax._tokens[Syntax._tokensIndex].CP == '.':
                    Syntax._tokensIndex += 1
                    if Syntax._tokens[Syntax._tokensIndex].CP == 'ID':
                        Syntax._tokensIndex += 1
                        if Syntax._tokens[Syntax._tokensIndex].CP == '(':
                            Syntax._tokensIndex += 1
                            if self.DECL_ASGN():
                                Syntax._tokensIndex += 1
                                if Syntax._tokens[Syntax._tokensIndex].CP == ')':
                                    return True
                                else:
                                    sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
                        else:
                            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
                    else:
                        sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
                else:
                    sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
            elif Syntax._tokens[Syntax._tokensIndex].CP == 'while':
                if self.WHILE_ST():
                    return True
            elif Syntax._tokens[Syntax._tokensIndex].CP == 'for':
                if self.FOR_ST():
                    return True
            elif Syntax._tokens[Syntax._tokensIndex].CP == 'if':
                if self.IF_ELSE():
                    return True
            elif Syntax._tokens[Syntax._tokensIndex].CP == 'def':
                if self.FUNC_DEF():
                    return True
            else:
                sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))


    def S_ST2(self):
        # if Syntax._tokens[Syntax._tokensIndex].CP in ['=',',','ASGN_OPT',',','(','elif','else','ID', 'self', 'while', 'for', 'if','}']:
        if Syntax._tokens[Syntax._tokensIndex].CP in ['=',',','ASGN_OPT']:
            if self.LIST():
                return True
        elif Syntax._tokens[Syntax._tokensIndex].CP in ['.','(']:
            if self.FUNC_CALL1():
                return True
        else:
            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))

    #endregions

    #region LOOPS

    def WHILE_ST(self):
        if Syntax._tokens[Syntax._tokensIndex].CP == 'while':
            Syntax._tokensIndex += 1
            if Syntax._tokens[Syntax._tokensIndex].CP == '(':
                Syntax._tokensIndex += 1
                if self.E():
                    Syntax._tokensIndex += 1
                    if Syntax._tokens[Syntax._tokensIndex].CP == ')':
                        Syntax._tokensIndex += 1
                        if Syntax._tokens[Syntax._tokensIndex].CP == ':':
                            Syntax._tokensIndex += 1
                            if self.BODY():
                                return True
                        else:
                            sys.exit(
                                self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
                    else:
                        sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
            else:
                sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))

    def FOR_ST(self):
        if Syntax._tokens[Syntax._tokensIndex].CP == 'for':
            Syntax._tokensIndex += 1
            if Syntax._tokens[Syntax._tokensIndex].CP == '(':
                Syntax._tokensIndex += 1
                if self.X():
                    Syntax._tokensIndex += 1
                    if Syntax._tokens[Syntax._tokensIndex].CP == ';':
                        Syntax._tokensIndex += 1
                        if self.Y():
                            Syntax._tokensIndex += 1
                            if Syntax._tokens[Syntax._tokensIndex].CP == ';':
                                Syntax._tokensIndex += 1
                                if self.X():
                                    Syntax._tokensIndex += 1
                                    if Syntax._tokens[Syntax._tokensIndex].CP == ')':
                                        Syntax._tokensIndex += 1
                                        if Syntax._tokens[Syntax._tokensIndex].CP == ":":
                                            Syntax._tokensIndex += 1
                                            if self.BODY():
                                                return True
                                        else:
                                            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
                                    else:
                                        sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
                            else:
                                sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
                    else:
                        sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
            else:
                sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))

    def X(self):
        if self.DECL_ASGN():
            return True
        else:
            Syntax._tokensIndex -= 1
            return True

    def Y(self):
        if self.E():
            return True
        else:
            Syntax._tokensIndex += 1
            return True

    #endregion

    #region DECL

    def DECL_ASGN(self):
        if Syntax._tokens[Syntax._tokensIndex].CP in ["ID","INC_DEC"]:
            if Syntax._tokens[Syntax._tokensIndex].CP=="ID":
                Syntax._tokensIndex+=1
                if Syntax._tokens[Syntax._tokensIndex].CP in ['=',',','ASGN_OPT']:
                    if self.LIST():
                        return True
                elif Syntax._tokens[Syntax._tokensIndex].CP == "INC_DEC":
                    return True
                else:
                    sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
            elif Syntax._tokens[Syntax._tokensIndex].CP == "INC_DEC":
                Syntax._tokensIndex += 1
                if Syntax._tokens[Syntax._tokensIndex].CP == "ID":
                    return True
                else:
                    sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))


    def LIST(self):
        if Syntax._tokens[Syntax._tokensIndex].CP in ['=',',','ASGN_OPT']:
            if self.INIT():
                Syntax._tokensIndex += 1
                if self.LIST2():
                    return True
            elif Syntax._tokens[Syntax._tokensIndex].CP=="ASGN_OPT":
                Syntax._tokensIndex += 1
                if self.E():
                    Syntax._tokensIndex += 1
                    if self.LIST2():
                        return True
            else:
                sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))


    def INIT(self):
        if Syntax._tokens[Syntax._tokensIndex].CP == "=":
            Syntax._tokensIndex += 1
            if self.INIT2():
                return True
        else:
            Syntax._tokensIndex -= 1
            return True


    def LIST2(self):
        # if Syntax._tokens[Syntax._tokensIndex].CP in [',',';']:
        if Syntax._tokens[Syntax._tokensIndex].CP==',':
            Syntax._tokensIndex += 1
            if self.DECL_ASGN():
                return True
        else:
            Syntax._tokensIndex -= 1
            return True


    def INIT2(self):
        if self.E():
            Syntax._tokensIndex += 1
            if self.INIT3():
                return True
        else:
            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))


    def INIT3(self):
        if Syntax._tokens[Syntax._tokensIndex].CP =='=':
            if self.INIT():
                return True

        else:
            Syntax._tokensIndex -= 1
            return True

    #endregion

    #region Expression

    def E(self):
        if self.F():
            Syntax._tokensIndex += 1
            if self.E1():
                return True
        else:
            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))


    def E1(self):
        if Syntax._tokens[Syntax._tokensIndex].VP == '||':
            Syntax._tokensIndex += 1
            if self.F():
                Syntax._tokensIndex += 1
                if self.E1():
                    return True
        else:
            Syntax._tokensIndex -= 1
            return True


    def F(self):
        if self.G():
            Syntax._tokensIndex += 1
            if self.F1():
                return True
        else:
            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))


    def F1(self):
        if Syntax._tokens[Syntax._tokensIndex].VP == '&&':
            Syntax._tokensIndex += 1
            if self.G():
                Syntax._tokensIndex += 1
                if self.F1():
                    return True
        else:
            Syntax._tokensIndex -= 1
            return True


    def G(self):
        if self.H():
            Syntax._tokensIndex += 1
            if self.G1():
                return True
        else:
            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))


    def G1(self):
        if Syntax._tokens[Syntax._tokensIndex].CP=='RO':
            Syntax._tokensIndex += 1
            if self.H():
                Syntax._tokensIndex += 1
                if self.G1():
                    return True
        else:
            Syntax._tokensIndex -= 1
            return True


    def H(self):
        if self.I():
            Syntax._tokensIndex += 1
            if self.H1():
                return True
        else:
            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))


    def H1(self):
        if Syntax._tokens[Syntax._tokensIndex].CP=='ADD_SUB':
            Syntax._tokensIndex += 1
            if self.I():
                Syntax._tokensIndex += 1
                if self.H1():
                    return True
        else:
            Syntax._tokensIndex -= 1
            return True


    def I(self):
        if self.J():
            Syntax._tokensIndex += 1
            if self.I1():
                return True
        else:
            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))


    def I1(self):
        if Syntax._tokens[Syntax._tokensIndex].CP == 'DIV_MUL':
            Syntax._tokensIndex += 1
            if self.J():
                Syntax._tokensIndex += 1
                if self.I1():
                    return True
        else:
            Syntax._tokensIndex -= 1
            return True


    def J(self):
        if Syntax._tokens[Syntax._tokensIndex].CP in ['ID', 'LO', '(', 'INC_DEC', 'self', 'INT_CONST', 'FLT_CONST','STR_CONST', 'CHAR_CONST','[']:
            if Syntax._tokens[Syntax._tokensIndex].CP=="ID":
                Syntax._tokensIndex += 1
                if self.J2():
                    return True
            elif Syntax._tokens[Syntax._tokensIndex].CP=="(":
                Syntax._tokensIndex += 1
                if self.E():
                    Syntax._tokensIndex += 1
                    if Syntax._tokens[Syntax._tokensIndex].CP==")":
                        return True
                    else:
                        sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
            elif Syntax._tokens[Syntax._tokensIndex].VP=="!":
                Syntax._tokensIndex += 1
                if self.J1():
                    return True
            elif Syntax._tokens[Syntax._tokensIndex].CP=="INC_DEC":
                Syntax._tokensIndex += 1
                if Syntax._tokens[Syntax._tokensIndex].CP=="ID":
                    return True
                else:
                    sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
            elif Syntax._tokens[Syntax._tokensIndex].CP in ['self', 'ID']:
                if self.FUNC_CALL():
                    return True
            elif Syntax._tokens[Syntax._tokensIndex].CP in ['INT_CONST', 'FLT_CONST', 'STR_CONST', 'CHAR_CONST']:
                if self.CONSTANT():
                    return True
            elif Syntax._tokens[Syntax._tokensIndex].CP == "[":
                if self.ARRAY_LIST():
                    return True
            else:
                sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))


    def J1(self):
        if self.J():
            return True
        else:
            Syntax._tokensIndex -= 1
            return True


    def J2(self):
        if Syntax._tokens[Syntax._tokensIndex].CP=='INC_DEC':
            return True
        else:
            Syntax._tokensIndex -= 1
            return True

    #endregion

    #region ARRAY LIST

    def ARRAY_LIST(self):
        if Syntax._tokens[Syntax._tokensIndex].CP == "[":
            Syntax._tokensIndex += 1
            if self.VALS():
                Syntax._tokensIndex += 1
                if Syntax._tokens[Syntax._tokensIndex].CP == "]":
                    return True
                else:
                    sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))


    def VALS(self):
        if Syntax._tokens[Syntax._tokensIndex].CP in ['ID', 'LO', '(', 'INC_DEC', 'self', 'INT_CONST', 'FLT_CONST','STR_CONST', 'CHAR_CONST', '[',',']:
            if Syntax._tokens[Syntax._tokensIndex].CP == ",":
                Syntax._tokensIndex += 1
                if self.E():
                    Syntax._tokensIndex += 1
                    if self.VALS():
                        return True
            elif self.E():
                Syntax._tokensIndex += 1
                if self.VALS():
                    return True

            else:
                sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
        else:
            Syntax._tokensIndex -= 1
            return True

    #endregion

    def CONSTANT(self):
        if Syntax._tokens[Syntax._tokensIndex].CP in ['INT_CONST', 'FLT_CONST','STR_CONST', 'CHAR_CONST']:
            return True
        else:
            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))

    #region FUNC_CALL

    def FUNC_CALL(self):
        if Syntax._tokens[Syntax._tokensIndex].CP in ['self','ID']:
            if Syntax._tokens[Syntax._tokensIndex].CP == "self":
                Syntax._tokensIndex += 1
                if Syntax._tokens[Syntax._tokensIndex].CP == ".":
                    Syntax._tokensIndex += 1
                    if Syntax._tokens[Syntax._tokensIndex].CP == "ID":
                        Syntax._tokensIndex += 1
                        if Syntax._tokens[Syntax._tokensIndex].CP == "(":
                            Syntax._tokensIndex += 1
                            if self.PARAMS():
                                Syntax._tokensIndex += 1
                                if Syntax._tokens[Syntax._tokensIndex].CP == ")":
                                    return True
                                else:
                                    sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
                        else:
                            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
                    else:
                        sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
                else:
                    sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))

            elif Syntax._tokens[Syntax._tokensIndex].CP == "ID":
                Syntax._tokensIndex += 1
                if self.FUNC_CALL1():
                    return True
            else:
                sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))


    def FUNC_CALL1(self):
        if Syntax._tokens[Syntax._tokensIndex].CP==".":
            Syntax._tokensIndex += 1
            if Syntax._tokens[Syntax._tokensIndex].CP == "ID":
                Syntax._tokensIndex += 1
                if Syntax._tokens[Syntax._tokensIndex].CP == "(":
                    Syntax._tokensIndex += 1
                    if self.PARAMS():
                        Syntax._tokensIndex += 1
                        if Syntax._tokens[Syntax._tokensIndex].CP == ")":
                            return True
                        else:
                            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
                else:
                    sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
            else:
                sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
        elif Syntax._tokens[Syntax._tokensIndex].CP == "(":
            Syntax._tokensIndex += 1
            if self.FUNC_CALL2():
                return True
        else:
            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))


    def FUNC_CALL2(self):
        if Syntax._tokens[Syntax._tokensIndex].CP == ")":
            Syntax._tokensIndex += 1
            if self.FUNC_CALL3():
                return True
        elif self.DECL_ASGN():
            return True

        else:
            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))


    def FUNC_CALL3(self):
        if Syntax._tokens[Syntax._tokensIndex].CP=='.':
            Syntax._tokensIndex += 1
            if Syntax._tokens[Syntax._tokensIndex].CP=='ID':
                Syntax._tokensIndex += 1
                if Syntax._tokens[Syntax._tokensIndex].CP == '(':
                    Syntax._tokensIndex += 1
                    if self.PARAMS():
                        Syntax._tokensIndex += 1
                        if Syntax._tokens[Syntax._tokensIndex].CP == ')':
                            return True
                        else:
                            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
                else:
                    sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
            else:
                sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
        else:
            Syntax._tokensIndex -= 1
            return True


    def PARAMS(self):
        if Syntax._tokens[Syntax._tokensIndex].CP == 'ID':
            Syntax._tokensIndex += 1
            if Syntax._tokens[Syntax._tokensIndex].CP == '=':
                Syntax._tokensIndex += 1
                if self.E():
                    Syntax._tokensIndex += 1
                    if self.PARAMS():
                        return True
        elif Syntax._tokens[Syntax._tokensIndex].CP == ',':
            Syntax._tokensIndex += 1
            if Syntax._tokens[Syntax._tokensIndex].CP == 'ID':
                Syntax._tokensIndex += 1
                if Syntax._tokens[Syntax._tokensIndex].CP == '=':
                    Syntax._tokensIndex += 1
                    if self.E():
                        Syntax._tokensIndex += 1
                        if self.PARAMS():
                            return True
        elif Syntax._tokens[Syntax._tokensIndex].CP == 'ID':
            Syntax._tokensIndex += 1
            if self.PARAMS():
                return True

        elif Syntax._tokens[Syntax._tokensIndex].CP == ',':
            Syntax._tokensIndex += 1
            if Syntax._tokens[Syntax._tokensIndex].CP == 'ID':
                Syntax._tokensIndex += 1
                if self.PARAMS():
                    return True

        else:
            Syntax._tokensIndex -= 1
            return True





    #endregion

    #region IF-ELSE

    def IF_ELSE(self):
        if Syntax._tokens[Syntax._tokensIndex].CP=="if":
            Syntax._tokensIndex += 1
            if Syntax._tokens[Syntax._tokensIndex].CP == "(":
                Syntax._tokensIndex += 1
                if self.E():
                    Syntax._tokensIndex += 1
                    if Syntax._tokens[Syntax._tokensIndex].CP == ")":
                        Syntax._tokensIndex += 1
                        if Syntax._tokens[Syntax._tokensIndex].CP == ":":
                            Syntax._tokensIndex += 1
                            if self.BODY():
                                Syntax._tokensIndex += 1
                                if self.ELIF():
                                    Syntax._tokensIndex += 1
                                    if self.O_ELSE():
                                        return True
                        else:
                            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
                    else:
                        sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
            else:
                sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))


    def ELIF(self):
        if Syntax._tokens[Syntax._tokensIndex].CP == "elif":
            Syntax._tokensIndex += 1
            if self.E():
                Syntax._tokensIndex += 1
                if Syntax._tokens[Syntax._tokensIndex].CP == ")":
                    Syntax._tokensIndex += 1
                    if Syntax._tokens[Syntax._tokensIndex].CP == ":":
                        Syntax._tokensIndex += 1
                        if self.BODY():
                            return True
                    else:
                        sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
                else:
                    sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
        else:
            Syntax._tokensIndex -= 1
            return True

    def O_ELSE(self):
        if Syntax._tokens[Syntax._tokensIndex].CP == "else":
            Syntax._tokensIndex += 1
            if Syntax._tokens[Syntax._tokensIndex].CP == ":":
                Syntax._tokensIndex += 1
                if self.BODY():
                    return True
            else:
                sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
        else:
            Syntax._tokensIndex -= 1
            return True

    #endregion

    def BODY(self):
        if Syntax._tokens[Syntax._tokensIndex].CP in ['ID', 'self', 'while', 'for', 'if', 'def']:
            if self.S_ST():
                return True
        elif Syntax._tokens[Syntax._tokensIndex].CP == "{":
            Syntax._tokensIndex += 1
            if self.M_ST():
                Syntax._tokensIndex += 1
                if Syntax._tokens[Syntax._tokensIndex].CP == "}":
                    return True
                else:
                    sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP, Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(Syntax._tokens[Syntax._tokensIndex].CP,Syntax._tokens[Syntax._tokensIndex].VP,Syntax._tokens[Syntax._tokensIndex].LN))

    def errorPrint(self,classPart,valuePart,lineNum):
        return "Error occur where class is "+classPart+" and value is "+valuePart+" line is "+str(lineNum)

