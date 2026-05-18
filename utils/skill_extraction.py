import re


SKILLS_DATABASE = [

    "python",
    "java",
    "c++",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "nlp",
    "data science",
    "sql",
    "mysql",
    "mongodb",
    "html",
    "css",
    "javascript",
    "react",
    "flask",
    "django",
    "pandas",
    "numpy",
    "scikit learn",
    "tensorflow",
    "communication",
    "leadership",
    "problem solving"
]


# Extraction
def extract_skills(text):

    detected_skills = []

    clean_text = text.lower()

    clean_text = re.sub(
        r'[^a-zA-Z0-9 ]',
        ' ',
        clean_text
    )

    for skill in SKILLS_DATABASE:

        if skill in clean_text:

            detected_skills.append(skill)

    return list(set(detected_skills))


# Matching
def match_job_skills(
    resume_skills,
    job_skills
):

    matched_skills = []

    missing_skills = []

    for skill in job_skills:

        if skill in resume_skills:

            matched_skills.append(skill)

        else:

            missing_skills.append(skill)

    return matched_skills, missing_skills


# Percentage
def calculate_skill_match_percentage(
    matched_skills,
    job_skills
):

    if len(job_skills) == 0:

        return 0

    percentage = (
        len(matched_skills)
        /
        len(job_skills)
    ) * 100

    return round(percentage, 2)


# Display
def display_skills(
    resume_skills,
    matched_skills,
    missing_skills
):

    print("\n")

    print("=" * 60)

    print("SKILL ANALYSIS")

    print("=" * 60)

    print(
        f"Detected Skills: "
        f"{', '.join(resume_skills)}"
    )

    print("\n")

    print(
        f"Matched Skills: "
        f"{', '.join(matched_skills)}"
    )

    print("\n")

    print(
        f"Missing Skills: "
        f"{', '.join(missing_skills)}"
    )

    print("=" * 60)


# Sample
if __name__ == "__main__":

    sample_resume = """

    Python developer with Machine Learning,
    NLP, SQL, Flask and React experience.

    """

    sample_job_description = """

    Looking for Python, NLP,
    Machine Learning and Django skills.

    """

    resume_skills = extract_skills(
        sample_resume
    )

    job_skills = extract_skills(
        sample_job_description
    )

    matched_skills, missing_skills = match_job_skills(
        resume_skills,
        job_skills
    )

    percentage = calculate_skill_match_percentage(
        matched_skills,
        job_skills
    )

    display_skills(
        resume_skills,
        matched_skills,
        missing_skills
    )

    print(
        f"\nSkill Match Percentage: "
        f"{percentage}%"
    )
