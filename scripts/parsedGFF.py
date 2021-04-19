#! /usr/bin/env python3

import csv
import argparse
from Bio import SeqIO
from collections import defaultdict
import re

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

# Dictionary: key = gene name, value = apphended list of exons (i.e. CDS)
cds = defaultdict(dict)

# Open and read in GFF file
with open(args.gff, 'r') as gff_in:
    # Create a csv reader object
    reader = csv.reader(gff_in, delimiter='\t')

# Loop over all the lines in our reader object (i.e., parsed file)
    for line in reader:
        # Check if sequence is an exon and add to gene CDS if so. Else skip the line
        if line[8].find('exon') > 0:
            start  = int(line[3]) # Start location of sequence
            end    = int(line[4]) # End location of sequence
            strand = line[6] # Which strand it's on
            header = line[0].split()[0].lower()+'_'+line[0].split()[1]+'_' # Creating formatted header line beginning for fasta output
            gene = re.search(r'(?<=Gene\s)\S+', line[8]) # Find and capture gene name from gff file
            key = '>'+header + gene.group(0)
            # Check if sequence is from + or - strand and reverse if -
            if strand == '+':
                sequence = genome.seq[start-1:end] # Minus 1 to account for zero-indexing and will be inclusive of final nucleotide
            else:
                sequence = genome.seq[start-1:end].reverse_complement() # Find reverse complement for - strand sequences
            if cds[key]:
                cds[key] = cds[key] + str(sequence).strip()
            else:
                cds[key] = '\n' + str(sequence).strip()

# Print the full CDS dictionary info in fasta format (with file name in commented-out header)
print('## '+name.capitalize())
for i in cds.keys():
    print(i, cds[i])
