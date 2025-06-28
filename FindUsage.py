"""
Write a function 'find_disk_usage' takes directory name and threshold as arguments
1. It must iterate through all the subfolders recursively and find space occupied by them
"""
import os
import sys

def get_size(path):
    """Get the total size of a directory or file."""
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for dirname in dirnames:
                dp = os.path.join(dirpath, dirname)
                total_size += get_size(dp)
            for filename in filenames:
                fp = os.path.join(dirpath, filename)
                total_size += get_size(fp)
        return total_size
    return 0

def find_disk_usage(directory, threshold):
    folder_sizes = []
    for root, dirs, files in os.walk(directory):
        # Only process immediate subfolders of the given directory
        if root == directory:
            for subfolder in dirs:
                subfolder_path = os.path.join(root, subfolder)
                subfolder_size = get_size(subfolder_path)
                if subfolder_size > threshold:
                    folder_sizes.append((subfolder_path, subfolder_size))
            break  # Only process the top-level directory
    return folder_sizes
# Example usage
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python FindUsage.py <directory_path>")
        sys.exit(1)
    directory_to_check = sys.argv[1]
    size_threshold = 512 * 1024  # 1 MB
    large_folders = find_disk_usage(directory_to_check, size_threshold)
    for folder, size in large_folders:
        print(f"Folder: {folder}, Size: {size / (1024 * 1024):.2f} MB")