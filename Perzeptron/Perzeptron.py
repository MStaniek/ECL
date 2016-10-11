import math

class Perceptron:
    def __init__(self, dimensionen):
        self.weightvector=[0]*dimensionen
    def update(self, test):
        sum=0
        for a,b in enumerate(self.weightvector):
            sum+=b*test[a]
        result=sum*test[-1]
        if result <= 0:
            for a,b in enumerate(self.weightvector):
                self.weightvector[a]+=(test[-1]*test[a])
                self.weightvector[a]=round(self.weightvector[a], 5)
    def iteration(self, testlist):
        for i in range(10):
            for a, test in enumerate(testlist):
                self.update(test)
                print("Iteration " +str(i) + "." + str(a) + " " + str(self.weightvector))

percep=Perceptron(2)
Testlist=[[9.2, 17, 1], [8.8, 38, 1], [8.8, 7, 1], [1.2, 0, -1], [3.3, 1, -1], [5.8, 4, -1]]
percep.iteration(Testlist)
