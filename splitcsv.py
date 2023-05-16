import csv
import sys

def split_csv(input_filename, output_prefix):
    # Create/open the output files
    with open(output_prefix + '_domains.csv', 'w', newline='') as domains_file, open(output_prefix + '_favicons.csv', 'w', newline='') as favicons_file, open(output_prefix + '_favtodomains.csv', 'w', newline='') as favtodomains_file:

        # Create CSV writer objects
        domains_writer = csv.writer(domains_file)
        favicons_writer = csv.writer(favicons_file)
        favtodomains_writer = csv.writer(favtodomains_file)

        # Write headers for the new CSV files
        domains_writer.writerow(['id', 'url'])
        favicons_writer.writerow(['id', 'hash', 'path'])
        favtodomains_writer.writerow(['favicon_id', 'domain_id'])

        # Open the input CSV file
        with open(input_filename, 'r') as f:
            reader = csv.reader(f)

            favicons = {}
            favicon_id = 1

            for row in reader:
                # Write a row to the domains file
                domains_writer.writerow([row[0], row[1]])

                # If the favicon hash is new, write a row to the favicons file and save the favicon_id
                if row[2] and row[2] not in favicons:
                    favicons[row[2]] = favicon_id
                    favicons_writer.writerow([favicon_id, row[2], row[3]])
                    favicon_id += 1
                elif row[2] == '':
                    favicons[row[2]] = None

                # Write a row to the favtodomains file
                favtodomains_writer.writerow([favicons[row[2]], row[0]])

    print("Files have been split successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_filename> <output_prefix>")
    else:
        split_csv(sys.argv[1], sys.argv[2])
