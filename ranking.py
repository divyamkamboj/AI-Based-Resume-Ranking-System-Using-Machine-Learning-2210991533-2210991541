
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def rank_resumes(
    resumes,
    resume_names,
    job_description
):

    documents = resumes + [job_description]

    tfidf = TfidfVectorizer()

    tfidf_matrix = tfidf.fit_transform(documents)

    similarity_scores = cosine_similarity(
        tfidf_matrix[-1],
        tfidf_matrix[:-1]
    )[0]

    ranking = list(
        zip(resume_names, similarity_scores)
    )

    ranking = sorted(
        ranking,
        key=lambda x: x[1],
        reverse=True
    )

    formatted_results = []

    rank_position = 1

    for resume, score in ranking:

        formatted_results.append(
            (
                resume,
                round(score, 2)
            )
        )

        print(
            f"Rank {rank_position} | "
            f"Resume: {resume} | "
            f"Score: {round(score, 2)}"
        )

        rank_position += 1

    return formatted_results
