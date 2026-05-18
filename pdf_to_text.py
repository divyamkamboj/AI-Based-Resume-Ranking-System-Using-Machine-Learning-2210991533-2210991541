
import PyPDF2


def extract_resume_text(file_path):

    text = ""

    with open(file_path, 'rb') as pdf_file:

        reader = PyPDF2.PdfReader(pdf_file)

        for page in reader.pages:

            extracted = page.extract_text()

            if extracted:

                text += extracted

    return text
