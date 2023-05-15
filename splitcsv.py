import csv
import sys

# Check command-line arguments
if len(sys.argv) != 3:
    print(f"Usage: python {sys.argv[0]} INPUT_FILENAME OUTPUT_ROOT")
    sys.exit(1)

input_filename = sys.argv[1]
output_root = sys.argv[2]

# Dictionaries for favicons and domains
favicons = {}
domains = {}
favicon_to_domain = []

# Read the input CSV file
with open(input_filename, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        url, favicon_hash, favicon_path = row
        if favicon_hash not in favicons:
            favicons[favicon_hash] = favicon_path
        if url not in domains:
            domains[url] = len(domains) + 1
        favicon_to_domain.append((favicon_hash, domains[url]))

# Write the favicons CSV file
with open(f"{output_root}-favicons.csv", 'w') as f:
    writer = csv.writer(f)
    for favicon_hash, favicon_path in favicons.items():
        writer.writerow([favicon_hash, favicon_path])

# Write the domains CSV file
with open(f"{output_root}-domains.csv", 'w') as f:
    writer = csv.writer(f)
    for url, id in domains.items():
        writer.writerow([id, url])

# Write the favicon-to-domain CSV file
with open(f"{output_root}-favtodom.csv", 'w') as f:
    writer = csv.writer(f)
    for favicon_hash, domain_id in favicon_to_domain:
        writer.writerow([favicon_hash, domain_id])
