
import re


TECHNICAL_SKILLS = ['Python', 'Java', 'SQL', 'HTML', 'CSS', 'JavaScript', 'Django', 'Flask', 'Networking', 'Windows', 'Linux', 'Troubleshooting', 'Cybersecurity', 'AWS', 'Azure', 'Excel', 'Power BI', 'Data Analysis', 'Machine Learning', 'API Testing', 'Selenium', 'Playwright', 'Git', 'Docker', 'Kubernetes', 'FastAPI', 'DBMS']


SKILL_ALIASES = {
    "Troubleshooting": [
        "troubleshoot",
        "troubleshooting",
        "troubleshoots"
    ],
    "Networking": [
        "network",
        "networks",
        "networking"
    ],
    "Python": [
        "python",
        "python programming"
    ],
    "SQL": [
        "sql",
        "structured query language"
    ]
}


def extract_skills(description, skills_database=None):

    if skills_database is None:
        skills_database = TECHNICAL_SKILLS

    found_skills = []

    for skill in skills_database:

        aliases = SKILL_ALIASES.get(skill, [skill])

        for alias in aliases:

            pattern = (
                r"(?<!\w)"
                + re.escape(alias)
                + r"(?!\w)"
            )

            if re.search(
                pattern,
                description,
                re.IGNORECASE
            ):
                found_skills.append(skill)
                break

    return found_skills


def match_job(candidate_skills, required_skills):

    candidate_set = {
        skill.lower().strip()
        for skill in candidate_skills
    }

    required_set = {
        skill.lower().strip()
        for skill in required_skills
    }

    matched_skills = candidate_set.intersection(
        required_set
    )

    missing_skills = required_set.difference(
        candidate_set
    )

    match_percentage = (
        len(matched_skills) / len(required_set) * 100
        if required_set else 0
    )

    return {
        "match_percentage": round(match_percentage, 2),
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills)
    }
