import sys
import subprocess

import Dependencies

def InstallPackage(PackageName):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', PackageName])

for Package in Dependencies.Packages:
    InstallPackage(Package)
