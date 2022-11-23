import os
from collections import Counter
from utils import extension_to_folder, move_file
from tqdm import tqdm    

if __name__ == '__main__':

    fol_to_manage = 'D:\\Opera Download'
    esc_border = "=="* 50
    print(f"\n{esc_border}")
    print(f"\nManaging folder - {fol_to_manage}")
    files = [f for f in os.listdir(fol_to_manage) if os.path.isfile(os.path.join(fol_to_manage, f))]
    print(f"\nThe folder has {len(files)} files")
    n = 5
    print(f'\nFirst {n} files are :')
    for i in range(n):
        print(f"  -->{files[i]}")
    
    file_exts = [i.split('.')[-1] for i in files]
    file_ext_dict = Counter(file_exts)
    file_ext_dict = dict(sorted(file_ext_dict.items(), key=lambda item: item[1], reverse= True))
    print(f"\nThere are {len(file_ext_dict)} different types of files:")
    print(f"\nThe first {n} are:")

    for ii, key in enumerate(file_ext_dict.keys()):
        print(f"  -->{key}\t\t{file_ext_dict[key]}")
        if ii == 4:
            break

    folders_available = extension_to_folder()
    c = 0
    c_in = 0
    not_counted = {}

    for ii, key in enumerate(file_ext_dict.keys()):
        if str(key).lower() in list(folders_available.keys()):            
            c_in += file_ext_dict[key]

        else:
            c += file_ext_dict[key]
            not_counted[key] = file_ext_dict[key]
    
    print(f"\nTotal {c_in} types of file accounted for and {c} types of file not accounted\n")
    # for ii, key in enumerate(not_counted.keys()):
    #     print(f"  -->{key}\t\t{not_counted[key]}")

    # Create Folders First
    for folder in folders_available.values():
        os.makedirs(os.path.join(fol_to_manage, folder), exist_ok= True)

    for f in tqdm(files, total = len(files)):
        ext = f.split('.')[-1]
        if ext.lower() in list(folders_available.keys()):
            folder = folders_available[ext.lower()]
        else:
            folder = 'Other'
        source = os.path.join(fol_to_manage, f)
        dest   = os.path.join(fol_to_manage, folder, f)
        move_file(source, dest)

