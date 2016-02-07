class Node:
    dampingfactor=1 # hier den Wert ändern (siehe Folien)
    def __init__(self, name):
        self.To=set()
        self.From=set()
        self.OldPageRank=0
        self.NewPageRank=0
        self.Name=name

    def addChild(self, other):
        self.To.add(other)
        other.addParent(self)


    def addParent(self, other):
        self.From.add(other)

    def initialize(self, nodenumber):
        #Initialisiert den PageRankwert des Knotens mit 1/(Anzahl aller Knoten)
        self.OldPageRank=1/nodenumber
        self.NewPageRank=self.OldPageRank
        self.nodenumber=nodenumber

    def iterationPageRank(self):
        #iteriert über alle Nachbarknoten und fügt pro Nachbarknoten: Nachbarknotenpagerank/(Anzahl der ausgehenden Verbindungen) zu dem Urknoten hinzu
        self.NewPageRank=((1-Node.dampingfactor)/self.nodenumber)+Node.dampingfactor*(sum([no.OldPageRank/len(no.To) for no in self.From]))

    def iterationRandomWalk(self):
        #Die Wahrscheinlichkeit, das der Nachbarknoten auf den eigentlichen Knoten zeigt, ist 1/(Menge aller Nachbarknoten des Nachbarknotens)
        self.NewPageRank=(sum([no.OldPageRank/len(no.To) for no in self.From]))
    def finishIter(self):
        self.OldPageRank=self.NewPageRank

def printnodes(nodelist):
    #Gibt den Wert für jeden Knoten aus.
    for node in nodelist:
        print(node.Name + " New PageRank: " + str(node.NewPageRank))
    print()

def ini(nodelist):
    #Initialisiert alle Knoten in der Knotenliste mit dem dem Wert 1/(Anzahl der Knoten)
    for node in nodelist:
        node.initialize(len(nodelist))

def iterate(nodelist):
    #Geht über jeden Knoten drüber und
    for node in nodelist:
        node.iterationPageRank()
    for node in nodelist:
        node.finishIter()

def Main():
    #Es werden 4 Knoten erstellt
    node1=Node("node1")
    node2=Node("node2")
    node3=Node("node3")
    node4=Node("node4")
    #So sehen die Verbindungen aus:
    #      node1 ----node4
    #    /      \
    # node2-----node3
    node2.addChild(node1)
    node3.addChild(node1)
    Nodelist=[node1, node2, node3, node4]
    ini(Nodelist)
    print("Iteration 0:")
    printnodes(Nodelist)
    for i in range(1, 100):
        print("Iteration "+str(i))
        iterate(Nodelist)
        printnodes(Nodelist)

def Main2():
    A=Node("nodeA")
    B=Node("nodeB")
    C=Node("nodeC")
    D=Node("nodeD")
    E=Node("nodeE")
    F=Node("nodeF")
    G=Node("nodeG")
    H=Node("nodeH")
    I=Node("nodeI")
    J=Node("nodeJ")
    K=Node("nodeK")
    D.addChild(A)
    D.addChild(B)
    B.addChild(C)
    C.addChild(B)
    F.addChild(B)
    F.addChild(E)
    E.addChild(F)
    E.addChild(B)
    E.addChild(D)
    G.addChild(B)
    G.addChild(E)
    H.addChild(B)
    H.addChild(E)
    I.addChild(B)
    I.addChild(E)
    J.addChild(E)
    K.addChild(E)
    Nodelist=[A, B, C, D, E, F, G, H, I, J, K]
    ini(Nodelist)
    print("Iteration 0:")
    printnodes(Nodelist)
    for i in range(1, 1000):
        print("Iteration "+str(i))
        iterate(Nodelist)
        printnodes(Nodelist)
if __name__=="__main__":
    Main2()