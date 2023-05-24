import json
import csv
import sys

def load_domains(file_path):
    domains_dict = {}
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            domains_dict[row[1]] = int(row[0])
    return domains_dict

def convert_json_to_csv(json_file, field, domains_dict):
    field_dict = {}
    next_id = 1
    field_csv_file = f'{field}.csv'
    field_domain_csv_file = f'{field}-to-domains.csv'
    
    with open(json_file, 'r') as f_json, \
         open(field_csv_file, 'w', newline='') as f_csv, \
         open(field_domain_csv_file, 'w', newline='') as fd_csv:
        json_data = json.load(f_json)
        field_writer = csv.writer(f_csv)
        field_domain_writer = csv.writer(fd_csv)
        
        field_writer.writerow(['id', field])
        field_domain_writer.writerow(['field_id', 'domain_id'])
        
        for obj in json_data:
            domain = obj.get('input')
            if domain in domains_dict:
                field_value = obj.get(field)
                if field_value and field_value not in field_dict:
                    field_dict[field_value] = next_id
                    field_writer.writerow([next_id, field_value])
                    field_domain_writer.writerow([next_id, domains_dict[domain]])
                    next_id += 1

def main(json_file, field, domains_file):
    domains_dict = load_domains(domains_file)
    convert_json_to_csv(json_file, field, domains_dict)

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python script.py data.json field domains.csv")
        sys.exit(1)

    json_file = sys.argv[1]
    field = sys.argv[2]
    domains_file = sys.argv[3]
    main(json_file, field, domains_file)
