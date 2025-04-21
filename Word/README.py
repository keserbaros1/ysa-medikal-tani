import pypandoc


def convert_docx_to_md(input_file, output_file):
    """
    Converts a .docx file to a .md file using pypandoc.

    Args:
        input_file (str): Path to the input .docx file.
        output_file (str): Path to the output .md file.
    """
    try:
        pypandoc.convert_file(input_file, "md", outputfile=output_file)
        print(f"Dönüştürme tamamlandı: {output_file}")
    except Exception as e:
        print(f"Dönüştürme sırasında bir hata oluştu: {e}")


def convert_md_to_docx(input_file, output_file):
    """
    Converts a .md file to a .docx file using pypandoc.

    Args:
        input_file (str): Path to the input .md file.
        output_file (str): Path to the output .docx file.
    """
    try:
        pypandoc.convert_file(input_file, "docx", outputfile=output_file)
        print(f"Dönüştürme tamamlandı: {output_file}")
    except Exception as e:
        print(f"Dönüştürme sırasında bir hata oluştu: {e}")

# Örnek kullanım
convert_docx_to_md("Grup_7_README.docx", "README.md")

# convert_md_to_docx("README.md", "README.docx")