import os.path
import gzip

folder = '../../Data/inflow-rate-2022-07-28/'

inflow_rates = [100, 250, 500, 1000, 2500, 5000, 10000, 20000]
reps = range(10,13)
header = "inflow,rep,update,partner,task_NOT,task_NAND,task_AND,task_ORN,task_OR,task_ANDN,task_NOR,task_XOR,task_EQU"

outputFileName = "munged_tasks.csv"

outFile = open(outputFileName, 'w')
outFile.write(header)

for t in inflow_rates:
    for r in reps:
            fname = f"{folder}Tasks_INFLOW_{t}_SEED{r}.data"
            curFile = open(fname, 'r')
            for line in curFile:
                if (line[0] != "u"):
                    splitline = line.split(',')
                    outstring1 = f"\n{t},{r},{splitline[0]}"
                    outstring2 = f"{outstring1},symbiont"
                    outstring1 += ",host"
                    for i in range(1, len(splitline), 2):
                        outstring1 += "," + splitline[i].strip()
                        outstring2 += "," + splitline[i+1].strip()
                    outFile.write(outstring1)
                    outFile.write(outstring2)
            curFile.close()
outFile.close()
