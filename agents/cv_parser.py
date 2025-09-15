import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")

def parse_cv(cv_text: str) -> dict:
    doc = nlp(cv_text)

    data = {
        "name": None,
        "experience": [],
        "skills": [],
        "education": []
    }

    # extract candidate name
    for ent in doc.ents:
        if ent.label_ == "PERSON" and data["name"] is None:
            data["name"] = ent.text

    # extract education info
    for line in cv_text.splitlines():
        if any(word in line for word in ["BSc", "MSc", "Bachelor", "Master", "Degree", "Diploma"]):
            data["education"].append(line.strip())

    # setup skill matcher
    matcher = Matcher(nlp.vocab)
    tech_skills = ["Python", "JavaScript", "TypeScript", "React", "Node.js",
                   "SQL", "PostgreSQL", "TensorFlow", "PyTorch", "NLP",
                   "AWS", "GCP", "Docker", "Kubernetes", "API", "Prisma"]
    for skill in tech_skills:
        matcher.add(skill, [[{"LOWER": skill.lower()}]])

    matches = matcher(doc)
    for match_id, start, end in matches:
        skill = nlp.vocab.strings[match_id]
        if skill not in data["skills"]:
            data["skills"].append(skill)

    # extract experience section
    capture_exp = False
    for line in cv_text.splitlines():
        if line.lower().startswith("experience"):
            capture_exp = True
            continue
        if line.lower().startswith(("skills", "education")):
            capture_exp = False
        if capture_exp and line.strip():
            data["experience"].append(line.strip())

    return data
