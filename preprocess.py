import re
import nltk

from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords

from nltk.stem import WordNetLemmatizer


nltk.download('punkt')

nltk.download('stopwords')

nltk.download('wordnet')


stop_words = set(
    stopwords.words('english')
)

lemmatizer = WordNetLemmatizer()


# Cleaning
def clean_text(text):

    text = text.lower()

    text = re.sub(
        r'[^a-zA-Z0-9 ]',
        ' ',
        text
    )

    text = re.sub(
        r'\s+',
        ' ',
        text
    )

    return text.strip()


# Tokenization
def tokenize_text(text):

    tokens = word_tokenize(text)

    return tokens


# Stopwords
def remove_stopwords(tokens):

    filtered_tokens = []

    for word in tokens:

        if word not in stop_words:

            filtered_tokens.append(word)

    return filtered_tokens


# Lemmatization
def lemmatize_tokens(tokens):

    lemmatized_words = []

    for word in tokens:

        lemma = lemmatizer.lemmatize(word)

        lemmatized_words.append(lemma)

    return lemmatized_words


# Joining
def join_tokens(tokens):

    clean_text = ' '.join(tokens)

    return clean_text


# Preprocessing
def preprocess_text(text):

    cleaned_text = clean_text(text)

    tokens = tokenize_text(
        cleaned_text
    )

    filtered_tokens = remove_stopwords(
        tokens
    )

    lemmatized_tokens = lemmatize_tokens(
        filtered_tokens
    )

    final_text = join_tokens(
        lemmatized_tokens
    )

    return final_text


# Sample
if __name__ == "__main__":

    sample_resume = """

    Python Developer with Machine Learning,
    NLP, Deep Learning and SQL experience.

    """

    processed_text = preprocess_text(
        sample_resume
    )

    print("\nProcessed Resume Text:\n")

    print(processed_text)
