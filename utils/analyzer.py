from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_score(resume, jd):
    cv = CountVectorizer()
    matrix = cv.fit_transform([resume, jd])
    similarity = cosine_similarity(matrix)[0][1]
    return round(similarity * 100, 2)