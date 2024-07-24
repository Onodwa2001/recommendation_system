from script import compare_keywords

def compare_words(student_keywords, tutors_keywords):
    scores = []
    for tutor_keywords in tutors_keywords:
        score = compare_keywords(student_keywords, tutor_keywords['keywords'])
        scores.append(score)
    return scores