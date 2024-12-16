import os

def has_write_permission(path):
    """
    Check if the provided path has write permission.
    Returns True if writable, False otherwise.
    """
    try:
        os.makedirs(path, exist_ok=True)  # Ensure the path exists for testing
        test_file = os.path.join(path, ".permission_test")
        with open(test_file, "w") as f:
            f.write("test")
        os.remove(test_file)
        return True
    except (OSError, IOError):
        return False

# Enhanced Logging Function
def log_message(message):
    """
    Log messages to the console and optionally to a log file.
    """
    print(message)

# Path to the text file containing the directory and file structure
file_path = os.path.abspath("project_structure.txt")

# Check if the file exists
if not os.path.exists(file_path):
    log_message(f"Error: File not found: {file_path}")
    exit(1)

# Base directory where the structure will be created
base_dir = os.path.abspath(".")

# Check write permission for the base directory
if not has_write_permission(base_dir):
    log_message(f"Error: No write permission in the base directory: {base_dir}")
    exit(1)

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

        # Check if it's a file or folder based on extension
        if "." in os.path.basename(path):  # It's a file
            dir_name = os.path.dirname(full_path)
            # Check write permission for the directory
            if not has_write_permission(dir_name):
                log_message(f"Warning: No write permission in the directory: {dir_name}. Skipping file: {full_path}")
                continue

            os.makedirs(dir_name, exist_ok=True)  # Ensure parent directories exist
            try:
                with open(full_path, "w") as f:  # Create an empty file
                    pass
                log_message(f"Created file: {full_path}")
            except Exception as e:
                log_message(f"Error creating file {full_path}: {e}")
        else:  # It's a directory
            if not has_write_permission(full_path):
                log_message(f"Warning: No write permission to create directory: {full_path}. Skipping.")
                continue

            try:
                os.makedirs(full_path, exist_ok=True)
                log_message(f"Created directory: {full_path}")
            except Exception as e:
                log_message(f"Error creating directory {full_path}: {e}")
