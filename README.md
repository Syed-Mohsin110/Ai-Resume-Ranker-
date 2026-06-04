<img width="1205" height="875" alt="Ai resume ranker dashboard" src="https://github.com/user-attachments/assets/3bc1bc02-92c2-45b3-9ec6-133e142fd342" />
<img width="1168" height="858" alt="wih dada" src="https://github.com/user-attachments/assets/e25da981-9593-4ed2-8e91-00205a06d649" />
<img width="902" height="905" alt="resul" src="https://github.com/user-attachments/assets/259104e0-789d-41a4-9de5-7f0362291f5d" />


Overview

AI Resume Ranker is a web-based application designed to analyze resumes and compare them with a given job description. The system generates a matching score that indicates how well a candidate’s resume aligns with the required job profile. It also highlights missing skills and provides basic suggestions for improvement.

This project demonstrates practical implementation of Natural Language Processing and web development using Flask.


Features

* Upload resumes in PDF format
* Extract and process text from resumes automatically
* Compare resume content with job description
* Generate a similarity or matching score
* Identify missing or relevant skills
* Provide basic improvement feedback
* Simple and responsive web interface

Live Demo
Currently running locally:
http://127.0.0.1:5000

Tech Stack

* Python
* Flask
* HTML
* CSS
* JavaScript
* Scikit-learn
* NLP techniques
* PyPDF2 / pdfplumber for text extraction



Project Structure


ai-resume-ranker/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── uploads/
├── model/
└── README.md
```



Installation and Setup

1. Clone the repository

```
git clone https://github.com/Syed-Mohsin110/Ai-Resume-Ranker-.git
```

2. Navigate to the project directory

```
cd Ai-Resume-Ranker-
```

3. Install required dependencies

```
pip install flask scikit-learn pdfplumber
```

4. Run the application

```
python app.py
```

5. Open in browser

```
http://127.0.0.1:5000
```

---

How It Works

1. The user uploads a resume in PDF format
2. The system extracts text from the resume
3. The job description is processed using NLP techniques
4. A similarity score is calculated between resume and job description
5. The system displays the result along with missing skills and suggestions

---

Future Improvements

* Improve ranking accuracy using advanced NLP models
* Add machine learning-based classification for job roles
* Implement user authentication system
* Allow multiple resume comparison
* Deploy the application on cloud platforms

---

Author

Syed Mohsin
Computer Science Student
Web Developer |AI Engineer

---

License

This project is open for learning and academic purposes.
