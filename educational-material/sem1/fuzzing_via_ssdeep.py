import ssdeep     # pip install ssdeep
import sys
"""
Python Script to figure out the similarity of files via a method known fuzzy hashing
"""

def cmd():
    res_line = "Between {} and {}, there is {:.2f} similiarity" # just formatting
    hash1 = ssdeep.hash_from_file(sys.argv[1]) #first file, first arg
    hash2 = ssdeep.hash_from_file(sys.argv[2])  # second file, second arg
    result = ssdeep.compare(hash1, hash2) # completes a fuzzy hash on 2 files supplied by cmd args
    print(res_line.format(sys.argv[1], sys.argv[2], result ))

def hardcode():
    hash1 = ssdeep.hash_from_file('{location of first executable}')  # be sure to fill in the location of the executable
    hash2 = ssdeep.hash_from_file('{location of second executable}')
    print(ssdeep.compare(hash1, hash2))

def main_cmd():
    if sys.argv[1] != "" and sys.argv[2] != "":
        cmd()

def main_hardcode():
    try:
        hardcode()
    except:
        print("need to fill out the location for both executables")

    
if __name__ == "__main__":
    main_cmd()
    #main_hardcode()