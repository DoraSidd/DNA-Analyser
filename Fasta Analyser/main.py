from fasta_reader import read_fasta
from analyser import print_analysis , analysis_text , gc_content


genes = read_fasta("analyser.fasta")
report = open("results.txt" , "w")

total_genes = 0
total_length = 0
total_gc = 0

for name , dna in genes.items():
    print()
    print(f"========== {name} ==========")
    print()

    report.write(f"========== {name} ==========\n\n")
    report.write(f"DNA: {dna}\n\n")
    report.write(analysis_text(dna))
    report.write("\n\n")

    print_analysis(dna)

    total_genes += 1
    total_length += len(dna)
    total_gc += gc_content(dna)

average_length = total_length / total_genes
average_gc = total_gc / total_genes

# TXT PRINT
report.write("========== SUMMARY ==========\n\n")
report.write(f"Total genes analysed : {total_genes}\n")
report.write(f"Average length       : {average_length:.2f}\n")
report.write(f"Average GC content   : {average_gc:.2f}%\n")

# TERMINAL PRINT
print()
print("========== SUMMARY ==========")
print(f"Total genes analysed : {total_genes}")
print(f"Average length       : {average_length:.2f}")
print(f"Average GC content   : {average_gc:.2f}%")

report.close()