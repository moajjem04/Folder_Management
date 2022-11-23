import shutil

def extension_to_folder():
    e_t_f = {}

    e_t_f['pdf']        = 'PDF'
    e_t_f['docx']       = 'Docs'
    e_t_f['doc']        = 'Docs'
    e_t_f['txt']        = 'Text'
    e_t_f['ipynb']      = 'Notebooks'
    e_t_f['png']        = 'Images'
    e_t_f['jpg']        = 'Images' 
    e_t_f['jpeg']       = 'Images'
    e_t_f['csv']        = 'CSV'
    e_t_f['xlsx']       = 'Excel'
    e_t_f['xls']        = 'Excel'
    e_t_f['m']          = 'Matlab_code' 
    e_t_f['mat']        = 'Mat_files'
    e_t_f['zip']        = 'Zip'
    e_t_f['py']         = 'Python_code'
    e_t_f['rar']        = 'Zip'
    e_t_f['tar']        = 'Zip'
    e_t_f['mp4']        = 'Video' 
    e_t_f['pkl']        = 'Pickle_files'
    e_t_f['pickle']     = 'Pickle_files'
    e_t_f['pptx']       = 'Powerpoint'
    e_t_f['ppt']        = 'Powerpoint'
    e_t_f['jfif']       = 'Images'
    e_t_f['tex']        = 'LaTex'
    e_t_f['bib']        = 'LaTex' 
    e_t_f['bmp']        = 'Images'
    e_t_f['pickle']     = 'Pickle_files'
    e_t_f['pt']         = 'Python_storage_files'
    e_t_f['h5']         = 'Python_storage_files'
    e_t_f['npz']        = 'Python_storage_files'
    e_t_f['md']         = 'Markdown'
    e_t_f['joblib']     = 'Python_storage_files' 

    e_t_f['else']       = 'Other'

    return e_t_f

def move_file(source, destination):
    try:
        shutil.move(source, destination)
        #print("File copied successfully.")
    
    # # If source and destination are same
    # except shutil.SameFileError:
    #     print("Source and destination represents the same file.")
    
    # # If there is any permission issue
    except PermissionError:
        print("Permission denied.")
    
    # # For other errors
    # except:
    #     print("Error occurred while copying file.")


