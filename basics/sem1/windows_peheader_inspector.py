import pefile   # pip install pefile
import sys


# pefile from https://github.com/erocarrera/pefile
# Only works with .exe (Windows Executables), sorry *.o files

def main():
    file = sys.argv[1]
    pe = pefile.PE(file)
    if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):     # the master list for imports, checks if it has the attribute
        for entry in pe.DIRECTORY_ENTRY_IMPORT: 
            print("%s" % entry.dll)     # prints the dll
            for imp in entry.imports:
                if(imp.name != None):
                    print("\t%s" % (imp.name))   # prints which functions are used from the import
                else:
                    print("\tord(%s)" % (str(imp.ordinal)))
            print("\n")


if __name__ == "__main__":
    try:
        main()
    except:
        print("No argument was provided")