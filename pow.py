import os
import re

# if used Windows default directiry = r'C:\Windows\System32'
directory = '/Users/dmitrijmakarov'
file_name_pattern = re.compile(r'^pow\d{4}+')


for file in os.listdir(directory):
    if file_name_pattern.match(file):
        print(file)