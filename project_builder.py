#!/usr/bin/python

import subprocess
import sys
import os

project_name = sys.argv[1]
project_path = os.path.abspath(project_name)

template = 'autotools_template'
template_path = project_path + '/' + template

print project_path

git_remote = 'https://github.com/rafaeldelucena/'+ template + '.git'

retrieve_command = 'mkdir ' + project_path + ' && cd ' + project_path + ' && git clone ' + git_remote
print retrieve_command
subprocess.check_call(retrieve_command, shell=True)


print 'project_path: ', project_path
new_files = []
trunk, dirs, files = next(os.walk(template_path))

valid_files = filter(lambda a: a[0] != '.', files)
valid_dirs = filter(lambda a: a[0] != '.', dirs)

for a in valid_files:
    new_files.append(trunk + '/' + a)
for b in valid_dirs:
    trunk, sub_dirs, other_files = next(os.walk(template_path + '/' + b))
    for c in other_files:
        new_files.append(trunk + '/' + c)

for file in new_files:
    pattern = '\'s/' + template + '/' + project_name + '/g\''
    replace_command = 'sed -i ' + pattern + ' ' + file
    subprocess.check_call(replace_command, shell=True)

merge_command = 'cd ' + project_path + ' && rsync -avz ' + template_path + '/' + ' ' + project_path
subprocess.check_call(merge_command, shell=True)
subprocess.check_call('rm -rf ' + template_path, shell=True)

for e in valid_dirs:
    rename_command = 'cd ' + project_path + '/' + e + ' && rename ' + pattern + ' *'
    subprocess.check_call(rename_command, shell=True)
