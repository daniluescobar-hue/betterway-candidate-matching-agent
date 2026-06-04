from pypdf import PdfReader

def read_pdf(pdf_path):

    text = ""

    try:
        reader = PdfReader(pdf_path)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    except Exception as e:
        print(f"Error leyendo {pdf_path}: {e}")

    return text