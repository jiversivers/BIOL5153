#! /usr/bin/env python3
# This script generates a slurm file for the AHPCC Pinnacle cluster

# define some variables
name ='name' # name to give job
queue = 'comp06' # queue to run job in
wall = 3 # this is in hours
nodes=1 # nodes to ask for
ppn=1 # processors to ask for

# This section prints the header/required info for the slurm script
print('#SBATCH -J', name) # name of job
print('#SBATCH --partition', queue) # swhich partition to run job
print('#SBATCH -o', name+'.txt') # Name of STDOUT file
print('#SBATCH -e', name+'.err') # Name of STERROR file
print('#SBATCH --mail-type=ALL') # set email alerts about job
print('#SBATCH --mail-user=jdivers@uark.edu') # email to send alerts to
print('#SBATCH --nodes='+str(nodes)) #number of nodes to run job on (default 1)
print('#SBATCH --ntasks-per-node='+str(ppn)) # processors to ask for (default 1)
print('#SBATCH --time='+str(wall)+':00:00') #time to ask for (default 3 hrs)
print()

print('export OMP_NUM_THREADS=32')
print()

print('# load required modules')
print('module load java')
print()

# cd into working directory
print('cd $SLURM_SUBMIT_DIR')

# copy files from storage to scratch
print('# input files needed for job')
print('files=')
print('rsync -av files /scratch/$SLURM_JOB_ID')
print()

# cd onto the scratch disk to run the job
print('cd /scratch/$SLURM_JOB_ID/')
print()

# commands for this job
print('# insert commands here')
print()
 
# copy output files back to storage
print('rsync -av', name, '$SLURM_SUBMIT_DIR')