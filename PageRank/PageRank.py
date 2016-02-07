'''
Autor: Michael Staniek
Datum: 05.02.2016
'''

class Node:
    dampingfactor=0.85 # hier den Wert ändern (siehe Folien)
    def __init__(self, name):
        self.neighbors=[]
        self.connections=0
        self.OldPageRank=0
        self.NewPageRank=0
        self.Name=name

    def addNeighbor(self, other):
        #Fügt einen Knoten zu diesem Knoten hinzu, ruft dann addNeighborAround auf, damit der andere Knoten auch eine Verbindung zurück hat.
        self.neighbors.append(other)
        other.addNeighborAround(self)
        self.connections+=1

    def addNeighborAround(self, other):
        self.neighbors.append(other)
        self.connections+=1

    def initialize(self, nodenumber):
        #Initialisiert den PageRankwert des Knotens mit 1/(Anzahl aller Knoten)
        self.OldPageRank=1/nodenumber
        self.NewPageRank=self.OldPageRank
        self.nodenumber=nodenumber

    def initializeZero(self, nodenumber):
        self.OldPageRank=0
        self.NewPageRank=self.OldPageRank
        self.nodenumber=nodenumber

    def iterationPageRank(self):
        #iteriert über alle Nachbarknoten und fügt pro Nachbarknoten: Nachbarknotenpagerank/(Anzahl der ausgehenden Verbindungen) zu dem Urknoten hinzu
        self.NewPageRank=((1-Node.dampingfactor)/self.nodenumber)+Node.dampingfactor*(sum([no.OldPageRank/len(no.neighbors) for no in self.neighbors]))

    def iterationRandomWalk(self):
        #Die Wahrscheinlichkeit, das der Nachbarknoten auf den eigentlichen Knoten zeigt, ist 1/(Menge aller Nachbarknoten des Nachbarknotens)
        self.NewPageRank=(sum([no.OldPageRank/len(no.neighbors) for no in self.neighbors]))
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
        node.initializeZero(len(nodelist))

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
    node5=Node("node5")
    node6=Node("node6")
    #So sehen die Verbindungen aus:
    #      node1 ----node4
    #    /      \
    # node2-----node3
    node1.addNeighbor(node2)
    node1.addNeighbor(node3)
    node2.addNeighbor(node3)
    node1.addNeighbor(node4)
    node5.addNeighbor(node2)
    node6.addNeighbor(node3)
    Nodelist=[node1, node2, node3, node4, node5, node6]
    ini(Nodelist)
    node4.OldPageRank=1
    node4.NewPageRank=1
    print("Iteration 0:")
    printnodes(Nodelist)
    for i in range(1, 100+1):
        print("Iteration "+str(i))
        iterate(Nodelist)
        printnodes(Nodelist)

if __name__=="__main__":
    Main()