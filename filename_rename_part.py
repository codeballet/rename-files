import os
import re
from pathlib import Path


def main():
    try:
        # Get directory info from user
        directory = input("Directory where files are: ")

        if not os.path.isdir(directory):
            raise ValueError(f"'{directory}' is not a valid directory")

        existing_files = [] # List to check for existing filenames
        directory_path = Path(directory) # Use for iterating files

        print("\nExisting files:")
        for item in directory_path.iterdir():
            if item.is_file():
                existing_files.append(item.name.lower()) # Add filename to checklist
                print(item.name) # Print existing filenames in lowercase

        # Ask user for pattern and replacement
        pattern = input("\nRegex pattern to replace:\n").lower()
        replacement = input("\nReplacement string:\n").lower()

        i = 0 # Counter for duplicate filenames

        for item in directory_path.iterdir():
            if item.is_file():
                print(f"\nChanging name of file: '{item.name}'")

                # Create a new filename suggestion
                new_name = re.sub(f"{pattern}", replacement, item.name.lower()).lower()

                if new_name == item.name.lower():
                    # The new filename is the same as before
                    print(f"No change for '{item.name}'. Just make sure to use lower case.")

                else:
                    # The filename is changed, check for duplicates
                    if new_name in existing_files:
                        print(f"Filename '{new_name}' already exists. Adding a suffix to avoid conflict.")
                        new_name = f"{os.path.splitext(new_name)[0]}_duplicate_{i}{os.path.splitext(new_name)[1]}"
                        i += 1

                print(f"Planned new filename is: {new_name}")

                # Rename the file
                dst = f"{directory}/{new_name}"
                src = f"{directory}/{item.name}"
                os.rename(src, dst)

        print("\nNew filenames:")
        for item in directory_path.iterdir():
            if item.is_file():
                print(item.name)

    except Exception as e:
        print(f"Error: {e}")
        


if __name__ == '__main__':
    main()
