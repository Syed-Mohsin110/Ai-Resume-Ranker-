from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

SKILLS = [
    "python", "javascript", "react", "sql", "flask",
    "html", "css", "machine learning", "communication",
    "leadership", "java", "c++"
]

def extract_skills(text):
    found = []
    lower_text = text.lower()

    for skill in SKILLS:
        if skill in lower_text:
            found.append(skill.title())

    return found

def rank_resumes(job_description, resumes):
    texts = [job_description] + resumes

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(texts)

    job_vector = vectors[0]
    resume_vectors = vectors[1:]

    scores = cosine_similarity(job_vector, resume_vectors)[0]

    results = []

    for i, score in enumerate(scores):
        results.append({
            "resume_id": i,
            "score": round(score * 100, 2),
            "skills": extract_skills(resumes[i])
        })

    return sorted(results, key=lambda x: x["score"], reverse=True)