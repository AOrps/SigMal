import ssdeep     # pip install ssdeep

"""
Python Script to figure out the similarity of files via a method known fuzzy hashing
"""

hash1 = ssdeep.hash_from_file('{location of first executable}')  # be sure to fill in the location of the executable
hash2 = ssdeep.hash_from_file('{location of first executable}')

print(ssdeep.compare(hash1, hash2))
