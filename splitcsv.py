import csv
import sys

def main(input_file, output_root):
    favicons = {}
    domains = {}
    favicon_to_domain = []
    favicon_id = 1
    domain_id = 1

    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            url, favicon_hash, favicon_path = row
            # Skip this row if the favicon hash is empty
            if not favicon_hash:
                continue
            if favicon_hash not in favicons:
                favicons[favicon_hash] = (favicon_id, favicon_path)
                favicon_id += 1
            if url not in domains:
                domains[url] = domain_id
                domain_id += 1
            favicon_to_domain.append((favicons[favicon_hash][0], domains[url]))

    with open(f'{output_root}-favicons.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for favicon_hash, (favicon_id, favicon_path) in favicons.items():
            writer.writerow([favicon_id, favicon_hash, favicon_path])

    with open(f'{output_root}-domains.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for url, domain_id in domains.items():
            writer.writerow([domain_id, url])

    with open(f'{output_root}-favtodom.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for favicon_id, domain_id in favicon_to_domain:
            writer.writerow([favicon_id, domain_id])

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_root = sys.argv[2]
    main(input_file, output_root)
