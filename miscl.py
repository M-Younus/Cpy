

class Token:

    def __init__(self,CP,VP,LN):
        self.CP=CP
        self.VP=VP
        self.LN=LN


class baseMatrix:

    def __init__(self,name,scope):
        self.name=name
        self.scope=scope


class matVariables(baseMatrix):

    def __init__(self,name,type,scope):
        super(matVariables,self).__init__(name,scope)
        self.type=type

class matFunctions(baseMatrix):

    def __init__(self,name,pl,rt,scope):
        super(matFunctions,self).__init__(name,scope)
        self.PLRT=pl+"->"+rt