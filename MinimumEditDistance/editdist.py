class Node:
    def __init__(self, X, Y, dictionary, A, B):
        if X > 0 and Y > 0:
            self.Parents=[dictionary[(X-1, Y-1)], dictionary[(X-1, Y)], dictionary[(X, Y-1)]]
        elif X > 0 and Y==0:
            self.Parents=[dictionary[(X-1, Y)]]
        elif Y > 0 and X==0:
            self.Parents=[dictionary[(X, Y-1)]]
        else:
            self.Parents=[]
        self.LetterA=A
        self.X=X
        self.Y=Y
        self.LetterB=B
        self.value=0
    def calcValue(self):
        SubstitutionCost=2 if self.LetterA!=self.LetterB else 0
        self.value=min([self.Parents[0].value+SubstitutionCost, self.Parents[1].value+1, self.Parents[2].value+1])
        #for node in self.Parents:
            #if node.value > self.value:
                #self.Parents.remove(node)

class Graph:
    def __init__(self, WortA, WortB):
        self.WortA="#"+WortA
        self.WortB="#"+WortB
        self.dictio=dict()
        for x, b in enumerate(self.WortA):
            for y, d in enumerate(self.WortB):
                node=Node(x, y, self.dictio, b, d)
                self.dictio[(x, y)]=node
    def initialise(self):
        for x,b in enumerate(self.WortA):
            self.dictio[x, 0].value=x
        for x,b in enumerate(self.WortB):
            self.dictio[0, x].value=x
    def calcValues(self):
        for x, b in enumerate(self.WortA):
            for y, d in enumerate(self.WortB):
                if x==0 or y==0:
                    continue
                self.dictio[(x, y)].calcValue()
        self.result=self.dictio[(len(self.WortA)-1, len(self.WortB)-1)].value
    def printGraph(self):
        print (" \t"+ "\t".join(self.WortB))
        for x, b in enumerate(self.WortA):
            print(b, end="\t")
            for y, d in enumerate(self.WortB):
                print(self.dictio[(x, y)].value, end="\t")
            print()
    def findAllResults(self, curNode=0, saveString="", maxval=100, valsave=0):
        #print(saveString)
        if valsave > maxval:
            return
        if curNode==0:
            curNode=self.dictio[(len(self.WortA)-1, len(self.WortB)-1)]
            maxval=curNode.value
        if curNode.X==0 and curNode.Y==0:
            print (saveString[::] + str(valsave))
        for node in curNode.Parents:
            val=str(node.value)
            if node.X == (curNode.X-1) and node.Y == (curNode.Y-1) and node.value==curNode.value:
                self.findAllResults(curNode=node, saveString=saveString+"M", maxval=maxval, valsave=valsave+0)
            if node.X == (curNode.X-1) and node.Y == (curNode.Y-1) and node.value==(curNode.value-2):
                self.findAllResults(curNode=node, saveString=saveString+"S", maxval=maxval, valsave=valsave+2)
            if node.X == (curNode.X-1) and node.Y == (curNode.Y) and node.value==(curNode.value-1):
                self.findAllResults(curNode=node, saveString=saveString+"D", maxval=maxval, valsave=valsave+1)
            if node.X == (curNode.X) and node.Y == (curNode.Y-1) and node.value==(curNode.value-1):
                self.findAllResults(curNode=node, saveString=saveString+"I", maxval=maxval, valsave=valsave+1)

if __name__=="__main__":
    test=Graph("pastor", "taste")
    test.initialise()
    test.calcValues()
    test.printGraph()
    print(test.findAllResults())


