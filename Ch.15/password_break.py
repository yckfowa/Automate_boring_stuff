import PyPDF4
import os

for folder_name, subfolders, filenames in os.walk("."): 
    for file in filenames:
        if file.endswith(".pdf"):
            path = os.path.join(folder_name, file)
            pdf_reader = PyPDF4.PdfFileReader(open(path, "rb"))
            if pdf_reader.isEncrypted:
                with open('password.txt', "r") as f:  # specify own txt file
                    for w in f.read().split("\n"):
                        if pdf_reader.decrypt(w) == 1:
                            print(f"File successfully decrypted, password is {w}")
                        else:
                            print("Nothing matched")


