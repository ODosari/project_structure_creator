import os

# Path to the text file containing the directory and file structure
file_path = "project_structure.txt"

# Base directory where the structure will be created
base_dir = "."

# Read the structure from the file and create directories and files
with open(file_path, "r") as file:
    for line in file:
        # Remove trailing spaces or newline characters
        path = line.strip()

        # Skip empty lines
        if not path:
            continue

        # Full path for the directory or file
        full_path = os.path.join(base_dir, path)

        if path.endswith('/'):  # If it ends with '/', treat it as a directory
            os.makedirs(full_path, exist_ok=True)
            print(f"Created directory: {full_path}")
        else:  # Otherwise, treat it as a file
            dir_name = os.path.dirname(full_path)
            os.makedirs(dir_name, exist_ok=True)  # Ensure parent directories exist
            with open(full_path, "w") as f:  # Create an empty file
                pass
            print(f"Created file: {full_path}")
