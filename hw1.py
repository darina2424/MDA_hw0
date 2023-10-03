from Bio import SeqIO


genome_records = SeqIO.parse("echi.fasta", "fasta")


start_codon = "ATG"
stop_codons = ["TAA", "TAG", "TGA"]
output_file = open("C:\genes\hw0\predict_bed", "w")
output_file.write("Gene_ID\tStart\tEnd\n")


for record in genome_records:
    sequence = str(record.seq)
    gene_found = False
    gene_start = None

    # поиск старт и стопа
    for i in range(0, len(sequence) - 2):
        codon = sequence[i:i + 3]

        if codon == start_codon:
            gene_start = i
            gene_found = True
        elif codon in stop_codons and gene_found:
            gene_end = i + 2
            output_file.write(f"{record.id}\t{gene_start + 1}\t{gene_end + 1}\n")
            gene_found = False


output_file.close()