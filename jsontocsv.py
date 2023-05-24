import csv
import json
import sys

json_file = sys.argv[1]
field = sys.argv[2]
domains_file = sys.argv[3]

def load_domains(file):
    domains_dict = {}
    with open(file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            domain_id, domain = row
            domains_dict[domain] = domain_id
    return domains_dict

def convert_json_to_csv(file, field, domains_dict):
    csv_file = f"{field}.csv"
    csv_to_domains_file = f"{field}-to-domains.csv"
    field_dict = {}
    domain_to_id = {}

    with open(file, 'r') as f_json, open(csv_file, 'w', newline='') as f_csv, open(csv_to_domains_file, 'w', newline='') as f_domains_csv:
        writer_csv = csv.writer(f_csv)
        writer_domains_csv = csv.writer(f_domains_csv)

        # Write the header row for CSV files
        writer_csv.writerow(['id', field])
        writer_domains_csv.writerow(['field_id', 'domain_id'])

        for line in f_json:
            try:
                data = json.loads(line)
                input_val = data.get('input')
                field_val = data.get(field)

                if input_val and field_val:
                    if field_val not in field_dict:
                        field_dict[field_val] = len(field_dict) + 1

                    field_id = field_dict[field_val]

                    if input_val in domains_dict:
                        domain = domains_dict[input_val]

                        if domain not in domain_to_id:
                            domain_to_id[domain] = len(domain_to_id) + 1

                        domain_id = domain_to_id[domain]

                        writer_csv.writerow([field_id, field_val])
                        writer_domains_csv.writerow([field_id, domain_id])

            except json.JSONDecodeError:
                print(f"Invalid JSON object: {line}")

    print(f"Conversion to CSV complete for field: {field}")

domains_dict = load_domains(domains_file)

convert_json_to_csv(json_file, field, domains_dict)
