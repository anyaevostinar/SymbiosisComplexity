import os.path
import gzip

folder = '../../Data/sample_treatment/'

treatment_postfixes = ["VT0.0", "VT1.0"]
partners = ["Host", "Sym"]
reps = range(21,26)
header = "uid treatment rep update donate partner\n"

outputFileName = "munged_basic.dat"

outFile = open(outputFileName, 'w')
outFile.write(header)

for t in treatment_postfixes:
    for r in reps:
        for p in partners:
            fname = folder +p+"Vals_" + t +"_SEED" + str(r)+ ".data"
            uid = t + "_" + str(r)
            curFile = open(fname, 'r')
            for line in curFile:
                if (line[0] != "u"):
                    splitline = line.split(',')
                    outstring1 = "{} {} {} {} {} {}\n".format(uid, t, r, splitline[0], splitline[1], p)
                    outFile.write(outstring1)
            curFile.close()
outFile.close()
