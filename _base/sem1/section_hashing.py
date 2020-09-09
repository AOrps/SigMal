import pefile    
import sys

# The code simply gets a hash of the section to figure out if the 
# file contains potentially malicious things

def main():
	pe = pefile.PE(sys.argv[1]) 
	for section in pe.sections: # simple for loop, iterating over the sections of the file
		print("%s\t%s" % (section.Name, section.get_hash_md5()))

if __name__ == "__main__":
	try:
		main()
	except:
		print("arguments  was not provided.")