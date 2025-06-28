# DiskSpace

DiskSpace is a set of Python utilities to measure and visualize disk space usage by files and folders on your system.

## Features

- **ShowFolderSize.py**:  
  An interactive GUI tool (Tkinter) to browse directories and view the size of each folder and file in a tree structure.  
  - Recursively calculates folder sizes, skipping symlinks to avoid infinite loops.
  - Displays human-readable sizes (e.g., KB, MB, GB).
  - Expands folders on demand for efficient navigation.
  - Keeps the UI responsive using background threads.

- **FindUsage.py**:  
  A command-line utility to scan a directory and report disk usage statistics.  
  - Lists files and folders sorted by size.
  - Supports recursive scanning.
  - Outputs results in a readable format for quick analysis.

## Usage

### ShowFolderSize.py

1. Run the script:
   ```
   python ShowFolderSize.py
   ```
2. Click "Choose Directory" to select a folder.
3. Browse the directory tree and view the size of each item.

### FindUsage.py

1. Run the script with the target directory as an argument:
   ```
   python FindUsage.py <directory_path>
   ```
2. View the output listing the largest files and folders.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- No external dependencies

## License

MIT License

---

*Created by Viv Krish. For questions or suggestions, please open an issue or contact the author.*
