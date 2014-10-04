#this will take Fasta format DNA strings and put into a dictionary
import sys

def fasta_to_dict():
    label = ""
    dna = ""
    dic = {}

    for tmp in sys.stdin.readlines():
        line = tmp.rstrip()
        if line[0] == ">":
            if label != "":
                dic[label] = dna
                dna = ""    
                label = line[1:]
            else:
                dna += line

    dic[label] = dna
