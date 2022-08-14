#a script to run several replicates of several treatments locally
#You should create a directory for your result files and run this script from within that directory
# usage: python3 simple_repeat.py <start_seed> <end_seed>
# Assumes that symbulation executable and SymSettings.cfg already in the folder

import subprocess
import sys
import time

verts = [0.0, 1.0]
NPROCS = 10
open_cmds = []
def cmd(command):
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

def silent_cmd(command):
    '''This wait causes all executions to run in series.                          
    For parralelization, remove .wait() and instead delay the                      
    R script calls unitl all neccesary data is created.'''
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).wait()

start_range = 10
end_range = 30

#collect optional command line arguments
if(len(sys.argv) > 1):
    #first argument is the starting range for seeds
    start_range = int(sys.argv[1])
    if(len(sys.argv) > 2):
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
        command_str = './symbulation_sgp -SEED '+str(a)+ ' -VERTICAL_TRANSMISSION ' +str(b)+ ' -FILE_NAME _VT'+str(b)
        settings_filename = "Output_VT"+str(b)+"_SEED"+str(a)+".data"

        print(command_str)
        cmd(command_str+" > "+settings_filename)

for i in open_cmds:
    i.wait()
