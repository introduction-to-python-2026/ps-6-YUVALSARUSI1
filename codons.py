  with open(file_path, "r") as file:
        lines = file.readlines()

    codon_to_amino_acid = {}
    for line in lines:
        stripped_line = line.strip()
        if not stripped_line:
            continue
        
        cells = stripped_line.split('\t')

        if len(cells) >= 3:
            codon = cells[0]
            amino_acid_abbr = cells[2]
            codon_to_amino_acid[codon] = amino_acid_abbr
            
    return codon_to_amino_acid
