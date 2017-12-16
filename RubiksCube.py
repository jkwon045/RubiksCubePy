class Face:
    def __init__ (self,num):
        self.side = []
        for i in range (3):
            self.side.append([])
            for j in range (3):
                self.side[i].append(num)

    #prints the face
    def _out(self):
        for i in range(3):
            for j in range(3):
                print(self.side[i][j], end = ' ')
            print('\n')

    #function to rotate the face clockwise
    def _rotateCW(self):
        length = 2
        i = 0
        j = 0
        topRow = []
        rightCol = []
        bottomRow = []
        leftCol = []
        #save off row
        for x in range(3):
            topRow.append(self.side[0][x])
            bottomRow.append(self.side[2][x])
            leftCol.append(self.side[x][0])
            rightCol.append(self.side[x][2])
        
        #copy left column to top row backwards
        while(i < length):
            self.side[0][i] = leftCol[length-i]
            i+=1
        #copy top row to right column forwards
        while(j < length):
            self.side[j][2] = topRow[j]
            j+=1
        #copy right column to bottom row backwards
        for x in reversed(range(3)):
            self.side[2][x] = rightCol[length-x]
        #copy bottom row to left column forwards
        for x in range(3):
            self.side[x][0] = bottomRow[x]

    #function to rotate face counter clockwise
    def _rotateCCW(self):
        length = 2
        topRow = []
        rightCol = []
        bottomRow = []
        leftCol = []

        #copying off the rows to replace values later
        for x in range(3):
            topRow.append(self.side[0][x])
            bottomRow.append(self.side[2][x])
            leftCol.append(self.side[x][0])
            rightCol.append(self.side[x][2])

        #copy right column to top row forwards
        for x in range(3):
            self.side[0][x] = rightCol[x]
        #copy bottom row to right column backwards
        for x in reversed(range(3)):
            self.side[x][2] = bottomRow[length-x]
        #copy left column to bottom row
        for x in range(3):
            self.side[2][x] = leftCol[x]
        #copy top row to left column backwards
        for x in reversed(range(3)):
            self.side[x][0] = topRow[length-x]

        
    #function to change a column in the face
    def _changeCol(self, num, col):
        for i in range (3):
            self.side[i][col] = num

class Cube:
    def __init__(self, num0, num1, num2, num3, num4, num5):
        self.side0 = Face(num0) #front, orange
        self.side1 = Face(num1) #top, yellow
        self.side2 = Face(num2) #down, white
        self.side3 = Face(num3) #left, green
        self.side4 = Face(num4) #right, blue
        self.side5 = Face(num5) #back, red
#    def rotateR(self):
        

def main():
    face = Face(0)
    face._changeCol(1,0)
    face._changeCol(2,2)
    print('intiial:')
    face._out()

    face._rotateCW()
    print('rotate 1x: ')
    face._out()
    face._rotateCCW()
    print('rotate 2z: ')
    face._out()
    face._rotateCW()
    print('rotate 3z: ')
    face._out()
    face._rotateCCW()
    print('rotate 4z: ')
    face._out()
    face._rotateCW()
    print('rotate 5z: ')
    face._out()
main()
