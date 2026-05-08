import os
import sys

fname = input("Enter input file name: ")

if not os.path.isfile(fname):
    print("File does not exist")
    sys.exit()

infile = open(fname, "r")
lines = infile.readlines()
infile.close()

linelist = []

for line in lines:
    linelist.append(line.strip())

linelist.sort()

outfile = open("sorted.txt", "w+")

for line in linelist:
    outfile.write(line + "\n")

outfile.seek(0, 0)

fstr = outfile.read()

print("sorted.txt contains", len(linelist), "lines")

outfile.close()