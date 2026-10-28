
from jobpilot_tools import extract_skills, match_job
from sample_profile import professional_profile


def analyze_job(job_title, job_description):

    if not isinstance(job_title, str) or not job_title.strip():
        raise ValueError("Please enter a valid job title.")

    if not isinstance(job_description, str) or not job_description.strip():
        raise ValueError("Please enter a valid job description.")

    required_skills = extract_skills(job_description)

    if not required_skills:
        return {
            "Job Title": job_title,
            "Message": "No supported technical skills detected."
        }

    candidate_skills = professional_profile["technical_skills"]

    result = match_job(candidate_skills, required_skills)

    return {
        "Candidate": professional_profile["name"],
        "Job Title": job_title,
        "Required Skills": required_skills,
        "Matched Skills": result["matched_skills"],
        "Missing Skills": result["missing_skills"],
        "Keyword Match (%)": result["match_percentage"]
    }


if __name__ == "__main__":

    job_title = "Python Backend Developer"

    job_description = """
    We need a developer with Python, SQL,
    Django, FastAPI, Docker, and AWS skills.
    """

    analysis = analyze_job(job_title, job_description)

    print("=" * 50)
    print("JOBPILOT AI - DEMO APPLICATION")
    print("=" * 50)

    for key, value in analysis.items():
        print(f"{key}: {value}")
