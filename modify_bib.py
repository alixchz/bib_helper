import os
import sys
import csv

abbreviations_csv = 'journal_abbreviations.csv'
# Récupère comme dict les abréviations de journaux, champs "short title" et "full title"
abbrev_dict = {}
with open(abbreviations_csv, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')  # Utiliser le séparateur ';'
    for row in reader:
        short_title = row['short_title'].strip()
        full_title = row['full_title'].strip()
        abbrev_dict[full_title] = short_title

if not len(sys.argv) == 3:
    print("Usage: python modify_bib.py source_file.bib new_file.bib")
    sys.exit(1)
source_file_bib = sys.argv[1]
new_bib = sys.argv[2]

if os.path.exists(new_bib):
    os.remove(new_bib)

fields_to_remove = ['doi', 'file', 'url']

for line in open(source_file_bib, 'r', encoding='utf-8'):
    write_line = True
    for field in fields_to_remove:
        if line.strip().startswith(field):
            write_line = False
            break
    if write_line:
        if line.strip().startswith('journal'):
            found_abbrev = False
            for journal_title in abbrev_dict:
                if journal_title in line:
                    short_title = abbrev_dict[journal_title]
                    line = line.replace(journal_title, short_title)
                    found_abbrev = True
                    break
            if not found_abbrev:
                print(f"Warning: No abbreviation found for journal in line: {line.strip()}")
            
            
        with open(new_bib, 'a', encoding='utf-8') as f:
            f.write(line)

