# Import functions from process_text.py and write_to_file.py
from process_text import process_line
from write_to_file import train_test_split_write_files

# Define the input and output paths and the ratio for splitting data
input_path = 'input_data.txt'
output_path = 'output_dir'
test_ratio = 0.15
val_ratio = 0.15

# Read the input file into a list of string lines
with open(input_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Process each line using the process_line() function from process_text.py
processed_lines = [process_line(line).strip() for line in lines]

# Split the processed data into three sets using the train_test_split_write_files() function from write_to_file.py
train_data, test_data, val_data = train_test_split_write_files(processed_lines, output_path, test_ratio, val_ratio)

print('Data processing and splitting is complete!')