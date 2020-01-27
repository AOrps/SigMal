import pefile    # Using our old friend pefile
import sys

pe = pefile.PE(sys.argv[1])   # alternatively you can just put the location of the file
print(pe.get_imphash())    
