#! /usr/bin/env python3

# This script generates a PBS file for the AHPCC Razor cluster

# define some variables
name ='name' # name to give job
queue = 'onenode16core' # queue to run job in
wall = 3 # this is in hours
nodes=1 # nodes to ask for
ppn=1 # processors to ask for

# This section prints the header/required info for the PBS script
print('#PBS -N',name) # Job name
print('#PBS -q', queue) # Which queue to use
print('#PBS -j oe') # Join STDOUT and STERROR into single file
print('#PBS -o', name +' .$PBS_JOBID') # Set name of job output file
print('#PBS -l nodes='+str(nodes)+':ppn='+str(ppn)) # How many resources to ask for (default 1 node, 1 processor)
print('#PBS -l walltime='+str(wall)+':00:00')# How much time to ask for, default to 3hr
print()

# cd into working directory
print ('cd $PBS_O_WORKDIR')
print()

# load the necessary modules
print('# load modules')
print('module purge')
print('module load gcc/7.2.1')
print()

# commands for this job
print('# insert commands here')