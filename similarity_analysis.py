import pandas as pd


# Analysis
def analyze_similarity_scores(result_dataframe):

    print("\n")

    print("=" * 60)

    print("SIMILARITY ANALYSIS")

    print("=" * 60)

    highest_score = result_dataframe[
        "Match Percentage"
    ].max()

    lowest_score = result_dataframe[
        "Match Percentage"
    ].min()

    average_score = round(
        result_dataframe[
            "Match Percentage"
        ].mean(),
        2
    )

    print(
        f"Highest Match Score: "
        f"{highest_score}%"
    )

    print(
        f"Lowest Match Score: "
        f"{lowest_score}%"
    )

    print(
        f"Average Match Score: "
        f"{average_score}%"
    )

    print("=" * 60)


# Top Candidates
def get_top_candidates(
    result_dataframe,
    top_n=3
):

    print("\n")

    print("=" * 60)

    print(f"TOP {top_n} CANDIDATES")

    print("=" * 60)

    top_candidates = result_dataframe.head(
        top_n
    )

    print(top_candidates)

    print("=" * 60)

    return top_candidates


# Recommendation
def generate_final_recommendation(
    result_dataframe
):

    print("\n")

    print("=" * 60)

    print("FINAL RECOMMENDATION")

    print("=" * 60)

    top_candidate = result_dataframe.iloc[0]

    score = top_candidate[
        "Match Percentage"
    ]

    if score >= 80:

        recommendation = (
            "Highly Recommended"
        )

    elif score >= 60:

        recommendation = (
            "Moderately Recommended"
        )

    else:

        recommendation = (
            "Low Recommendation"
        )

    print(
        f"Selected Candidate: "
        f"{top_candidate['Resume Name']}"
    )

    print(
        f"Final Score: "
        f"{score}%"
    )

    print(
        f"Recommendation Status: "
        f"{recommendation}"
    )

    print("=" * 60)

    return recommendation


# Export
def export_analysis_report(
    result_dataframe,
    output_file
):

    result_dataframe.to_csv(
        output_file,
        index=False
    )

    print("\nAnalysis report exported")

    print(
        f"Saved File: "
        f"{output_file}"
    )


# Sample
if __name__ == "__main__":

    sample_data = {

        "Resume Name": [
            "resume1.pdf",
            "resume2.pdf",
            "resume3.pdf"
        ],

        "Match Percentage": [
            89.5,
            74.2,
            58.8
        ]
    }

    dataframe = pd.DataFrame(
        sample_data
    )

    analyze_similarity_scores(
        dataframe
    )

    get_top_candidates(
        dataframe
    )

    generate_final_recommendation(
        dataframe
    )

    export_analysis_report(
        dataframe,
        "analysis_report.csv"
    )
