import pefile    # Using our old friend pefile
import sys

def main():
    pe = pefile.PE(sys.argv[1])   # alternatively you can just put the location of the file
    print(pe.get_imphash())    

if __name__ == "__main__":
    if sys.argv[1] != "":
        main()