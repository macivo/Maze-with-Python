import numpy as np 
import os

foundPath = ""
def main():
    #read first how long is a line
    fileName = "./maze-one.txt"
    startValue = 2
    endValue = 3

    #create an empty array
    f = open(fileName, "r")
    length = len(f.readline()) -1
    fieldAsArray = np.empty((0,length), int)
    f.close

    #read file to numpy
    fieldAsArray = readField(fieldAsArray, fileName)
    startXY = searchPositon(fieldAsArray, startValue)
    endXY = searchPositon(fieldAsArray, endValue)

    #search the paht
    getWalkPaht(fieldAsArray,startXY,endXY)
    ### Deliverable 1 ###
    print("\nThe path from 'A' to 'B' is: " + foundPath + "\n")
    
    ### Deliverable 2 ###
    fieldAsArray = convertForPrinting(fieldAsArray, startXY) 
    printField(fieldAsArray)

def convertForPrinting(fieldAsArray, startXY):
    changeY=startXY[0]
    changeX=startXY[1]
    global foundPath
    foundPath = foundPath[:-1]
    for char in foundPath:
        if char == "N":
            changeY -= 1
            fieldAsArray[changeY][changeX] = 11
        if char == "S":
            changeY += 1
            fieldAsArray[changeY][changeX] = 12
        if char == "W":
            changeX -= 1
            fieldAsArray[changeY][changeX] = 13
        if char == "E":
            changeX += 1     
            fieldAsArray[changeY][changeX] = 14 
    return fieldAsArray

def getWalkPaht(fieldAsArray,startXY,endXY):
    sy = startXY[0]
    sx = startXY[1]
    
    def aroudCheck(sy, sx, moved, pathAsString):
        pathAsString += moved
        # if 'B' is found!!! 
        global foundPath
        if fieldAsArray[sy-1][sx] == 3:           
            foundPath += pathAsString + "N"
        if fieldAsArray[sy+1][sx] == 3:
            foundPath += pathAsString + "S"
        if fieldAsArray[sy][sx-1] == 3:
            foundPath += pathAsString + "W"
        if fieldAsArray[sy][sx+1]== 3:
            foundPath += pathAsString + "E"

        # 'N' (north)
        if(moved != "S" and sy-1 >= 0 and fieldAsArray[sy-1][sx] == 1):
            aroudCheck(sy-1, sx, "N", pathAsString)
        #'S' (south)
        if(moved != "N" and sy+1 <= len(fieldAsArray) and fieldAsArray[sy+1][sx] == 1):
            aroudCheck(sy+1, sx, "S", pathAsString)
        #'W' (west)
        if(moved != "E" and sx-1 >= 0 and fieldAsArray[sy][sx-1] == 1):
            aroudCheck(sy, sx-1, "W", pathAsString)
        #'E' (east) 
        if(moved != "W" and sx+1 <= len(fieldAsArray[0]) and fieldAsArray[sy][sx+1] == 1):
            aroudCheck(sy, sx+1, "E", pathAsString)
    aroudCheck(sy, sx, "", "")

def searchPositon(fieldAsArray, value):
    startPostiton = np.where(fieldAsArray == value)
    startXY = ()
    for i in startPostiton:
        j = int(i)
        coordinate = (j,)
        startXY += coordinate    
    return startXY    

def readField(fieldAsArray, fileName):
    #create numpy 2D arrays
    f = open(fileName, "r")
    strLine = ""
    for line in f:
        for x in line:
            if (x == "*"): 
                strLine += "0" 
            elif(x == " "):
                strLine += "1"
            elif (x == "A"):
                strLine += "2"
            elif (x == "B"):
                strLine += "3"
        one = np.array(list(strLine), dtype="int8")
        fieldAsArray = np.vstack((fieldAsArray,one))
        strLine = "" 
    f.close()
    return fieldAsArray

def printField(fieldAsArray):
    print("The graph as the text file with the path between 'A' and 'B' illustrated in the maze it self:")
    #print field
    for x in fieldAsArray:
        stringLine = ""
        pathImage = ""
        for y in x:
            if y == 11:
                y = "N"
            elif y == 12:
                y = "S"
            elif y == 13:
                y = "W"
            elif y == 14:
                y = "E"
            stringLine += str(y) 
            if y == 0:
                y = " "
            elif y == 1:
                y = " "
            pathImage += str(y)
        print(stringLine + "   ||   " + pathImage)
        del stringLine, pathImage

if __name__ == "__main__":
    main()
    input("\nPress Enter to exit the program :)")
