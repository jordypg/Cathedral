from myarrays import nXnArray

def pieceFromFile(name, color):
    if name in ('academy', 'abbey'):
        filename = 'pieces/' + str(name) + '_' + str(color) + '.txt'
    else:
        filename = 'pieces/' + str(name) + '.txt'
    lines = []
    with open(filename) as f:
        lines = f.readlines()
    array = nXnArray(5, '.')
    for y in range(5):
        for x in range(5):
            array.setCoord(lines[y][x], x, y)
    piece = Piece(name, color, array)
    return piece


class Piece:
    def __init__(self, name, color, array):
        '''
        name is the name of the piece
        color is either "white" or "black"
        layout is a 5x5 grid, with "." where the piece isn't,
        and "#" where it is. Rotates around the center.
        '''
        self.name = name
        self.array = array
        self.color = color

        #calculate the size of the piece
        self.size = 0
        for y in range(5):
            for x in range(5):
                if (self.array.getCoord(x, y) != '.'):
                    if(color == 'w'):
                        self.array.setCoord('w', x, y)
                    if(color == 'b'):
                        self.array.setCoord('b', x, y)
                    self.size+=1
        #print(self.array)

    def __str__(self):
        return str(self.array)
    
    def getName(self):
        return self.name
    
    def getColor(self):
        return self.color

    def getSize(self):
        return self.size
    
    def getArray(self):
        return self.array
    
    def rotate(self, rotation):
        self.array.setLayout(self.array.getRotation(rotation))