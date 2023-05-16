import csv
import sys

def split_csv(input_filename, output_prefix):
    # Create/open the output files
    with open(output_prefix + '_domains.csv', 'w', newline='') as domains_file, open(output_prefix + '_favicons.csv', 'w', newline='') as favicons_file, open(output_prefix + '_favtodomains.csv', 'w', newline='') as favtodomains_file:

        # Create CSV writer objects
        domains_writer = csv.writer(domains_file)
        favicons_writer = csv.writer(favicons_file)
        favtodomains_writer = csv.writer(favtodomains_file)

        # Write headers
        domains_writer.writerow(['id', 'url'])
        favicons_writer.writerow(['id', 'hash', 'path'])
        favtodomains_writer.writerow(['favicon_id', 'domain_id'])

        # Create favicon dictionary
        favicons = {}

        with open(input_filename, 'r') as input_file:
            csv_reader = csv.reader(input_file)

            for row in csv_reader:
                domain_id = row[0]
                domain_url = row[1]
                favicon_hash = row[2] if row[2] else None
                favicon_path = row[3] if row[3] else None

                # Write domain row
                domains_writer.writerow([domain_id, domain_url])

                if favicon_hash and favicon_path:
                    if (favicon_hash, favicon_path) not in favicons:
                        favicon_id = len(favicons) + 1
                        favicons[(favicon_hash, favicon_path)] = favicon_id
                        # Write favicon row
                        favicons_writer.writerow([favicon_id, favicon_hash, favicon_path])
                    else:
                        favicon_id = favicons[(favicon_hash, favicon_path)]
                    # Write favtodomains row
                    favtodomains_writer.writerow([favicon_id, domain_id])

if __name__ == "__main__":
    split_csv(sys.argv[1], sys.argv[2])
