import os.path
import gzip

folder = '../../Data/vt-resources-2022-08-03/'

#verts = ["NONE", 0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
res = ["NONE", 0, 10, 25, 50, 75, 100, 200]
reps = range(10,20)
header = "vres,rep,update,partner,donate_calls,donated,earned,task_NOT,task_NAND,task_AND,task_ORN,task_OR,task_ANDN,task_NOR,task_XOR,task_EQU"

outputFileName = "munged_tasks.csv"

outFile = open(outputFileName, 'w')
outFile.write(header)

for v in res:
    for r in reps:
            fname = f"{folder}Tasks_VRES_{v}_SEED{r}.data"
            curFile = open(fname, 'r')
            donatedFile = open(f"{folder}SymDonated_VRES_{v}_SEED{r}.data", 'r')
            donatedFile.readline()
            #print(f"----VT_{v}_SEED{r}----")
            for line in curFile:
                if (line[0] != "u"):
                    sym = True
                    vname = v
                    if v == "NONE":
                        vname = "No symbiont"
                        sym = False

                    splitline = line.split(',')
                    outstring1 = f"\n{vname},{r},{splitline[0]}"
                    dLine = donatedFile.readline().split(',')
                    # update,earned,calls,donated
                    #print(dLine)
                    outstring2 = f"{outstring1},symbiont,{dLine[2].strip()},{dLine[3].strip()},{dLine[1].strip()}"
                    outstring1 += ",host,0,0,0"
                    for i in range(1, len(splitline), 2):
                        outstring1 += "," + splitline[i].strip()
                        outstring2 += "," + splitline[i+1].strip()
                    outFile.write(outstring1)
                    if sym:
                        outFile.write(outstring2)
            curFile.close()
outFile.close()
