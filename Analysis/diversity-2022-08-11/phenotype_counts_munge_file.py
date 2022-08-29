import os
import os.path

import gzip

folder = '../../Data/diversity-2022-08-11' #change this if needed

verts = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
reps = range(10,18)
header = "rep, VT_rate, phenotype, count, partner\n"
sumHeader = "VT_rate, phenotype, sum_count, partner\n"

outputFileName = "munged_diversity_phenotype_counts.csv"
sumOutputFileName = "munged_diversity_phenotype_sums.csv"

outFile = open(outputFileName, 'w')
outFile.write(header)
sumOutFile = open(sumOutputFileName, 'w')
sumOutFile.write(sumHeader)


for v in verts:
    dict = {"host":{},"sym":{}} # this is for summing up counts
    for r in reps:
        fname = f"{folder}/_phenotype_counts__Diversity_{v}_SEED{r}.data"
        curFile = open(fname, 'r')
        print(f"----VT_{v}_SEED{r}----")
        
        curFile.readline()
        while True:
            string = curFile.readline()
            if not string:
                break
            
            line = string.split(' ')
            if(len(line)>1):
                outstring = "{}, {}, {}, {}, {}".format(r, v, line[0], line[1], line[2])
                outFile.write(outstring)
                if (line[0] in dict[line[2][0:-1]].keys()):
                    dict[line[2][0:-1]][line[0]] += int(line[1])
                else:
                    dict[line[2][0:-1]][line[0]] = int(line[1])
            else:
                print("error occured") # this line should not be reached                
        curFile.close()

    for partner in dict.keys():
        for phenotype in dict[partner].keys():
            sumOutstring = "{}, {}, {}, {}\n".format(v, phenotype, str(dict[partner][phenotype]), partner)
            sumOutFile.write(sumOutstring)
outFile.close()
sumOutFile.close()