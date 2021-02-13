import sys
import subprocess

# to make a signature based ids (the core components):
# compute hashes
# classify as malware or not

def usage():
    # prints how to use this script
    use = f"python3 demo-signatureBasedIDS.py (file)"
    print(f"Usage: ")
    print(use)

def get_repository():
    # populated a set with "malicious files"
    return {"d5570e17ad969b17a817936ae4381bee","e599eb9a0140ce7a5efc2859520a5b03"}

# hacky solution to output 
def byteToHashValue(byteRet):
    # converts b'return' value to str(hash) 
    decoByte = byteRet.decode('utf-8')
    value = decoByte.split(" ")[-1]
    return value


def main(file):
    # Ensure you have openssl prior to usage
    proc_byte = subprocess.check_output([
        "openssl",
        "md5",
        f"{file}"
    ])
    hashval = byteToHashValue(proc_byte).strip('\n')

    malSet = get_repository()

    if(hashval in malSet):
        print("Malware")



if __name__ == "__main__":
    try:
        first_cmd_line_arg = sys.argv[1]
    except:
        usage()
    
    main(first_cmd_line_arg)