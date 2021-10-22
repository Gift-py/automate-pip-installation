
import sys
import subprocess

my_file = open("requirements.txt", "r")
content_list = my_file. readlines()

libraries = []
for i in range(len(content_list)):
    y = content_list[i].split('=')
    libraries.append(y[0])

#print(libraries)

#implemet pip as a subprocess
for x in range(len(libraries)):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', libraries[x]])

    #process output with an API in the subprocess module
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

print(installed_packages)
