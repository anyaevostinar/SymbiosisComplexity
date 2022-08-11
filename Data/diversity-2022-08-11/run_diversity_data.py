#a script to run several replicates of several treatments locally
#You should create a directory for your result files and run this script from within that directory
# usage: python3 simple_repeat.py <start_seed> <end_seed>
# Assumes that symbulation executable and SymSettings.cfg already in the folder

import subprocess
import sys
import time

verts = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
# verts = [0.2]

path = '../../SymbulationEmp/'

NPROCS = 28
open_cmds = []

def cmd(command):
    '''This wait causes all executions to run in series.
    For parallelization, remove .wait() and instead delay the
    R script calls unitl all necessary data is created.'''
    c = subprocess.Popen(command, shell=True)
    open_cmds.append(c)
    while len(open_cmds) >= NPROCS:
        # Poll every 30 seconds for terminated processes
        time.sleep(30)
        i = 0
        while i < len(open_cmds):
            if open_cmds[i].poll() is not None:
                del open_cmds[i]
            else:
                i += 1


start_range = 10
end_range = 18

#collect optional command line arguments
if len(sys.argv) > 1:
    #first argument is the starting range for seeds
    start_range = int(sys.argv[1])
    if len(sys.argv) > 2:
        #if the user provides a second argument, use it
        #as the inclusive end of the seed range
        end_range = int(sys.argv[2]) + 1
    else:
        #if the user does not provide a second argument,
        #set the seed range as just the single seed 
        #indicated by the first argument
        end_range = start_range + 1

seeds = range(start_range, end_range)

#Tell the user the inclusive range of seeds
print("Using seeds", start_range, "through", end_range-1)


for a in seeds:
    for b in verts:
        command_str = f'./symbulation_sgp -SEED {a} -VERTICAL_TRANSMISSION {b} -FILE_NAME _Diversity_{b}'
        settings_filename = "Output_Diversity_"+str(b)+"_SEED"+str(a)+".data"

        print(command_str)
        # Run 4 processes at once
        cmd(command_str+" > "+settings_filename) #count % 4 == 0)
        # cmd(command_str,False)
    # Now do it one more time without symbionts
    command_str = f'./symbulation_sgp -SEED {a} -START_MOI 0 -FILE_NAME _Diversity_NONE'
    settings_filename = "Output_Diversity_NONE_SEED"+str(a)+".data"
    # cmd(command_str,False)

    print(command_str)
    cmd(command_str+" > "+settings_filename)
for i in open_cmds:
    i.wait()