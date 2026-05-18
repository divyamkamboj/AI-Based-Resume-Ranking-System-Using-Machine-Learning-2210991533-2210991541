from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import pandas as pd


# Ranking
def rank_resumes(
    resumes,
    resume_names,
    job_description
):

    documents = resumes + [job_description]

    tfidf_vectorizer = TfidfVectorizer()

    tfidf_matrix = tfidf_vectorizer.fit_transform(
        documents
    )

    job_description_vector = tfidf_matrix[-1]

    resume_vectors = tfidf_matrix[:-1]

    similarity_scores = cosine_similarity(
        job_description_vector,
        resume_vectors
    )[0]

    ranked_results = list(
        zip(
            resume_names,
            similarity_scores
        )
    )

    ranked_results = sorted(
        ranked_results,
        key=lambda x: x[1],
        reverse=True
    )

    final_results = []

    rank_position = 1

    print("\n")

    print("=" * 60)

    print("CANDIDATE RANKING RESULTS")

    print("=" * 60)

    for resume, score in ranked_results:

        percentage_score = round(
            score * 100,
            2
        )

        if percentage_score >= 80:

            recommendation = "Strong Match"

        elif percentage_score >= 60:

            recommendation = "Moderate Match"

        else:

            recommendation = "Low Match"

        print(
            f"Rank {rank_position}"
        )

        print(
            f"Resume Name: {resume}"
        )

        print(
            f"Similarity Score: {round(score, 2)}"
        )

        print(
            f"Match Percentage: {percentage_score}%"
        )

        print(
            f"Recommendation: {recommendation}"
        )

        print("-" * 60)

        result_data = {

            "Rank": rank_position,

            "Resume Name": resume,

            "Similarity Score": round(score, 2),

            "Match Percentage": percentage_score,

            "Recommendation": recommendation
        }

        final_results.append(result_data)

        rank_position += 1

    return pd.DataFrame(final_results)


# Statistics
def display_statistics(result_dataframe):

    print("\n")

    print("=" * 60)

    print("RANKING STATISTICS")

    print("=" * 60)

    total_candidates = len(
        result_dataframe
    )

    average_score = round(
        result_dataframe[
            "Match Percentage"
        ].mean(),
        2
    )

    top_candidate = result_dataframe.iloc[0]

    print(
        f"Total Candidates: {total_candidates}"
    )

    print(
        f"Average Match Score: {average_score}%"
    )

    print(
        f"Top Candidate: "
        f"{top_candidate['Resume Name']}"
    )

    print(
        f"Highest Score: "
        f"{top_candidate['Match Percentage']}%"
    )

    print("=" * 60)
