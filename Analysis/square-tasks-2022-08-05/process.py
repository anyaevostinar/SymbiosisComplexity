import os.path
import gzip

folder = './'

treatment_postfixes = ["VT0.0", "VT1.0"]

fname = "munged_basic.dat"
outputFileName = "table.dat"

outFile = open(outputFileName, 'w')

curFile = open(fname, 'r')
table = {'Host':{},'Sym':{}}
next(curFile) # skip the header line
lineNum = 1
while True:
    line1 = curFile.readline()
    line2 = curFile.readline()
    if (line1 == '\n'): break
    if not line2:break #end of file

    temp = line2.split(' ')
    partner = temp[1][:-1]
    lineList = line1.split(' ')
    vert = float(lineList[1][2:len(lineList[1])])
    update = int(lineList[3])
    
    if (vert not in table[partner].keys()):
        table[partner][vert] = {}
    if (update not in table[partner][vert].keys()):
        table[partner][vert][update] = {}
    i = 4
    while (i < len(lineList)-1):
        squareNum = int(lineList[i][:-1]) #"9:"
        squareCount = int(lineList[i+1][:-1]) #"3;"
        #print("Update: ", update, "SquareNum: ", squareNum, "SquareCount: ", squareCount)
        if (squareNum not in table[partner][vert][update].keys()):
            table[partner][vert][update][squareNum] = 0
        table[partner][vert][update][squareNum] += squareCount
        i += 2


outFile.write("partner vertical_transmission update squareNum completions\n")
for partner in table.keys():
    for vert in table[partner].keys():
        for update in table[partner][vert].keys():
        # print("=====================")
        # print("update:",update)
            squareNum = ""
            squareCount = ""
            for square in table[partner][vert][update].keys():
                squareNum = str(square)
                
                squareCount = str(table[partner][vert][update][square])
                
                outstring = "{} {} {} {} {}\n".format(partner, vert, update, squareNum, squareCount)
                outFile.write(outstring)
        
    

curFile.close()
outFile.close()