# pip install python-magic  --> # src: https://github.com/ahupp/python-magic
import magic  

f = magic.Magic()
print(f.from_file("{PATH OF FILE}"))    # CHANGE THE STRING to ensure it reads in the correct file.

# This small script has the same functionality of the using the $((file)) command on Linux systems
