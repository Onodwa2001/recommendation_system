import spacy

nlp = spacy.load("en_core_web_md")

def compare_keywords(array1, array2):
    # Convert the lists of keywords to spaCy documents
    doc1 = nlp(" ".join(array1))
    doc2 = nlp(" ".join(array2))

    # Calculate the similarity score between the two documents
    similarity_score = doc1.similarity(doc2)

    return similarity_score

