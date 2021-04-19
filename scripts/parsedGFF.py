#! /usr/bin/env python3

import csv
import argparse
from Bio import SeqIO

# Inputs: 1) GFF file, 2) Correspon ding genome sequence (FASTA) format

# Create an argument parser object
parser = argparse.ArgumentParser(description='This script will parse a GFF file and extract each feature from the genome')

# Add postional arguments
parser.add_argument('gff', help='name of the GFF file')
parser.add_argument('fasta', help='name of the FASTA file')

# Parse the arguments
args = parser.parse_args()

# Read in FASTA file
genome = SeqIO.read(args.fasta, 'fasta')

# Extract genome name from file name
name   = args.gff.split('.')[0]
# Open and read in GFF file
with open(args.gff, 'r') as gff_in:
    # Create a csv reader object
    reader = csv.reader(gff_in, delimiter='\t')

# Loop over all the lines in our reader object (i.e., parsed file)
    for line in reader:
        start  = int(line[3]) # Start location of sequence
        end    = int(line[4]) # End location of sequence
        strand = line[6]
        header = line[8] # GFF info of sequence
        print('>'+name, header)
        if strand == '+':
            print(genome.seq[start-1:end],'\n') # Minus 1 to account for zero-indexing and will be inclusive of final nucleotide
        else:
            sequence = genome.seq[start-1:end]
            rev_comp=sequence.reverse_complement() # Find reverse complement for - strand sequences
            print(rev_comp, '\n')