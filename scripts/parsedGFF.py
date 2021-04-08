#! /usr/bin/env python3

import csv
import argparse
from Bio import SeqIO

# Inputs: 1) GFF file, 2) Correspon ding genome sequence (FASTA) format

# Create an argument parser object
parser = argparse.ArgumentParser(description='This script will parse a GFF file and extract each feature from the genome')

# Add postional arguments
parser.add_argument('gff', help='name of the GFF file')
parser.add_argument('fasta', help='namne of the FASTA file')

# Parse the arguments
args = parser.parse_args()

# GFF filename
gff_input = 'watermelon.gff'

# FASTA filename
fasta_input = 'watermelon.fsa'

# Open and read in GFF file
with open(args.gff, 'r') as gff_in:
    # Create a csv reader object
    reader = csv.reader(gff_in, delimiter='\t')

    # Loop over all the lines in our reader object (i.e., parsed file)
    for line in reader:
        start  = line[3]
        end    = line[4]
        strand = line[6]


# Read in FASTA file
genome = SeqIO.read(args.fasta, 'fasta')
print(genome.id)
print(len(genome.seq))

# Parse the GFF file
