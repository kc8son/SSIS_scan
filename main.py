####################################################################################################
#
#   Date Written: 03/31/2023        By: Joseph P. Merten
#   This script will scan through a set of SSIS packages for the specified string.
#
####################################################################################################
#   imports
import pdb
import sys
import os
import csv

####################################################################################################
#   Variables
# file_location = "C:\_Tasks&Stories\DirectMailMkt"
pkg_path = "C:\\Git\\SSIS\\SSIS"
search_string = "estTransferToStage_CriticalStatusAddedEvent"
print(pkg_path)

####################################################################################################
#   functions
def find_string(my_file, my_string):
    """This function reads the ^.dtsx files and searches for the specified string."""
    line_found = 0
    with open(my_file) as f:
        my_lines = f.readlines()
        for my_line in my_lines:
            if my_string in my_line:
                if line_found == 0:
                    print(my_file)
                line_found += 1
                print("--", my_line)
    return line_found

def scan_pkgs(my_pkg_path, my_search_string):
    file_count = 0
    found_count = 0
    lines_found = 0
    for (dirpath, dirnames, filenames) in os.walk(my_pkg_path):
        for filename in filenames:
            if filename.endswith('.dtsx'):
                lines_found = find_string(os.sep.join([dirpath, filename]), my_search_string)
                if lines_found > 0:
                    found_count += 1
                    print(f"\tFound {found_count} times...")
                file_count += 1
    print(f">>>{file_count} files searched...")


####################################################################################################
#   Main code
if __name__ == '__main__':
    scan_pkgs(pkg_path, search_string)



