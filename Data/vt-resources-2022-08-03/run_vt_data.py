#a script to run several replicates of several treatments locally
#You should create a directory for your result files and run this script from within that directory
# usage: python3 simple_repeat.py <start_seed> <end_seed>
# Assumes that symbulation executable and SymSettings.cfg already in the folder

import subprocess
import sys

# verts = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
res = [0, 10, 25, 50, 75, 100, 200]
# mois = [0, 1]
# inflows = [100, 250, 500, 1000, 2500, 5000, 10000, 20000]

def cmd(command, wait):
    '''This wait causes all executions to run in sieries.                          
    For parralelization, remove .wait() and instead delay the                      
    R script calls unitl all neccesary data is created.'''
    c = subprocess.Popen(command, shell=True)
    if wait:
        return c.wait()
    else:
        return c

def silent_cmd(command):
    '''This wait causes all executions to run in sieries.                          
    For parralelization, remove .wait() and instead delay the                      
    R script calls unitl all neccesary data is created.'''
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).wait()

start_range = 10
end_range = 20

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

count = 0
for a in seeds:
    count += 1
    for b in res:
        command_str = f'./symbulation_sgp -SEED {a} -SYM_VERT_TRANS_RES {b} -FILE_NAME _VRES_{b}'
        settings_filename = "Output_VRES_"+str(b)+"_SEED"+str(a)+".data"

        print(command_str)
        # Run 4 processes at once
        cmd(command_str+" > "+settings_filename, False)#count % 4 == 0)
    # Now do it one more time without symbionts
    command_str = f'./symbulation_sgp -SEED {a} -START_MOI 0 -FILE_NAME _VRES_NONE'
    settings_filename = "Output_VRES_NONE_SEED"+str(a)+".data"

    print(command_str)
    cmd(command_str+" > "+settings_filename, count % 3 == 0)
