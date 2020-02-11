

import os
rootdir = ''
jar_path = 'x'

file_ext_whitelist = [] # means all
# file_ext_whitelist = ['.pdf', '.ipynb', '.nb', '.csv']

to_be_moved = ''

import subprocess
#subprocess.run(["java", "-cp", jar_path, 'zhcode', '-a7', oldfile_name, newfile_name])

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        oldfile_name = subdir + '/' + file
        # print(file)
        filename, file_extension = os.path.splitext(file)
        # print(file_extension)
        if os.path.isfile(oldfile_name) and ( len(file_ext_whitelist) ==0 or (file_extension in file_ext_whitelist)):    
            newfile_name = subdir + '/' + file.replace(to_be_moved, '')
            os.rename(oldfile_name, newfile_name)
            #print('oldfile_name: %s, newfile_name: %s' % (oldfile_name, newfile_name))
        
