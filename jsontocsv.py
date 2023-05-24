import json
import csv
import sys

def convert_json_to_csv(json_file, field, domains_dict):
    output_file = f'{field}.csv'
    field_to_domains_file = f'{field}-to-domains.csv'

    with open(json_file, 'r') as f_json, open(output_file, 'w', newline='') as f_output, open(field_to_domains_file, 'w', newline='') as f_field_domains:
        writer = csv.writer(f_output)
        field_domains_writer = csv.writer(f_field_domains)

        field_id_map = {}
        domain_id_map = {}

        next_field_id = 1
        next_domain_id = 1

        writer.writerow(['id', field])
        field_domains_writer.writerow(['field_id', 'domain_id'])

        for line in f_json:
            try:
                obj = json.loads(line.strip())
                domain = obj['input']
                field_value = obj.get(field)

                print("Domain:", domain)
                print("Field value:", field_value)

                if field_value:
                    field_id = field_id_map.get(field_value)
                    if not field_id:
                        field_id = next_field_id
                        field_id_map[field_value] = field_id
                        writer.writerow([field_id, field_value])
                        next_field_id += 1

                    domain_id = domain_id_map.get(domain)
                    if not domain_id:
                        domain_id = next_domain_id
                        domain_id_map[domain] = domain_id
                        field_domains_writer.writerow([field_id, domain_id])
                        next_domain_id += 1

                    print("Field ID:", field_id)
                    print("Domain ID:", domain_id)

            except json.JSONDecodeError:
                continue

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
