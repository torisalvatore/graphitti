#!/usr/bin/python3
import re
import sys
import csv
import os

def commentRemover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return " " # note: a space and not an empty string
        else:
            return s
    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    return re.sub(pattern, replacer, text)

def noempties(text):
    lines = text.split('\n')
    lines = [line for line in lines if line.strip()]
    return lines


directory = r"C:\Users\toris\OneDrive\Desktop\diffs\graphitti"

writer = csv.DictWriter(sys.stdout, fieldnames=['file', 'original_lines', 'code_lines'])
writer.writeheader()

for root, subdirectories, files in os.walk(directory):

    for file in files:
        path = os.path.join(root, file)

        with open(path, encoding="utf8") as f:
            contents = f.read()
            val = commentRemover(contents)
            val = noempties(val)
            writer.writerow({
                'file': file,
                'original_lines': contents.count('\n'),
                'code_lines': len(val)
            })





# THIS WORKS TO PRINT FILENAMES
# directory = r"C:\Users\toris\OneDrive\Desktop\diffs\graphitti"

# for root, subdirectories, files in os.walk(directory):
#     for subdirectory in subdirectories:
#         print(os.path.join(root, subdirectory))
#     for file in files:
#         print(os.path.join(file))
