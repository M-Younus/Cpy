

class Token:

    def __init__(self,CP,VP,LN):
        self.CP=CP
        self.VP=VP
        self.LN=LN


class matFunctions:

    def __init__(self,name,tpl):
        self.name=name
        self.PL=tpl

class matClassesContainer:

    def __init__(self,name,parent,link):
        self.name=name
        self.parent=parent
        self.link=link

class matClasses:

    def __init__(self,name,type=0):
        self.name=name
        self.type=type