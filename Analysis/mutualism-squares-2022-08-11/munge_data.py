import os.path
import gzip

folder = '../../Data/host-symbiont-squares-2022-08-09/'

verts = [0.0, 1.0]
reps = range(10,20)
header = "vert,rep,update,partner,donate_calls,donated,earned,mutualism,task_SQU"

outputFileName = "munged_tasks.csv"

outFile = open(outputFileName, 'w')
outFile.write(header)

for v in verts:
    for r in reps:
            fname = f"{folder}Tasks_VT{v}_SEED{r}.data"
            curFile = open(fname, 'r')
            #donatedFile = open(f"{folder}SymDonated_VT_{v}_SEED{r}.data", 'r')
            #donatedFile.readline()
            mutualismFile = open(f"{folder}SymImpact_VT{v}_SEED{r}.data", 'r')
            mutualism = mutualismFile.readline().strip()
            print("Mutualism", mutualism)
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
                    # update,earned,calls,donated
                    #print(dLine)
                    outstring2 = f"{outstring1},symbiont,{mutualism}"
                    outstring1 += ",host,0,0,0,NA"
                    for i in range(1, len(splitline), 2):
                        outstring1 += "," + splitline[i].strip()
                        outstring2 += "," + splitline[i+1].strip()
                    outFile.write(outstring1)
                    if sym:
                        outFile.write(outstring2)
            curFile.close()
            mutualismFile.close()
outFile.close()
