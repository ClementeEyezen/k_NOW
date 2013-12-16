from data import Token

class Multi_Token(Token):
    #a wrapper class of sorts that allows multiple single word tokens to be associate
    # for example the words fuel and cell might be associated as "fuel cell"
    def __init__(self, name1=None):
        global name
        global hasTokens
        hasTokens=[]
        name = name1
        
    def toString(self):
        string = ""
        for token in hasTokens:
            string = string+token.toString()
        return string
    
    def addToken(self,token):
        hasTokens.append(token)
        #tokens should stay in order
        #hasTokens.sort(token, key=token.toString().lower)
    
    def removeToken(self,target):
        for index, token in enumerate(hasTokens):
            if (token==target):
                hasTokens.remove(index)