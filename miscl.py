

class Token:

    def __init__(self,CP,VP,LN):
        self.CP=CP
        self.VP=VP
        self.LN=LN


class baseMatrix:

    def __init__(self,name,scope):
        self.name=name
        self.scope=scope


class matFunctions(baseMatrix):

    def __init__(self,name,tpl,scope):
        super(matFunctions,self).__init__(name,scope)
        self.name=name
        self.scope=scope
        self.PL=tpl

class matClassesContainer(baseMatrix):

    def __init__(self,name,parent,link):
        self.name=name
        self.parent=parent
        self.link=link