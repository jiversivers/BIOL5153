
# %%
# Set filename var to nucleotide data
filename = ('../example_files/dna.txt')


# %%
# Open the filename and assign to handle infile
infile = open(filename, 'r')


# %%
# Reading the dna sequence into a variable and removing trailing return
seq = infile.read().rstrip()


# %%
# Closing the file
infile.close()


# %%
# Displaying the length of the sequence
print('Sequence length:', str(len(seq)))


# %%
# Displaying different nt frequencies to 3 decimal places
numA = seq.count('A')/len(seq)
print('Freq of A:', str("%0.3f" % numA))
numC = seq.count('C')/len(seq)
print('Freq of C:', str("%0.3f" % numC))
numG = seq.count('G')/len(seq)
print('Freq of G:', str("%0.3f" % numG))
numT = seq.count('T')/len(seq)
print('Freq of T:', str("%0.3f" % numT))
print('G+C content:', str("%0.3f" % (numG + numC)))


# %%
# Checking frequency sum is 1
check=numA+numC+numG+numT
if check == 1 :
    print('Frequency check succesful.')
else :
    print('Error in frequency sum. Sum =', str(check))
# %%
