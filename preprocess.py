import json
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

# Open the input and output files
with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    # Read each line from the input file
    for line in f_in:
        # Remove leading/trailing whitespaces
        line = line.strip()
        
        # Add curly braces at the beginning and end of the line
        line = '{' + line + '}'
        
        # Write the updated line to the output file
        f_out.write(line + '\n')

print("File processed successfully!")
