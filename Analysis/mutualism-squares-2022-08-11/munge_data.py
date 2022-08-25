import os.path
import gzip

folder = '../../Data/host-symbiont-squares-2022-08-09/'

verts = [0.0, 1.0]
reps = range(10,20)
header = "vert,rep,update,partner,donate_calls,donated,earned,mutualism,attempts_horiz,success_horiz,attempts_vert,task_NOT,task_NAND,task_AND,task_ORN,task_OR,task_ANDN,task_NOR,task_XOR,task_EQU"

outputFileName = "munged_tasks.csv"

outFile = open(outputFileName, 'w')
outFile.write(header)

for v in verts:
    for r in reps:
            fname = f"{folder}Tasks_VT{v}_SEED{r}.data"
            curFile = open(fname, 'r')
            #donatedFile = open(f"{folder}SymDonated_VT{v}_SEED{r}.data", 'r')
            #donatedFile.readline() # skip header
            mutualismFile = open(f"{folder}SymImpact_VT{v}_SEED{r}.data", 'r')
            transFile = open(f"{folder}TransmissionRates_VT{v}_SEED{r}.data", 'r')
            transFile.readline() # skip header
            #print(f"----VT_{v}_SEED{r}----")
            for line in curFile:
                if (line[0] != "u"):
                    # Split mutualism across updates so we have somewhere to put each line,
                    # even though all that data is really from the last update.
                    mutualism = (mutualismFile.readline() or "NA").strip()
                    sym = True
                    vname = v
                    if v == "NONE":
                        vname = "No symbiont"
                        sym = False

                    splitline = line.split(',')
                    outstring1 = f"\n{vname},{r},{splitline[0]}"
                    # update,earned,calls,donated
                    #dLine = donatedFile.readline().split(',')
                    # update,attempts_horiz,success_horiz,attempts_vert
                    tLine = transFile.readline().split(',')
                    outstring2 = f"{outstring1},symbiont,{mutualism}"
                    outstring2 += f",{tLine[1].strip()},{tLine[2].strip()},{tLine[3].strip()}"
                    outstring1 += ",host,0,0,0,NA,NA,NA,NA"
                    for i in range(1, len(splitline), 2):
                        outstring1 += "," + splitline[i].strip()
                        outstring2 += "," + splitline[i+1].strip()
                    outFile.write(outstring1)
                    if sym:
                        outFile.write(outstring2)
            curFile.close()
            #donatedFile.close()
            mutualismFile.close()
outFile.close()

