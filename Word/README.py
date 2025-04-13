import pypandoc

# Markdown dosyasını docx formatına çevirme
pypandoc.convert_file("README.md", "docx", outputfile="README.docx")
print("Dönüştürme tamamlandı: README.docx")
