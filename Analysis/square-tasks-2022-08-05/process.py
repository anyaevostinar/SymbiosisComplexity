import os.path
import gzip

folder = './'

treatment_postfixes = ["VT0.0", "VT1.0"]

fname = "../sample_treatment/munged_basic.dat"
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
    update = int(lineList[3])
    
    if (update not in table[partner].keys()):
        table[partner][update] = {}
    i = 4
    while (i < len(lineList)-1):
        squareNum = int(lineList[i][:-1]) #"9:"
        squareCount = int(lineList[i+1][:-1]) #"3;"
        if (squareNum not in table[partner][update].keys()):
            table[partner][update][squareNum] = 0
        table[partner][update][squareNum] += squareCount
        i += 2


outFile.write("partner update squareNum completions\n")
for partner in table.keys():
    for update in table[partner].keys():
        # print("=====================")
        # print("update:",update)
        squareNum = ""
        squareCount = ""
        for square in table['Host'][update].keys():
            squareNum = str(square)
            
            squareCount = str(table['Host'][update][square])
            
            outstring = "{} {} {} {}\n".format(partner, update,squareNum, squareCount)
            outFile.write(outstring)
        
    

curFile.close()
outFile.close()