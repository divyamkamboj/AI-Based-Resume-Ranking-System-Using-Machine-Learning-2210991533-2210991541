
import os
import pandas as pd

from utils.pdf_to_text import extract_resume_text
from utils.preprocess import preprocess_text
from utils.ranking import rank_resumes


# =====================================================
# AI Resume Screening and Candidate Ranking System
# =====================================================

RESUME_FOLDER = "data/resumes"
JOB_DESCRIPTION_FILE = "data/job_description.txt"
OUTPUT_FOLDER = "outputs"
OUTPUT_FILE = "outputs/ranked_candidates.csv"


def load_job_description(file_path):

    try:

        with open(file_path, "r", encoding="utf-8") as file:

            job_description = file.read()

        return job_description

    except FileNotFoundError:

        print("Error: Job description file not found")

        return ""


def create_output_directory():

    if not os.path.exists(OUTPUT_FOLDER):

        os.makedirs(OUTPUT_FOLDER)


def load_resumes():

    resumes = []

    resume_names = []

    print("\nLoading resumes from folder...")

    for file in os.listdir(RESUME_FOLDER):

        if file.endswith(".pdf"):

            resume_path = os.path.join(
                RESUME_FOLDER,
                file
            )

            print(f"Processing Resume: {file}")

            extracted_text = extract_resume_text(
                resume_path
            )

            processed_text = preprocess_text(
                extracted_text
            )

            resumes.append(processed_text)

            resume_names.append(file)

    print("\nTotal Resumes Processed:", len(resumes))

    return resumes, resume_names


def save_results(result_df):

    result_df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("\nResults saved successfully!")

    print(f"Output File: {OUTPUT_FILE}")


if __name__ == "__main__":

    print("=" * 60)

    print("AI Resume Screening and Ranking System")

    print("=" * 60)

    create_output_directory()

    resumes, resume_names = load_resumes()

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

    result_df = pd.DataFrame(
        ranked_results,
        columns=[
            "Resume Name",
            "Similarity Score"
        ]
    )

    print("\nFinal Candidate Ranking")

    print("-" * 60)

    print(result_df)

    print("-" * 60)

    save_results(result_df)

    print("\nSystem Execution Completed Successfully")
