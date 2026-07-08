#=========================================================
# DNA LIBRARIES
#=========================================================
complement = {"A":"T", "T":"A", "G":"C", "C":"G"}
genetic_code = {
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "TAT": "Y", "TAC": "Y", "TAA": "STOP", "TAG": "STOP",
    "TGT": "C", "TGC": "C", "TGA": "STOP", "TGG": "W",

    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",

    "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",

    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}
#=========================================================
# DNA LENGTH
#=========================================================
def sequence_length(dna):
    seq = 0
    for i in dna:
        seq += 1
    return seq

#=========================================================
# COUNT BASES
#=========================================================
def count_bases(dna):
    a = 0
    t = 0
    g = 0
    c = 0
    for base in dna:
        if base == "A":
            a += 1 
        elif base == "T":
            t += 1
        elif base == "G":
            g += 1
        elif base == "C":
            c += 1
    return a , t , g , c 

#=========================================================
# BASE PERCENTAGES
#=========================================================
def base_percentages(dna):
    a , t , g , c = count_bases(dna)
    length = sequence_length(dna)
    return (a / length * 100 , t / length * 100 , g / length * 100 , c / length * 100 )

#=========================================================
# GC CONTENT
#=========================================================
def gc_content(dna):
    g = 0
    c = 0
    for base in dna:
        if base == "G":
            g += 1
        if base == "C":
            c += 1
    gc = ((g+c) / len(dna))*100
    return gc

#=========================================================
# FIND THE ATG START CODON
#=========================================================
def find_start(dna):
    start = ""
    start = dna.find("ATG")
    return start

#=========================================================
# COMPLEMENT DNA
#=========================================================
def complement_dna(dna):
    comp = ""
    for base in dna:
        comp += complement[base]
    return comp

#=========================================================
# REVERSE COMPLEMENT DNA
#=========================================================
def reverse_complement(dna):
    comp = ""
    rev_comp = ""
    comp = complement_dna(dna)
    rev_comp = comp[::-1]
    return rev_comp

#=========================================================
# TRANSCRIPTION RNA
#=========================================================
def transcribe(dna):
    rna = ""
    rna = dna.replace("T" , "U")
    return rna

#=========================================================
# TRANSLATION
#=========================================================
def translate(dna):
    codon = ""
    amino_acid = ""
    protein = ""

    start = find_start(dna)
    if start == -1:
        return ""
    
    for i in range(start,len(dna),3):
        codon = dna[i:i+3]

        if len(codon) < 3:
            break

        amino_acid = genetic_code[codon]

        if amino_acid == "STOP":
            break
        protein += amino_acid
    return protein

#=========================================================
# VALIDATION
#=========================================================
def validate_dna(dna):
    for base in dna:
        if base not in "ATGC":
            return False
    return True  

#=========================================================
# EXPORT THE RESULTS IN THE RESULTS.TXT
#=========================================================
def analysis_text(dna):
    if not validate_dna(dna):
        return "Invalid DNA sequence!\n"

    seq = sequence_length(dna)
    a, t, g, c = count_bases(dna)
    a_per , t_per , g_per , c_per = base_percentages(dna)
    gc = gc_content(dna)

    start = find_start(dna)
    comp = complement_dna(dna)
    rev_comp = reverse_complement(dna)
    rna = transcribe(dna)
    protein = translate(dna)

    text = ""
    text += f"Length             : {seq}\n"
    text += f"A                  : {a} ({a_per:.2f}%)\n"
    text += f"T                  : {t} ({t_per:.2f}%)\n"
    text += f"G                  : {g} ({g_per:.2f}%)\n"
    text += f"C                  : {c} ({c_per:.2f}%)\n"
    text += f"GC Content         : {gc:.2f}%\n"
    text += f"ATG Position       : {start}\n"
    text += f"Complement         : {comp}\n"
    text += f"Reverse Complement : {rev_comp}\n"
    text += f"RNA                : {rna}\n"
    text += f"Protein            : {protein}\n"

    return text

#=========================================================
# DNA ANALYSIS
#=========================================================
def print_analysis(dna):
    print(analysis_text(dna))