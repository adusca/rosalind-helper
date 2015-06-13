# This will read a file with Fasta format DNA strings and return a list of tuples
def fasta_to_lst(filepath):
    label = ""
    dna = ""
    lst = []

    with open(filepath, 'r') as f:
        for tmp in f.readlines():
            line = tmp.rstrip()
            if line[0] == ">":
                if label != "":
                    lst.append((label, dna))
                    dna = ""
                label = line[1:]
            else:
                dna += line

        lst.append((label, dna))

    return lst
