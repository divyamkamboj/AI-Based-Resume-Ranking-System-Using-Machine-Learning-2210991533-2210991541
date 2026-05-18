import os
import PyPDF2


# Extraction
def extract_resume_text(file_path):

    extracted_text = ""

    try:

        with open(file_path, "rb") as pdf_file:

            pdf_reader = PyPDF2.PdfReader(
                pdf_file
            )

            total_pages = len(
                pdf_reader.pages
            )

            print(
                f"\nReading PDF: "
                f"{os.path.basename(file_path)}"
            )

            print(
                f"Total Pages: "
                f"{total_pages}"
            )

            page_number = 1

            for page in pdf_reader.pages:

                print(
                    f"Processing Page: "
                    f"{page_number}"
                )

                page_text = page.extract_text()

                if page_text:

                    extracted_text += page_text

                page_number += 1

        print(
            "Resume text extracted successfully"
        )

        return extracted_text

    except FileNotFoundError:

        print("PDF file not found")

        return ""

    except Exception as error:

        print(
            f"Error while reading PDF: "
            f"{error}"
        )

        return ""


# Information
def get_resume_information(file_path):

    try:

        with open(file_path, "rb") as pdf_file:

            pdf_reader = PyPDF2.PdfReader(
                pdf_file
            )

            information = {

                "File Name":
                os.path.basename(file_path),

                "Total Pages":
                len(pdf_reader.pages)
            }

            return information

    except Exception as error:

        print(
            f"Unable to fetch information: "
            f"{error}"
        )

        return {}


# Sample
if __name__ == "__main__":

    sample_file = "sample_resume.pdf"

    resume_text = extract_resume_text(
        sample_file
    )

    print("\nExtracted Resume Text:\n")

    print(resume_text[:1000])

    print("\nResume Information:\n")

    print(
        get_resume_information(
            sample_file
        )
    )
