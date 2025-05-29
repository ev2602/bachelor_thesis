import os
import subprocess

input_dir = "data/JeleniFiltered"
output_dir = "data/MSA"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get a list of all the files in the input directory
files = os.listdir(input_dir)

for file in files:
    # Construct the input and output file paths
    input_file = os.path.join(input_dir, file)
    output_file = os.path.join(output_dir, file)

    # Run MAFFT and save the aligned sequences to the output file
    command = f"mafft --op 2 --ep 0 --auto --reorder {input_file} > {output_file}"
    subprocess.run(command, shell=True)

    print(f"Alignment completed for {file}. Output saved to {output_file}")