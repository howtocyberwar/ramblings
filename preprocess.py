import json
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

# Open the input and output files
with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    # Read the input file line by line
    lines = f_in.readlines()

    # Process the lines in chunks of four
    for i in range(0, len(lines), 4):
        # Extract the JSON object from the lines
        json_data = ''.join(lines[i:i+4])

        # Parse the JSON object
        data = json.loads(json_data)

        # Write the JSON object to the output file
        json.dump(data, f_out)
        f_out.write('\n')

print("File processed successfully!")
