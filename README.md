# Usage
1. In the `modify_bib` file, edit the list `fields_to_remove` accordingly to your needs. 

2. Try:

```
python modify_bib [original_file.bib] [new_cleaned_file.bib]
```

You will see a list of warnings for journal abbreviations which are not in the database yet. 

3. Edit the file `journal_abbreviations.csv` to add them. Repeat step 2 if necessary.


> When adding new references and/or fields, make sure to do so in the original bib file and rerun the script in order not to lose data! The remove fields are not commented (not supported...) but erased in the cleaned bib.
