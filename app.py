from flask import Flask, render_template, request
import os
from utils.parser import extract_text
from utils.ranker import rank_resumes

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "uploads"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload():
    job_desc = request.form['job_desc']
    files = request.files.getlist('resumes')

    resumes_text = []
    filenames = []

    for file in files:
        path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(path)

        text = extract_text(path)

        resumes_text.append(text)
        filenames.append(file.filename)

    ranked = rank_resumes(job_desc, resumes_text)

    for i in range(len(ranked)):
        ranked[i]["filename"] = filenames[ranked[i]["resume_id"]]

    # Analytics
    total = len(ranked)
    highest = max(r["score"] for r in ranked) if total else 0
    average = round(sum(r["score"] for r in ranked) / total, 2) if total else 0
    qualified = len([r for r in ranked if r["score"] >= 70])

    return render_template(
        "result.html",
        results=ranked,
        total=total,
        highest=highest,
        average=average,
        qualified=qualified
    )

if __name__ == "__main__":
    app.run(debug=True)