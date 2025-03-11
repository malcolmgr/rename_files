import os

def rename_image_files_sequentially(folder_path, new_filename_prefix):
    """
    Renames image files (.png, .jpg, .jpeg, .mov) in a folder sequentially,
    using a user-defined filename prefix and preserving extensions.

    Args:
        folder_path (str): The path to the folder to process (e.g., "d:/myfolder").
        new_filename_prefix (str): The desired prefix for the new filenames.
    """

    try:
        files = sorted(os.listdir(folder_path))
        count = 1

        for filename in files:
            file_name, file_extension = os.path.splitext(filename)
            if file_extension.lower() in (".png", ".jpg", ".jpeg", ".mov"):
                old_path = os.path.join(folder_path, filename)
                new_filename = f"{new_filename_prefix}_{count:03d}{file_extension}"
                new_path = os.path.join(folder_path, new_filename)

                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed '{filename}' to '{new_filename}'")
                    count += 1
                except OSError as e:
                    print(f"Error renaming '{filename}': {e}")

    except FileNotFoundError:
        print(f"Error: Folder not found at '{folder_path}'")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage with user input:
folder_to_rename = input("Enter the folder path: ")
new_filename_prefix = input("Enter the desired filename prefix: ")

rename_image_files_sequentially(folder_to_rename, new_filename_prefix)
