import csv
import json
import sys

def convert_json_to_csv(json_file, field, domains_file):
    # Load the domains data from the CSV file
    domains_dict = {}
    with open(domains_file, 'r') as f_domains:
        csv_reader = csv.reader(f_domains)
        next(csv_reader)  # Skip the header
        for row in csv_reader:
            domain_id, domain = row
            domains_dict[domain] = domain_id

    # Open the output CSV files for writing
    output_csv_file = f'{field}.csv'
    field_to_domains_csv_file = f'{field}-to-domains.csv'
    with open(output_csv_file, 'w', newline='') as f_output, open(field_to_domains_csv_file, 'w', newline='') as f_field_to_domains:
        output_csv_writer = csv.writer(f_output)
        field_to_domains_csv_writer = csv.writer(f_field_to_domains)

        # Write the headers to the output CSV files
        output_csv_writer.writerow(['id', field])
        field_to_domains_csv_writer.writerow(['field_id', 'domain_id'])

        # Read the JSON data from the input file and convert it to CSV
        with open(json_file, 'r') as f_json:
            for line in f_json:
                data = json.loads(line)
                input_value = data['input']
                field_value = data[field]
                domain_id = domains_dict.get(input_value)

                # Write the data to the output CSV files
                output_csv_writer.writerow([domain_id, field_value])
                field_to_domains_csv_writer.writerow([domain_id, domain_id])

def main(json_file, field, domains_file):
    print(f"Processing {json_file}")
    print(f"Extracting field: {field}")

    convert_json_to_csv(json_file, field, domains_file)

    print("Conversion complete")

if __name__ == "__main__":
    json_file = sys.argv[1]
    field = sys.argv[2]
    domains_file = sys.argv[3]
    main(json_file, field, domains_file)
