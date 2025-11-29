def create_codon_dict(file_path):
    codon_to_amino_acid_dict = {}
    with open(file_path) as codons_file:
        codon_to_amino_acid_dict = {row.strip().split('\t')[0]: row.strip().split('\t')[2] for row in codons_file.readlines()}
    return codon_to_amino_acid_dict
