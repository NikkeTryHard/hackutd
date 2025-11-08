import re
import os

# The name of your input markdown file
input_filename = r'C:\Users\louis\Desktop\hackathon\projects.md'

# The directory where you want to save the new files
output_directory = 'projects'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    print(f"Created directory: '{output_directory}'")

# Read the entire markdown file content
try:
    with open(input_filename, 'r', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print(f"Error: The file '{input_filename}' was not found.")
    exit()

# Use a regular expression to find all file blocks.
# This pattern looks for:
# - A line starting with '### File'
# - Captures the filename (e.g., 'asset_angel.json')
# - Captures the content within the ```json ... ``` block
# The re.DOTALL flag allows '.' to match newlines.
pattern = re.compile(r"### File \d+: `(.*?)`\s*```json\n(.*?)\n```", re.DOTALL)

# Find all matches in the content
matches = pattern.findall(content)

if not matches:
    print("No file blocks were found in the markdown file. Check the format.")
    exit()

# Loop through each found match
for filename, json_content in matches:
    # Construct the full path for the output file
    output_filepath = os.path.join(output_directory, filename)
    
    try:
        # Write the extracted JSON content to the new file
        with open(output_filepath, 'w', encoding='utf-8') as f:
            f.write(json_content)
        print(f"Successfully created '{output_filepath}'")
    except IOError as e:
        print(f"Error writing to file '{output_filepath}': {e}")

print(f"\nProcess complete. {len(matches)} files were created in the '{output_directory}' directory.")