import PyPDF4
import os
import sys


password = sys.argv[1]

for folder_name, subfolders, filenames in os.walk("."):

    for file in filenames:
        if file.endswith(".pdf"):
            path = os.path.join(folder_name, file)
            pdf_reader = PyPDF4.PdfFileReader(open(path, 'rb'))

            if pdf_reader.isEncrypted is True:
                pdf_reader.decrypt(password)
                pdf_writer = PyPDF4.PdfFileWriter()
                for page_num in range(pdf_reader.numPages):
                    pdf_writer.addPage(pdf_reader.getPage(page_num))

                decrypted_path = path[:-14] + '_decrpyted.pdf' # make the name look better in easy way, could have better ways
                decrypted_version = open(decrypted_path, 'wb')
                pdf_writer.write(decrypted_version)
                decrypted_version.close()

    print("Files have been decrypted")

