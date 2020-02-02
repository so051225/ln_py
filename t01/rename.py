

import os
rootdir = 'xxx'
jar_path = 'x'

import subprocess
#subprocess.run(["java", "-cp", jar_path, 'zhcode', '-a7', oldfile_name, newfile_name])

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        oldfile_name = subdir + '/' + file
        if os.path.isfile(oldfile_name) and '.pdf' in file:    
            newfile_name = subdir + '/' + file.replace('xxx', '')
            os.rename(oldfile_name, newfile_name)
            # print('oldfile_name: %s, newfile_name: %s' % (oldfile_name, newfile_name))
        
    
