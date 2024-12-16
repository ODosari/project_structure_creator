
# Project Structure Creator

A Python script to automatically create a directory and file structure from a text file input. This tool is especially useful for initializing complex project structures quickly and efficiently.

## Features

- Reads a text file containing a directory and file structure.
- Creates directories and files as specified in the text file.
- Supports nested directory and file creation.
- Skips existing directories or files to prevent overwriting.

## Requirements

- Python 3.x

## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/project-structure-creator.git
   cd project-structure-creator
   ```

2. Ensure you have a text file defining the desired directory and file structure. For example:

   **`project_structure.txt`**:
   ```plaintext
   project/
   project/src/
   project/src/main.py
   project/tests/
   project/tests/test_main.py
   ```

3. Run the script:

   ```bash
   python create_structure.py
   ```

4. The script will create the specified directories and files in the current directory.

## Input File Format

- Lines ending with a `/` are treated as directories.
- Lines without a `/` are treated as files.
- Example structure:
  ```plaintext
  my_project/
  my_project/src/
  my_project/src/main.py
  my_project/tests/
  my_project/tests/test_main.py
  ```

## Example Output

Given the `project_structure.txt` file, the script will create the following structure:

```
my_project/
├── src/
│   └── main.py
└── tests/
    └── test_main.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

### Steps to Contribute

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.


