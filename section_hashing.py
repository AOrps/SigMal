import pefile    
import sys

pe = pefile.PE(sys.argv[1])
for section in pe.sections:
	print("%s\t%s" % (section.Name, section.get_hash_md5()))
