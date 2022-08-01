import os.path
import gzip

folder = '../../Data/vertical-transmission-2022-07-28/'

verts = ["NONE", 0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
reps = range(10,20)
header = "vert,rep,update,partner,donated,task_NOT,task_NAND,task_AND,task_ORN,task_OR,task_ANDN,task_NOR,task_XOR,task_EQU"

outputFileName = "munged_tasks.csv"

outFile = open(outputFileName, 'w')
outFile.write(header)

for v in verts:
    for r in reps:
            fname = f"{folder}Tasks_VT_{v}_SEED{r}.data"
            curFile = open(fname, 'r')
            donatedFile = open(f"{folder}SymDonated_VT_{v}_SEED{r}.data", 'r')
            donatedFile.readline()
            for line in curFile:
                if (line[0] != "u"):
                    sym = True
                    if v == "NONE":
                        v = "No symbiont"
                        sym = False

                    splitline = line.split(',')
                    outstring1 = f"\n{v},{r},{splitline[0]}"
                    dLine = donatedFile.readline().split(',')
                    # update,earned,donated
                    donated = float(dLine[2]) / float(dLine[1]) if dLine[1] != "0" else 0
                    outstring2 = f"{outstring1},symbiont,{donated}"
                    outstring1 += ",host,0"
                    for i in range(1, len(splitline), 2):
                        outstring1 += "," + splitline[i].strip()
                        outstring2 += "," + splitline[i+1].strip()
                    outFile.write(outstring1)
                    if sym:
                        outFile.write(outstring2)
            curFile.close()
outFile.close()
