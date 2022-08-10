import os.path
import gzip

folder = '../../Data/modularity-2022-08-10' #change this later

verts = [0.2,0.4]#0.4, 0.6, 0.8, 1.0
reps = range(10,18)
header = "host_pm, host_fm, sym_pm, sym_fm\n" #update,

outputFileName = "munged_modularity.csv"

outFile = open(outputFileName, 'w')
outFile.write(header)

#./Output_VT0.0_SEED10.data'
for v in verts:
    for r in reps:
            
            fname = f"{folder}Modularity_{v}_SEED{r}.data"
            curFile = open(fname, 'r')
            # donatedFile = open(f"{folder}SymDonated_VT_{v}_SEED{r}.data", 'r')
            # donatedFile.readline()
            # mutualismFile = open(f"{folder}SymImpact_VT_{v}_SEED{r}.data", 'r')
            # mutualism = mutualismFile.readline().strip()
            print(f"----VT_{v}_SEED{r}----")
            
            if (not is_file_empty(curFile)):
                string = curFile.readline()
                line = string.split(' ')
                outstring = "{}, {}, {}, {}".format(line[0], line[1], line[2], line[3])
                outFile.write(outstring)
                    
            curFile.close()
outFile.close()