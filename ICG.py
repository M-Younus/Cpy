
import sys

class ICG:

    _tokens = [];_tokensIndex=0;_tempNum=0;_labelNum=0

    def __init__(self,tokens):
        ICG._tokens=tokens
        ICG._tokensIndex = 0


    def PROG(self):
        if ICG._tokens[ICG._tokensIndex].CP == "class":
            if self.CLASS():
                return True
        if ICG._tokens[ICG._tokensIndex].CP in ['ID', 'self', 'while', 'for', 'if', 'def']:
            if self.M_ST():
                return True

    #region Class

    def CLASS(self):
        if ICG._tokens[ICG._tokensIndex].CP == "class":
            ICG._tokensIndex += 1
            if ICG._tokens[ICG._tokensIndex].CP == "ID":
                ICG._tokensIndex += 1
                if self.CLASS1():
                    return True
            else:
                sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))

        else:
            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))


    def CLASS1(self):
        if ICG._tokens[ICG._tokensIndex].CP=='(':
            ICG._tokensIndex += 1
            if self.PARENT():
                ICG._tokensIndex += 1
                if ICG._tokens[ICG._tokensIndex].CP==')':
                    ICG._tokensIndex += 1
                    if ICG._tokens[ICG._tokensIndex].CP == ':':
                        ICG._tokensIndex += 1
                        if ICG._tokens[ICG._tokensIndex].CP == '{':
                            ICG._tokensIndex += 1
                            if self.M_ST():
                                ICG._tokensIndex += 1
                                if ICG._tokens[ICG._tokensIndex].CP == '}':
                                    return True
                                else:
                                    sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
                        else:
                            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
                    else:
                        sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
                else:
                    sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))


    def PARENT(self):
        if ICG._tokens[ICG._tokensIndex].CP == 'ID':
            ICG._tokensIndex += 1
            if self.PARENT():
                return True
        elif ICG._tokens[ICG._tokensIndex].CP == ',':
            ICG._tokensIndex += 1
            if ICG._tokens[ICG._tokensIndex].CP == 'ID':
                ICG._tokensIndex += 1
                if self.PARENT():
                    return True
            else:
                sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
        else:
            ICG._tokensIndex -= 1
            return True

    #endregion

    #region FUNC DEF

    def FUNC_DEF(self):
        if ICG._tokens[ICG._tokensIndex].CP == 'def':
            ICG._tokensIndex += 1
            if ICG._tokens[ICG._tokensIndex].CP == 'ID':
                ICG._tokensIndex += 1
                if ICG._tokens[ICG._tokensIndex].CP == '(':
                    ICG._tokensIndex += 1
                    if self.ARGS():
                        ICG._tokensIndex += 1
                        if ICG._tokens[ICG._tokensIndex].CP == ')':
                            ICG._tokensIndex += 1
                            if ICG._tokens[ICG._tokensIndex].CP == ':':
                                ICG._tokensIndex += 1
                                if ICG._tokens[ICG._tokensIndex].CP == '{':
                                    ICG._tokensIndex += 1
                                    if self.M_ST():
                                        ICG._tokensIndex += 1
                                        if self.RET():
                                            ICG._tokensIndex += 1
                                            if ICG._tokens[ICG._tokensIndex].CP == '}':
                                                return True
                                            else:
                                                sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
                                else:
                                    sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
                            else:
                                sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
                        else:
                            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
                else:
                    sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
            else:
                sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))

        else:
            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))

    def ARGS(self):
        if ICG._tokens[ICG._tokensIndex].CP in ['self', 'ID']:
            if self.SELF():
                ICG._tokensIndex += 1
                if self.DECL_ASGN():
                    return True
        else:
            ICG._tokensIndex -= 1
            return True

    def SELF(self):
        if ICG._tokens[ICG._tokensIndex].CP=='self':
            ICG._tokensIndex += 1
            if ICG._tokens[ICG._tokensIndex].CP == ',':
                return True
            else:
                sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
        else:
            ICG._tokensIndex -= 1
            return True

    def RET(self):
        if ICG._tokens[ICG._tokensIndex].CP=='return':
            ICG._tokensIndex += 1
            if self.E():
                return True
        else:
            ICG._tokensIndex -= 1
            return True

    #endregion

    #region Statements

    def M_ST(self):
        if ICG._tokens[ICG._tokensIndex].CP in ['ID', 'self', 'while', 'for', 'if', 'def']:
            if self.S_ST():
                ICG._tokensIndex += 1
                if self.M_ST():
                    return True

        else:
            ICG._tokensIndex -= 1
            return True

    def S_ST(self):
        if ICG._tokens[ICG._tokensIndex].CP in ['ID','self', 'while','for','if','def']:
            if ICG._tokens[ICG._tokensIndex].CP =='ID':
                ICG._tokensIndex += 1
                if self.S_ST2():
                    return True
            elif ICG._tokens[ICG._tokensIndex].CP == 'self':
                ICG._tokensIndex += 1
                if ICG._tokens[ICG._tokensIndex].CP == '.':
                    ICG._tokensIndex += 1
                    if ICG._tokens[ICG._tokensIndex].CP == 'ID':
                        ICG._tokensIndex += 1
                        if ICG._tokens[ICG._tokensIndex].CP == '(':
                            ICG._tokensIndex += 1
                            if self.DECL_ASGN():
                                ICG._tokensIndex += 1
                                if ICG._tokens[ICG._tokensIndex].CP == ')':
                                    return True
                                else:
                                    sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
                        else:
                            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
                    else:
                        sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
                else:
                    sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
            elif ICG._tokens[ICG._tokensIndex].CP == 'while':
                if self.WHILE_ST():
                    return True
            elif ICG._tokens[ICG._tokensIndex].CP == 'for':
                if self.FOR_ST():
                    return True
            elif ICG._tokens[ICG._tokensIndex].CP == 'if':
                if self.IF_ELSE():
                    return True
            elif ICG._tokens[ICG._tokensIndex].CP == 'def':
                if self.FUNC_DEF():
                    return True
            else:
                sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))


    def S_ST2(self):
        # if ICG._tokens[ICG._tokensIndex].CP in ['=',',','ASGN_OPT',',','(','elif','else','ID', 'self', 'while', 'for', 'if','}']:
        if ICG._tokens[ICG._tokensIndex].CP in ['=',',','ASGN_OPT']:
            if self.LIST():
                return True
        elif ICG._tokens[ICG._tokensIndex].CP in ['.','(']:
            if self.FUNC_CALL1():
                return True
        else:
            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))

    #endregions

    #region LOOPS

    def WHILE_ST(self):
        if ICG._tokens[ICG._tokensIndex].CP == 'while':
            WL1=self.createLabel()
            self.generate(WL1+":")
            self.generate(self.createLabel()+":")
            ICG._tokensIndex += 1
            if ICG._tokens[ICG._tokensIndex].CP == '(':
                ICG._tokensIndex += 1
                WT1=self.createTemp()
                if self.E(WT1):
                    ICG._tokensIndex += 1
                    if ICG._tokens[ICG._tokensIndex].CP == ')':
                        WL2 = self.createLabel()
                        getattr("if("+WT1+"==FALSE)")
                        self.generate("JMP "+WL2)
                        ICG._tokensIndex += 1
                        if ICG._tokens[ICG._tokensIndex].CP == ':':
                            ICG._tokensIndex += 1
                            if self.BODY():
                                self.generate("JMP " + WL1)
                                self.generate(WL2 + ":")
                                return True
                        else:
                            sys.exit(
                                self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
                    else:
                        sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
            else:
                sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))

    def FOR_ST(self):
        if ICG._tokens[ICG._tokensIndex].CP == 'for':
            ICG._tokensIndex += 1
            if ICG._tokens[ICG._tokensIndex].CP == '(':
                ICG._tokensIndex += 1
                FT1=self.createTemp()
                if self.X(FT1):
                    ICG._tokensIndex += 1
                    if ICG._tokens[ICG._tokensIndex].CP == ';':
                        FL1=self.createLabel()
                        self.generate(FL1+":")
                        ICG._tokensIndex += 1
                        FT2=self.createTemp()
                        if self.Y(FT2):
                            ICG._tokensIndex += 1
                            if ICG._tokens[ICG._tokensIndex].CP == ';':
                                ICG._tokensIndex += 1
                                FT3=self.createTemp()
                                if self.X(FT3):
                                    ICG._tokensIndex += 1
                                    if ICG._tokens[ICG._tokensIndex].CP == ')':
                                        ICG._tokensIndex += 1
                                        if ICG._tokens[ICG._tokensIndex].CP == ":":
                                            ICG._tokensIndex += 1
                                            if self.BODY():
                                                self.generate("if("+FT2+"==FALSE")
                                                FL2=self.createLabel()
                                                self.generate("JMP "+FL2)
                                                # T3
                                                self.generate("JMP "+FL1)
                                                self.generate(FL2+":")
                                                return True
                                        else:
                                            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
                                    else:
                                        sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
                            else:
                                sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
                    else:
                        sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
            else:
                sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))

    def X(self):
        if self.DECL_ASGN():
            return True
        else:
            ICG._tokensIndex -= 1
            return True

    def Y(self):
        if self.E():
            return True
        else:
            ICG._tokensIndex += 1
            return True

    #endregion

    #region DECL

    def DECL_ASGN(self):
        if ICG._tokens[ICG._tokensIndex].CP in ["ID","INC_DEC"]:
            if ICG._tokens[ICG._tokensIndex].CP=="ID":
                ICG._tokensIndex+=1
                if ICG._tokens[ICG._tokensIndex].CP in ['=',',','ASGN_OPT']:
                    if self.LIST():
                        return True
                elif ICG._tokens[ICG._tokensIndex].CP == "INC_DEC":
                    return True
                else:
                    sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
            elif ICG._tokens[ICG._tokensIndex].CP == "INC_DEC":
                ICG._tokensIndex += 1
                if ICG._tokens[ICG._tokensIndex].CP == "ID":
                    return True
                else:
                    sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))


    def LIST(self):
        if ICG._tokens[ICG._tokensIndex].CP in ['=',',','ASGN_OPT']:
            if self.INIT():
                ICG._tokensIndex += 1
                if self.LIST2():
                    return True
            elif ICG._tokens[ICG._tokensIndex].CP=="ASGN_OPT":
                ICG._tokensIndex += 1
                if self.E():
                    ICG._tokensIndex += 1
                    if self.LIST2():
                        return True
            else:
                sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))


    def INIT(self):
        if ICG._tokens[ICG._tokensIndex].CP == "=":
            ICG._tokensIndex += 1
            if self.INIT2():
                return True
        else:
            ICG._tokensIndex -= 1
            return True


    def LIST2(self):
        # if ICG._tokens[ICG._tokensIndex].CP in [',',';']:
        if ICG._tokens[ICG._tokensIndex].CP==',':
            ICG._tokensIndex += 1
            if self.DECL_ASGN():
                return True
        else:
            ICG._tokensIndex -= 1
            return True


    def INIT2(self):
        if self.E():
            ICG._tokensIndex += 1
            if self.INIT3():
                return True
        else:
            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))


    def INIT3(self):
        if ICG._tokens[ICG._tokensIndex].CP =='=':
            if self.INIT():
                return True

        else:
            ICG._tokensIndex -= 1
            return True

    #endregion

    #region Expression

    def E(self,Etype):
        if self.F():
            ICG._tokensIndex += 1
            if self.E1():
                return True
        else:
            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))


    def E1(self):
        if ICG._tokens[ICG._tokensIndex].VP == '||':
            ICG._tokensIndex += 1
            if self.F():
                ICG._tokensIndex += 1
                if self.E1():
                    return True
        else:
            ICG._tokensIndex -= 1
            return True


    def F(self):
        if self.G():
            ICG._tokensIndex += 1
            if self.F1():
                return True
        else:
            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))


    def F1(self):
        if ICG._tokens[ICG._tokensIndex].VP == '&&':
            ICG._tokensIndex += 1
            if self.G():
                ICG._tokensIndex += 1
                if self.F1():
                    return True
        else:
            ICG._tokensIndex -= 1
            return True


    def G(self):
        if self.H():
            ICG._tokensIndex += 1
            if self.G1():
                return True
        else:
            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))


    def G1(self):
        if ICG._tokens[ICG._tokensIndex].CP=='RO':
            ICG._tokensIndex += 1
            if self.H():
                ICG._tokensIndex += 1
                if self.G1():
                    return True
        else:
            ICG._tokensIndex -= 1
            return True


    def H(self):
        if self.I():
            ICG._tokensIndex += 1
            if self.H1():
                return True
        else:
            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))


    def H1(self):
        if ICG._tokens[ICG._tokensIndex].CP=='ADD_SUB':
            ICG._tokensIndex += 1
            if self.I():
                ICG._tokensIndex += 1
                if self.H1():
                    return True
        else:
            ICG._tokensIndex -= 1
            return True


    def I(self):
        if self.J():
            ICG._tokensIndex += 1
            if self.I1():
                return True
        else:
            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))


    def I1(self):
        if ICG._tokens[ICG._tokensIndex].CP == 'DIV_MUL':
            ICG._tokensIndex += 1
            if self.J():
                ICG._tokensIndex += 1
                if self.I1():
                    return True
        else:
            ICG._tokensIndex -= 1
            return True


    def J(self):
        if ICG._tokens[ICG._tokensIndex].CP in ['ID', 'LO', '(', 'INC_DEC', 'self', 'INT_CONST', 'FLT_CONST','STR_CONST', 'CHAR_CONST','[']:
            if ICG._tokens[ICG._tokensIndex].CP=="ID":
                ICG._tokensIndex += 1
                if self.J2():
                    return True
            elif ICG._tokens[ICG._tokensIndex].CP=="(":
                ICG._tokensIndex += 1
                if self.E():
                    ICG._tokensIndex += 1
                    if ICG._tokens[ICG._tokensIndex].CP==")":
                        return True
                    else:
                        sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
            elif ICG._tokens[ICG._tokensIndex].VP=="!":
                ICG._tokensIndex += 1
                if self.J1():
                    return True
            elif ICG._tokens[ICG._tokensIndex].CP=="INC_DEC":
                ICG._tokensIndex += 1
                if ICG._tokens[ICG._tokensIndex].CP=="ID":
                    return True
                else:
                    sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
            elif ICG._tokens[ICG._tokensIndex].CP in ['self', 'ID']:
                if self.FUNC_CALL():
                    return True
            elif ICG._tokens[ICG._tokensIndex].CP in ['INT_CONST', 'FLT_CONST', 'STR_CONST', 'CHAR_CONST']:
                if self.CONSTANT():
                    return True
            elif ICG._tokens[ICG._tokensIndex].CP == "[":
                if self.ARRAY_LIST():
                    return True
            else:
                sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))


    def J1(self):
        if self.J():
            return True
        else:
            ICG._tokensIndex -= 1
            return True


    def J2(self):
        if ICG._tokens[ICG._tokensIndex].CP=='INC_DEC':
            return True
        else:
            ICG._tokensIndex -= 1
            return True

    #endregion

    #region ARRAY LIST

    def ARRAY_LIST(self):
        if ICG._tokens[ICG._tokensIndex].CP == "[":
            ICG._tokensIndex += 1
            if self.VALS():
                ICG._tokensIndex += 1
                if ICG._tokens[ICG._tokensIndex].CP == "]":
                    return True
                else:
                    sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))


    def VALS(self):
        if ICG._tokens[ICG._tokensIndex].CP in ['ID', 'LO', '(', 'INC_DEC', 'self', 'INT_CONST', 'FLT_CONST','STR_CONST', 'CHAR_CONST', '[',',']:
            if ICG._tokens[ICG._tokensIndex].CP == ",":
                ICG._tokensIndex += 1
                if self.E():
                    ICG._tokensIndex += 1
                    if self.VALS():
                        return True
            elif self.E():
                ICG._tokensIndex += 1
                if self.VALS():
                    return True

            else:
                sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
        else:
            ICG._tokensIndex -= 1
            return True

    #endregion

    def CONSTANT(self):
        if ICG._tokens[ICG._tokensIndex].CP in ['INT_CONST', 'FLT_CONST','STR_CONST', 'CHAR_CONST']:
            return True
        else:
            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))

    #region FUNC_CALL

    def FUNC_CALL(self):
        if ICG._tokens[ICG._tokensIndex].CP in ['self','ID']:
            if ICG._tokens[ICG._tokensIndex].CP == "self":
                ICG._tokensIndex += 1
                if ICG._tokens[ICG._tokensIndex].CP == ".":
                    ICG._tokensIndex += 1
                    if ICG._tokens[ICG._tokensIndex].CP == "ID":
                        ICG._tokensIndex += 1
                        if ICG._tokens[ICG._tokensIndex].CP == "(":
                            ICG._tokensIndex += 1
                            if self.PARAMS():
                                ICG._tokensIndex += 1
                                if ICG._tokens[ICG._tokensIndex].CP == ")":
                                    return True
                                else:
                                    sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
                        else:
                            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
                    else:
                        sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
                else:
                    sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))

            elif ICG._tokens[ICG._tokensIndex].CP == "ID":
                ICG._tokensIndex += 1
                if self.FUNC_CALL1():
                    return True
            else:
                sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))


    def FUNC_CALL1(self):
        if ICG._tokens[ICG._tokensIndex].CP==".":
            ICG._tokensIndex += 1
            if ICG._tokens[ICG._tokensIndex].CP == "ID":
                ICG._tokensIndex += 1
                if ICG._tokens[ICG._tokensIndex].CP == "(":
                    ICG._tokensIndex += 1
                    if self.PARAMS():
                        ICG._tokensIndex += 1
                        if ICG._tokens[ICG._tokensIndex].CP == ")":
                            return True
                        else:
                            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
                else:
                    sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
            else:
                sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
        elif ICG._tokens[ICG._tokensIndex].CP == "(":
            ICG._tokensIndex += 1
            if self.FUNC_CALL2():
                return True
        else:
            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))


    def FUNC_CALL2(self):
        if ICG._tokens[ICG._tokensIndex].CP == ")":
            ICG._tokensIndex += 1
            if self.FUNC_CALL3():
                return True
        elif self.DECL_ASGN():
            return True

        else:
            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))


    def FUNC_CALL3(self):
        if ICG._tokens[ICG._tokensIndex].CP=='.':
            ICG._tokensIndex += 1
            if ICG._tokens[ICG._tokensIndex].CP=='ID':
                ICG._tokensIndex += 1
                if ICG._tokens[ICG._tokensIndex].CP == '(':
                    ICG._tokensIndex += 1
                    if self.PARAMS():
                        ICG._tokensIndex += 1
                        if ICG._tokens[ICG._tokensIndex].CP == ')':
                            return True
                        else:
                            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
                else:
                    sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
            else:
                sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
        else:
            ICG._tokensIndex -= 1
            return True


    def PARAMS(self):
        if self.DECL_ASGN():
            return True
        else:
            ICG._tokensIndex -= 1
            return True

    #endregion

    #region IF-ELSE

    def IF_ELSE(self):
        if ICG._tokens[ICG._tokensIndex].CP=="if":
            ICG._tokensIndex += 1
            if ICG._tokens[ICG._tokensIndex].CP == "(":
                ICG._tokensIndex += 1
                IT1=self.createTemp()
                if self.E(IT1):
                    ICG._tokensIndex += 1
                    if ICG._tokens[ICG._tokensIndex].CP == ")":
                        IL1=self.createLabel()
                        self.generate("if("+IT1+"==FALSE)")
                        self.generate("JMP "+IL1)
                        ICG._tokensIndex += 1
                        if ICG._tokens[ICG._tokensIndex].CP == ":":
                            ICG._tokensIndex += 1
                            if self.BODY():
                                ICG._tokensIndex += 1
                                if self.ELIF(IL1):
                                    ICG._tokensIndex += 1
                                    if self.O_ELSE(IL1):
                                        return True
                        else:
                            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
                    else:
                        sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
            else:
                sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))


    def ELIF(self,eLabel):
        if ICG._tokens[ICG._tokensIndex].CP == "elif":
            ICG._tokensIndex += 1
            if self.E():
                ICG._tokensIndex += 1
                if ICG._tokens[ICG._tokensIndex].CP == ")":
                    ICG._tokensIndex += 1
                    if ICG._tokens[ICG._tokensIndex].CP == ":":
                        ICG._tokensIndex += 1
                        if self.BODY():
                            return True
                    else:
                        sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
                else:
                    sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
        else:
            self.generate(eLabel+":")
            ICG._tokensIndex -= 1
            return True

    def O_ELSE(self,oLabel):
        OL2=None
        if ICG._tokens[ICG._tokensIndex].CP == "else":
            OL2=self.createLabel()
            self.generate("JMP"+OL2)
            self.generate(oLabel+":")
            ICG._tokensIndex += 1
            if ICG._tokens[ICG._tokensIndex].CP == ":":
                ICG._tokensIndex += 1
                if self.BODY():
                    return True
            else:
                sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
        else:
            self.generate(OL2+":")
            ICG._tokensIndex -= 1
            return True

    #endregion

    def BODY(self):
        if ICG._tokens[ICG._tokensIndex].CP in ['ID', 'self', 'while', 'for', 'if', 'def']:
            if self.S_ST():
                return True
        elif ICG._tokens[ICG._tokensIndex].CP == "{":
            ICG._tokensIndex += 1
            if self.M_ST():
                ICG._tokensIndex += 1
                if ICG._tokens[ICG._tokensIndex].CP == "}":
                    return True
                else:
                    sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP, ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(ICG._tokens[ICG._tokensIndex].CP,ICG._tokens[ICG._tokensIndex].VP,ICG._tokens[ICG._tokensIndex].LN))

    def errorPrint(self,classPart,valuePart,lineNum):
        return "Error occur where class is "+classPart+" and value is "+valuePart+" line is "+str(lineNum)



    def createLabel(self):
        return "L"+ICG._labelNum+1


    def createTemp(self):
        return "t"+ICG._tempNum+1

    def generate(self,data):
        print(data)
