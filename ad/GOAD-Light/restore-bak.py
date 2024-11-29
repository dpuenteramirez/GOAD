import os

def restore_bak_files(root_folder):
    """
    Restores `.bak` files by renaming them to their original names, overwriting the modified files.

    :param root_folder: Root folder to start restoring.
    """
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith('.bak'):
                bak_file_path = os.path.join(dirpath, filename)
                # Determine the original file name by stripping the `.bak` extension
                original_file_path = bak_file_path[:-4]

                try:
                    # Restore the backup by renaming the .bak file
                    os.replace(bak_file_path, original_file_path)
                    print(f"Restored: {original_file_path}")
                except Exception as e:
                    print(f"Error restoring file {bak_file_path}: {e}")

# Example usage
root_folder = '.'  # Replace with your root folder path
restore_bak_files(root_folder)
