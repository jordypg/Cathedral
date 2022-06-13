from cat_pieces import pieceFromFile
from myarrays import nXnArray
from tkinter import *

def main():
    print("beginning a new run")
    p = pieceFromFile('academy', 'w')
    print(p)
    p.rotate(1)
    print(p)
    b = Board()
    print(b.makeMove((p, 4, 3)))
    print(b.makeMove((p, 7, 3)))
    #print(b.getIslands())



class LIFO():
    def __init__(self):
        self.stackList = []
    def isEmpty(self):
        if self.stackList == []:
            return True
        return False
    
    def push(self, item):
        self.stackList.append(item)
    def pop(self):
        popped = self.stackList[len(self.stackList)-1]
        self.stackList = self.stackList[:len(self.stackList) - 2]
        return popped
    def remove(self, item):
        if item in self.stackList:
            self.stackList.remove(item)
    def contains(self, item):
        if item in self.stackList:
            return True
        return False


class Connection():
    def __init__(self, n, x, y):
        self.n = n
        self.coordList = [(x, y)]
    
    def _in(self, x,y):
        if((x, y) in self.coordList):
            return True
        if(x == -1 and ((x+1, y) in self.CoordList)):
            return True
        if(x == n and ((x-1, y) in self.CoordList)):
            return True
        if(y == -1 and ((x, y+1) in self.CoordList)):
            return True
        if(y == n and ((x, y-1) in self.CoordList)):
            return True
        return False
        
    def countNeighbors(self, x, y):
        count = 0
        if(self._in(x+1, y)):
            count+=1
        if(self._in(x-1, y)):
            count+=1
        if(self._in(x, y+1)):
            count+=1
        if(self._in(x, y-1)):
            count+=1
        return count

    def checkIfEnclosure(self):
        for coord in self.coordList:
            if (self.countNeighbors(coord[0], coord[1]) < 2):
                return False
        return True

    #def canAdd(self, x, y):
        #for coordList

class Board:
    def __init__(self):
        self.blankValue = '.'
        self.array = nXnArray(10, self.blankValue)
        self.centersArray = nXnArray(10, '-')
        #self.array.setCoord('q', 1, 1)

    def __str__(self):
        return str(self.array)
    
    def moveToFilled(self, move):
        pieceFilled = move[0].getArray().getFilled()
        for i in range (len(pieceFilled)):
            pieceFilled[i] = (pieceFilled[i][0] + move[1] - 2, pieceFilled[i][1] + move[2] - 2)
        return pieceFilled


    #moves are of the form (piece, x, y)
    def checkOverlapLegality(self, move):
        boardFilled = self.array.getFilled()
        pieceFilled = self.moveToFilled(move)
        for coord in pieceFilled:
            if(coord in boardFilled):
                return False
        return True

    
    
    #returns list of lists of blank squares, each of the form [(x,y), ...]
    def getIslands(self):
        unassignedBlankSquares = []

        #list of lists
        islands = []

        for y in range(self.array.n):
            for x in range(self.array.n):
                if (self.array.getCoord(x, y) == self.blankValue):
                    unassignedBlankSquares.append((x,y))
        print('blank squares is ' + str(unassignedBlankSquares))
        
        #the dict is now full of blank square tuples
        while (unassignedBlankSquares != []):
            #pop square off front
            currentSquare = unassignedBlankSquares[0]

            assignedSquares = []

            currentIsland = {}
            possibleIslandSquares = LIFO()
            possibleIslandSquares.push((currentSquare, self.blankValue))

            while (not possibleIslandSquares.isEmpty()):
                possibleIslandSquare = possibleIslandSquares.pop()
                if (possibleIslandSquare[1] == self.blankValue):
                    #assign the square
                    currentIsland[possibleIslandSquare[0]] = possibleIslandSquare[1]
                    assignedSquares.append(possibleIslandSquare[0])

                    neighbors = self.array.getNeighbors((possibleIslandSquare[0])[0], (possibleIslandSquare[0])[1])
                    print('neighbors are ' + str(neighbors))
                    for neighbor in neighbors:
                        if neighbor[0] not in assignedSquares:
                            print('pushing square ' + str(neighbor))
                            possibleIslandSquares.push(neighbor)
                    #print(str(possibleIslandSquare))
                    #print(unassignedBlankSquares)
                    print('possible island square value is ' + str(possibleIslandSquare[1]) + ' with key ' + str(possibleIslandSquare[0]))
                    if possibleIslandSquare[1] == self.blankValue:
                        unassignedBlankSquares.remove(possibleIslandSquare[0])
                        if possibleIslandSquare[0] == (1,9):
                            print("REMOVING 1 9 !!!!!")
            print("current island is " + str(currentIsland))
            islands.append(currentIsland)
        
        return islands

    
    def makeMove(self, move):
        if (self.checkOverlapLegality(move) == True):
            for coord in self.moveToFilled(move):
                self.array.setCoord(move[0].getColor(), coord[0], coord[1])
            self.centersArray.setCoord(move[0].getColor(), move[1], move[2])
            return self
        else:
            return None

    
    


if __name__ == "__main__":
    main()