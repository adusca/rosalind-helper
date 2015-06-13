with open('codon_table', 'r') as f:
    lines = f.readlines()
    pairs = [line.strip().split(' ') for line in lines]
    CODON_DICT = dict(pairs)

DNA_TO_RNA = {
    'A': 'A',
    'T': 'U',
    'G': 'G',
    'C': 'C'
}


def dna_to_rna(string):
    return ''.join(map(DNA_TO_RNA.get, string))


def codon_to_aminoacid(codon_array):
    return ''.join(map(CODON_DICT.get, codon_array))
