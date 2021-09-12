# pip install python-magic  --> # src: https://github.com/ahupp/python-magic
import magic  


def main():
    f = magic.Magic()
    print(f.from_file("{PATH OF FILE}"))    # CHANGE THE STRING to ensure it reads in the correct file.

# This small script has the same functionality of the using the $((file)) command on Linux systems
if __name__ == "__main__":
    try:
        main()
    except:
        print("need to fill out the path of the file")