# DNA Sequence Analyzer

A small Python program that performs basic analysis on a DNA sequence.

The program uses the following DNA sequence:

```python
dna = "ATGGCCATTTAAGTAGCC"
```

## What it does

* Calculates the length of the DNA sequence
* Counts how many `A`, `T`, `G` and `C` bases it contains
* Calculates the GC content percentage
* Creates the complementary DNA strand
* Translates DNA codons into amino acids until it finds a stop codon

## How it works

The program uses dictionaries for:

* Complementary bases:

  * `A → T`
  * `T → A`
  * `G → C`
  * `C → G`

* Basic codon translation:

  * `ATG → M`
  * `GCC → A`
  * `ATT → I`
  * `GTA → V`
  * `TAA`, `TAG`, `TGA → STOP`

## Output

The program prints the results of the analysis, including the DNA length, base counts, GC content, complementary sequence, and translated protein.
