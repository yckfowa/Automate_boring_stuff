import PyPDF4
import os
import sys

password = sys.argv[1]

for folder_name, subfolders, filenames in os.walk("."):

    for file in filenames:
        if file.endswith(".pdf"):
            path = os.path.join(folder_name, file)
            pdf_reader = PyPDF4.PdfFileReader(open(path, 'rb'))
            # if not pdf_file is not encrypted, copy the files and create new files
            if not pdf_reader.isEncrypted:
                pdf_writer = PyPDF4.PdfFileWriter()
                for page_num in range(pdf_reader.numPages):
                    pdf_writer.addPage(pdf_reader.getPage(page_num))

                pdf_writer.encrypt(password)
                encrypted_path = path[:-4] + '_encrpyted.pdf'

                encrypted_version = open(encrypted_path, 'wb')
                pdf_writer.write(encrypted_version)
                encrypted_version.close()

                pdf_reader = PyPDF4.PdfFileReader(open(encrypted_path, 'rb'))
                if (pdf_reader.isEncrypted is True
                        and pdf_reader.decrypt(password) == 1):
                    # if file successfully decrypted, will return 1 else 0
                    os.remove(path)
    print("All files in the folder have been encrypted and original files have been removed")

