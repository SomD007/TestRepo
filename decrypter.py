from pypdf import PdfReader, PdfWriter

reader=PdfReader("encrypted-maths1.pdf")

for i in range(1,200):
    if reader.is_encrypted:
        j=str(i)
        reader.decrypt("123")
        print(i)
    else:
        print("Value=",i)
        break
        