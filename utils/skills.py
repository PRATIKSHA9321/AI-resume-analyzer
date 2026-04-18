import spacy
nlp = spacy.load("en_core_web_sm")

SKILL_DB = ["python", "java", "c++", "machine learning", "sql",
            "html", "css", "javascript", "flask", "django"]

def extract_skills(text):
    doc = nlp(text.lower() if text else "")
    found = []
    for token in doc:
        if token.text in SKILL_DB:
            found.append(token.text)
    return list(set(found))

def find_missing_skills(resume_skills, jd_skills):
    return list(set(jd_skills) - set(resume_skills))