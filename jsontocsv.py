import json
import csv
import sys

def convert_json_to_csv(json_file, field, domains_dict):
    output_file = f'{field}.csv'
    field_to_domains_file = f'{field}-to-domains.csv'

    with open(json_file, 'r') as f_json, open(output_file, 'w', newline='') as f_output, open(field_to_domains_file, 'w', newline='') as f_field_domains:
        json_data = (json.loads(line) for line in f_json)
        writer = csv.writer(f_output)
        field_domains_writer = csv.writer(f_field_domains)

        writer.writerow(['id', field])
        field_domains_writer.writerow(['field_id', 'domain_id'])

        next_id = 1

        for obj in json_data:
            domain = obj['input']
            field_value = obj.get(field)

            if field_value:
                field_id = next_id
                writer.writerow([field_id, field_value])
                next_id += 1

                domain_id = domains_dict.get(domain)
                if domain_id:
                    field_domains_writer.writerow([field_id, domain_id])

def load_domains(domains_file):
    domains_dict = {}
    with open(domains_file, 'r') as f_domains:
        reader = csv.reader(f_domains)
        for row in reader:
            domains_dict[row[1]] = int(row[0])
    return domains_dict

def main(json_file, field, domains_file):
    domains_dict = load_domains(domains_file)
    convert_json_to_csv(json_file, field, domains_dict)

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python jsontocsv.py data.json field domains.csv")
        sys.exit(1)

    json_file = sys.argv[1]
    field = sys.argv[2]
    domains_file = sys.argv[3]

    main(json_file, field, domains_file)
