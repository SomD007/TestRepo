from pypdf import PdfReader, PdfWriter

reader = PdfReader("maths.pdf")
writer = PdfWriter(clone_from=reader)
#meta=reader.metadata

#password= password
writer.encrypt("123", algorithm="RC4-128")

with open("encrypted-maths1.pdf","wb") as f:
    writer.write(f)
print("Done")

#print(meta)
#print(meta.creation_date)
#print(meta.creator)
