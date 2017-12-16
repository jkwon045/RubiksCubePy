class Face:
    def __init__ (self,num):
        self.side = []
        for i in range (3):
            self.side.append([])
            for j in range (3):
                self.side[i].append(num)
    def out(self):
        for i in range(3):
            for j in range(3):
                print(self.side[i][j], end = ' ')
            print('\n')
    def rotateCW(self):
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
            
        #outputting every row
        print("Top: ", end = "")
        for x in range(3):
            print(topRow[x], end = " ")
        print("\nRight: ", end = " ")
        for x in range(3):
            print(rightCol[x], end = " ")
        print("\nBottom: ", end = " ")
        for x in range(3):
            print(bottomRow[x], end = " ")
        print("\nLeft: ", end = " ")
        for x in range(3):
            print(leftCol[x], end = " ")
        print("\n")
        
        #copy left column to top row
        while(i < length):
            self.side[0][i] = leftCol[length-i]
            i+=1
        #copy top row to right column
        while(j < length):
            self.side[j][2] = topRow[j]
            j+=1
        #copy right column to bottom row
        for x in reversed(range(3)):
            self.side[2][x] = rightCol[length-i]
        #copy bottom row to left column
        for x in range(3):
            self.side[x][0] = bottomRow[x]
    def changeCol(self, num, col):
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
    print("Hello World")
    face = Face(0)
    face.changeCol(1,0)
    face.changeCol(2,2)
    print('intiial:')
    face.out()
    face.rotateCW()
    print('rotate x1: ')
    face.out()
    face.rotateCW()
    face.out()
    face.rotateCW()
    face.out()
    face.rotateCW()
    face.out()
    face.rotateCW()
    face.out()
main()
