import os
import re

def rename_files(directory):
    for filename in os.listdir(directory):
        # Match only files that follow the 'label_*.png' pattern and capture the digits
        match = re.match(r'label_(\d+)\.png', filename)
        if match:
            number = match.group(1)
            new_name = f'image_{number}.png'

            # Constructing full file paths
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_name)

            # Renaming the file
            try:
                os.rename(old_file, new_file)
                print(f'Renamed {filename} to {new_name}')
            except OSError as e:
                print(f'Error renaming {filename}: {e}')

# Example usage
# combine file paths
directory_path = os.path.join(os.getcwd(), 'data_test', 'HorwarthDS', 'masks_positive')
rename_files(directory_path)