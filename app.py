from flask import Flask, render_template, request
app = Flask(__name__)

# Sample job listings
jobs = [
    {"title": "Software Developer", "skills": ["Python", "Django"], "education": "Bachelor's", "job_type": "Full-time", "location": "Remote"},
    {"title": "Data Analyst", "skills": ["SQL", "Excel"], "education": "Bachelor's", "job_type": "Part-time", "location": "New York"},
    {"title": "Web Developer", "skills": ["HTML", "CSS", "JavaScript"], "education": "Associate's", "job_type": "Full-time", "location": "San Francisco"}
]

# Job matching function
def match_jobs(user_data):
    matches = []
    for job in jobs:
        skill_match = len(set(user_data["skills"]).intersection(job["skills"])) > 0
        education_match = user_data["education"].lower() in job["education"].lower()
        job_type_match = user_data["job_type"].lower() == job["job_type"].lower()
        location_match = user_data["location"].lower() in job["location"].lower()

        if skill_match and education_match and job_type_match and location_match:
            matches.append(job)
    return matches

# Route to display the form and handle input
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Getting form data
        skills = request.form.get("skills").split(",")
        education = request.form.get("education")
        job_type = request.form.get("job_type")
        location = request.form.get("location")

        # User data dictionary
        user_data = {
            "skills": [skill.strip() for skill in skills],
            "education": education.strip(),
            "job_type": job_type.strip(),
            "location": location.strip()
        }

        # Get matched jobs
        matched_jobs = match_jobs(user_data)

        return render_template("index.html", matched_jobs=matched_jobs)

    return render_template("index.html", matched_jobs=None)

if __name__ == "__main__":
    app.run(debug=True)
