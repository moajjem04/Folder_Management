# Utility script to sort my downloads folder

This a helper script written in python to sort the various files in any folders.
I usually use it for sorting my downloads.

The process is fairly simple.
In `utils.py` we have a function named `extension_to_folder()` which has a dictionary that maps all the various extensions to a folder name.

Based on that mapping, the code moves files to the new folder.
