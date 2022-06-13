class nXnArray():
    def __init__(self, n, blankValue = '0'):
        self.layout = {}
        self.n = n
        self.blankValue = blankValue

        for y in range(n):
            for x in range(n):
                self.layout[(x,y)] = blankValue

    def __str__(self):
        finalStr = ''
        for y in range(self.n):
            for x in range(self.n):
                finalStr = finalStr + str(self.layout[(x,y)]) + ' '
            if(y != self.n - 1):
                finalStr = finalStr + '\n'
        return finalStr
    
    def getCoord(self, x, y):
        return self.layout[(x,y)]
    
    def setCoord(self, value, x, y):
        self.layout[(x,y)] = value

    #returns a list of tuples of the form ((x,y), neighbor value)
    def getNeighbors(self, x, y):
        neighbors = []
        if(x - 1) >= 0:
            neighbors.append(  ( ((x-1), y), self.getCoord((x-1), y) )  )
        if(y - 1) >= 0:
            neighbors.append(  ( (x, (y-1)), self.getCoord(x, (y-1)) )  )
        if(x + 1) < self.n:
            neighbors.append(  ( ((x+1), y), self.getCoord((x+1), y) )  )
        if(y + 1) < self.n:
            neighbors.append(  ( (x, (y+1)), self.getCoord(x, (y+1)) )  )
        return neighbors
    
    def setLayout(self, layout):
        self.layout = layout
    
    def getLayout(self):
        return self.layout

    def getRotation(self, rotation):
        originalLayout = self.layout.copy()
        rotationLayout = self.layout.copy()
        for i in range(rotation):
            for endY in range(self.n):
                for endX in range(self.n):
                    rotationLayout[(endX, endY)] = originalLayout[endY, (self.n-1-endX)]
            originalLayout = rotationLayout.copy()
        return rotationLayout
    
    def getFilled(self):
        filledCoords = []
        for y in range(self.n):
            for x in range(self.n):
                if(self.getCoord(x,y) != self.blankValue):
                    filledCoords.append((x, y))
        return filledCoords