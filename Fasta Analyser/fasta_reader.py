

def read_fasta(analyser):
    f = open(analyser)
    sequences = {"Gene1": "ATGGCCATTTAAGTAGCC" , "Gene2": "ATGCGTGCGGCCTAA"}
    current_name = ""
    current_dna = ""
    
    for line in f:
        line = line.strip()

        if line == "":
            continue
        if line.startswith(">"):
            if current_name != "":
                sequences[current_name] = current_dna
            current_name = line[1:]
            current_dna = "" 
        else:
            current_dna += line
    f.close()
    sequences[current_name] = current_dna
    return sequences
