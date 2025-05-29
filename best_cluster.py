import multiprocessing as mp
import subprocess
from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator
import sys

def run_mafft(op, ep, input_file, output_file):
    command = f"mafft --op {op} --ep {ep} --reorder {input_file} > {output_file}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    output, _ = process.communicate()
    aligned_seqs = output.decode().split(">")[1:]  # Assuming single-line sequences in the input file
    aligned_seqs = [seq.split("\n", 1)[1].replace("\n", "") for seq in aligned_seqs]
    return aligned_seqs

def calculate_distance(op, ep, input_file, counter):
    #Run MAFFT with specified op and ep values
    output_file = input_file[:-6] + "_o.fasta" 
    alignment = run_mafft(op, ep, input_file, output_file)

    alignment = AlignIO.read(output_file, 'fasta')
    
    #calculate distance matrix
    calculator = DistanceCalculator('identity')
    distance_matrix = calculator.get_distance(alignment)
    
    #save distance matrix in file
    output_file = f'J{counter}distance_matrix_op{op}_ep{ep}.txt'
    with open(output_file, 'w') as f:
        for row in distance_matrix:
            f.write('\t'.join(map(str, row)) + '\n')


op_values = [0, 1, 2, 5, 10]
ep_values = [0, 1, 2, 5, 10]

args = sys.argv[1:]
input_file = args[0]
counter = input_file[1:3]
calculate_distance(op, ep, input_file, counter)


for op in op_values:
    for ep in ep_values:
        pool.apply_async(calculate_distance, args=(op, ep))
        calculate_distance(op, ep)
