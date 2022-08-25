import os
import os.path

import gzip

folder = '../../Data/diversity-2022-08-11' #change this if needed

verts = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
reps = range(10,18)
header = "rep, VT_rate, alpha_diversity, shannon_diversity, species_richness, partner\n"

outputFileName = "munged_diversity.csv"

outFile = open(outputFileName, 'w')
outFile.write(header)

for v in verts:
    for r in reps:
        fname = f"{folder}/_diversity__Diversity_{v}_SEED{r}.data"
        curFile = open(fname, 'r')
        print(f"----VT_{v}_SEED{r}----")
        
        
        curFile.readline()
        for i in range(2):
            string = curFile.readline()
            
            line = string.split(' ')
            if(len(line)>1):
                outstring = "{}, {}, {}, {}, {}, {}".format(r, v, line[0], line[1], line[2], line[3])
                outFile.write(outstring)
            else:
                print("error occured")
                
        curFile.close()
outFile.close()