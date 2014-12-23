import shutil
import os
def file_renamer(file_path, dest):
    #Create the rename string with '_' in place of '.'
    file_canonical = file_path.split('\\')
    file = file_canonical[len(file_canonical)-1]

    file_name = file.split('.')
    changed_name = ''
    for part_index in range( len(file_name) -1):
        if part_index == len(file_name) -2:
            changed_name += file_name[part_index]
        else:
            changed_name += file_name[part_index] + '_'

    path = ''
    for path_index in range( len(file_canonical)-1):
        path += file_canonical[path_index] + '\\'

    if dest == '':
        return path  + changed_name + '.' + file_name[len(file_name)-1]
    return dest + '\\' + changed_name + '.' + file_name[len(file_name)-1]

def file_copy(path_src, path_dst):
    #Copy the file to one directory. If path_dst is empty create a copy in the same directory
    os.chdir(path_src)
    file_list = os.listdir(path_src)
    for file in file_list:
        new_file_name = file_renamer(file, path_dst)
        shutil.copyfile(file, new_file_name)

###Change this line to src and dst
file_copy("Z:\\Downloads\\arrow_s01_un", 'C:\\Temp\\Arrow')
