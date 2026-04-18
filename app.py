from flask import Flask, render_template, request
import os
from utils.parser import extract_text
from utils.analyzer import calculate_score
from utils.skills import extract_skills, find_missing_skills
from utils.suggestions import generate_suggestions
from utils.database import Resume, session

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create uploads folder if not exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['resume']
    jd = request.form['job_description']

    if file.filename == '':
        return "No file selected"

    # Save file
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Extract text
    resume_text = extract_text(filepath)
    if not resume_text:
        return "Could not read resume properly. Try another PDF."

    # Analysis
    score = calculate_score(resume_text, jd)
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd)
    missing = find_missing_skills(resume_skills, jd_skills)
    suggestions = generate_suggestions(score, missing, resume_text)

    # Save to database
    resume_record = Resume(
        filename=file.filename,
        score=int(score),
        skills=", ".join(resume_skills),
        missing_skills=", ".join(missing),
        suggestions=", ".join(suggestions)
    )
    session.add(resume_record)
    session.commit()

    # Render result
    return render_template(
        'result.html',
        score=score,
        skills=resume_skills,
        missing=missing,
        suggestions=suggestions
    )


@app.route('/history')
def history():
    # Get all past uploads from database
    resumes = session.query(Resume).order_by(Resume.uploaded_at.desc()).all()
    return render_template("history.html", resumes=resumes)


if __name__ == '__main__':
    app.run(debug=True)