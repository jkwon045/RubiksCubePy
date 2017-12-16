class Face:
    def __init__ (self,char):
        self.side = []
        for i in range (3):
            self.side.append([])
            for j in range (3):
                self.side[i].append(char)

    #prints the face
    def _out(self):
        visual = []
        for i in range(3):
            for j in range(3):
                visual.append(self.side[i][j])
                print(self.side[i][j], end = ' ')
            print('\n')
        return visual

    def _retRow(self, rowNum):
        return self.side[rowNum]

    def _retCol(self, colNum):
        tmp = []
        for i in range(3):
            tmp.append[i][colNum]
        return tmp

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
    def _changeCol(self, otherCol, colNum):
        for i in range(3):
            self.side[i][colNum] = otherCol[i]

    def _changeRow(self, otherRow, rowNum):
        for i in range(3):
            self.side[rowNum][i] = otherRow[i]

class Cube:
    def __init__(self, char0, char1, char2, char3, char4, char5):
        #front, orange
        self.side0 = Face(char0)
        #top, yellow
        self.side1 = Face(char1)
        #down, white
        self.side2 = Face(char2)
        #left, green
        self.side3 = Face(char3)
        #right, blue
        self.side4 = Face(char4)
        #back, red
        self.side5 = Face(char5)

    def _out(self):
        dummyFace = Face(" ")
        visual = []

        #appending to visual representation

        for i in range(3):
            visual.append(dummyFace._retRow(rowNum=0))
            visual.append(' ')
            visual.append(self.side1._retRow(rowNum=i))
            visual.append('\n')

        for i in range(3):
            visual.append(self.side3._retRow(rowNum = i))
            visual.append(' ')
            visual.append(self.side0._retRow(rowNum = i))
            visual.append(' ')
            visual.append(self.side4._retRow(rowNum = i))
            visual.append(' ')
            visual.append(self.side5._retRow(rowNum = i))
            visual.append('\n')

        for i in range(3):
            visual.append(dummyFace._retRow(rowNum=0))
            visual.append(' ')
            visual.append(self.side2._retRow(rowNum=i))
            visual.append('\n')

        for i in range(len(visual)):
            for j in range(len(visual[i])):
                if ( j == len(visual[i])-1):
                  print( visual[i][j], end = "" )
                else:
                    print(visual[i][j], end = " ")
        
        
        

def main():
    face = Face(0)
    dummy1 = [1, 1, 1]
    dummy2 = [2, 2, 2]
    face._changeCol(dummy1, colNum=0)
    face._changeRow(dummy2, rowNum=1)
    print('intiial:')
    face._out()

    face._rotateCW()
    print('rotate 1x: ')
    print(face._out())
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

    c = Cube('a', 'b', 'c', 'd', 'e', 'f')
    c._out()
main()
