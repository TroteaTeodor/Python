import hashlib
from difflib import SequenceMatcher

def hash_file(file1, file2):
    h1 = hashlib.sha1()
    h2 = hashlib.sha1()

    with open (file1, "rb") as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h1.update(chunk)

    with open (file2, "rb") as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h2.update(chunk)

    return h1.hexdigest(), h2.hexdigest()

msg1, msg2 = hash_file("pdf\pdf1.pdf", "pdf\pdf2.pdf")

if (msg1 != msg2):
    print("These files are not identical!")
else:
    print("These files are identical")