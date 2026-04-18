# utils/suggestions.py

def generate_suggestions(score, missing_skills, resume_text=""):
    """
    Generates suggestions based on score, missing skills, and resume text.
    """
    suggestions = []

    # Score-based suggestions
    if score < 50:
        suggestions.append("Your resume is not well aligned with the job description.")
    elif score < 75:
        suggestions.append("Your resume is moderately aligned. Improve keyword usage.")
    else:
        suggestions.append("Good match! Fine-tune for better impact.")

    # Missing skills
    if missing_skills:
        suggestions.append("Add these important skills: " + ", ".join(missing_skills))

    # Resume content analysis
    if "project" not in resume_text.lower():
        suggestions.append("Add projects to showcase practical experience.")

    if "experience" not in resume_text.lower():
        suggestions.append("Include work experience or internships.")

    if "%" not in resume_text:
        suggestions.append("Add measurable achievements (e.g., improved performance by 20%).")

    return suggestions