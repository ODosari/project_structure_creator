
# Project Structure Creator

A Python script to automatically create a directory and file structure from a text file input. This tool is especially useful for initializing complex project structures quickly and efficiently, including handling hidden files and directories.

## Features

- Reads a text file containing a directory and file structure.
- Creates directories and files as specified in the text file.
- Supports nested directory and file creation, including dotfiles and hidden directories.
- Checks for write permissions before creating directories or files to avoid errors.
- Logs actions, warnings, and errors for better traceability.
- Skips existing directories or files to prevent overwriting.

## Requirements

- Python 3.x

## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/ODosari/project_structure_creator.git
   cd project_structure_creator
   ```

2. Ensure you have a text file defining the desired directory and file structure. For example:

   **`project_structure.txt`**:
   ```plaintext
   project/
   project/src/
   project/src/main.py
   project/.env
   project/.git/
   project/.git/config
   ```

3. Run the script:

   ```bash
   python create_structure.py
   ```

4. The script will create the specified directories and files in the current directory.

## Input File Format

- Lines ending with a `/` are treated as directories.
- Lines without a `/` are treated as files.
- Supports hidden files (e.g., `.env`) and directories (e.g., `.git/`).
- Example structure:
  ```plaintext
  my_project/
  my_project/src/
  my_project/src/main.py
  my_project/.env
  my_project/.git/
  my_project/.git/config
  ```

## Example Output

Given the `project_structure.txt` file, the script will create the following structure:

```
my_project/
├── src/
│   └── main.py
├── .env
├── .git/
│   └── config
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

### Steps to Contribute

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

## License

Not yet added
