import pefile    
import sys

# The code simply gets a hash of the section to figure out if the 
# file contains potentially malicious things

pe = pefile.PE(sys.argv[1]) 
for section in pe.sections: # simple for loop, iterating over the sections of the file
	print("%s\t%s" % (section.Name, section.get_hash_md5()))
