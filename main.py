import hashlib

def crackHash(inputPass):
    try:
        passFile = open("wordlist.txt", "r")
    except:
        print("Could not find file")

    for password in passFile:
        encPass = password.encode("utf-8")
        digest = hashlib.sha256(encPass.strip()).hexdigest()
        if digest == inputPass:
            print("password found: " + password)

#paste or type hash of any password here(sha256), cracker will compare hashes to see if hash matches up with wordslist.
if __name__ == '__main__':
    #paste password hash here
    crackHash("55c05ceb08f50fb400ab7e57548891b660b3d08ffb40bf9e540112ded25cd7a4")