import os
import pandas as pd
from datetime import datetime

from utils.pdf_to_text import extract_resume_text
from utils.preprocess import preprocess_text
from utils.ranking import rank_resumes


RESUME_FOLDER = "data/resumes"

JOB_DESCRIPTION_FILE = "data/job_description.txt"

OUTPUT_FOLDER = "outputs"

OUTPUT_FILE = "outputs/ranked_candidates.csv"


# Output
def create_output_folder():

    if not os.path.exists(OUTPUT_FOLDER):

        os.makedirs(OUTPUT_FOLDER)

        print("Output folder created")

    else:

        print("Output folder already exists")


# Job
def load_job_description(file_path):

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            job_description = file.read()

        print("Job description loaded")

        return job_description

    except FileNotFoundError:

        print("Job description file not found")

        return ""


# Resume
def process_resumes():

    resumes = []

    resume_names = []

    total_resumes = 0

    print("\nProcessing resumes...\n")

    for file in os.listdir(RESUME_FOLDER):

        if file.endswith(".pdf"):

            total_resumes += 1

            file_path = os.path.join(
                RESUME_FOLDER,
                file
            )

            print(f"Reading Resume: {file}")

            extracted_text = extract_resume_text(
                file_path
            )

            processed_text = preprocess_text(
                extracted_text
            )

            resumes.append(processed_text)

            resume_names.append(file)

    print("\nTotal Resumes:", total_resumes)

    return resumes, resume_names


# Save
def save_results(result_dataframe):

    result_dataframe.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("\nResults exported")

    print("Output:", OUTPUT_FILE)


# Display
def display_results(result_dataframe):

    print("\n")

    print("=" * 60)

    print("FINAL CANDIDATE RANKING")

    print("=" * 60)

    print(result_dataframe)

    print("=" * 60)


# Main
def main():

    print("\n")

    print("=" * 60)

    print("AI Resume Screening System")

    print("=" * 60)

    print("Execution Time:",
          datetime.now())

    create_output_folder()

    resumes, resume_names = process_resumes()

    job_description = load_job_description(
        JOB_DESCRIPTION_FILE
    )

    processed_job_description = preprocess_text(
        job_description
    )

    ranked_results = rank_resumes(
        resumes,
        resume_names,
        processed_job_description
    )

    result_dataframe = pd.DataFrame(
        ranked_results,
        columns=[
            "Resume Name",
            "Similarity Score"
        ]
    )

    display_results(result_dataframe)

    save_results(result_dataframe)

    print("\nSystem Executed Successfully")


# Driver
if __name__ == "__main__":

    main()
