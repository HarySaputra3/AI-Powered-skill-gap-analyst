try:
    from sentence_transformers import SentenceTransformer, util
    import torch
    USE_TRANSFORMER = True
except ImportError:
    USE_TRANSFORMER = False

import re

# dgeneral skills (library)
SKILL_LIBRARY = [
    "Frontend Development", "Backend Development", "Database Design",
    "REST API Design", "Cyber Security", "Cloud Deployment",
    "Data Analysis", "Machine Learning", "DevOps", "Testing Frameworks",
    "FinTech Integration", "Collaboration", "Leadership", "Communication",
    "Problem Solving", "Teamwork"
]

# if sentence-transformers available
if USE_TRANSFORMER:
    model = SentenceTransformer("all-MiniLM-L6-v2")

def analyze_skills(parsed_cv: dict) -> dict:
    explicit = parsed_cv.get("skills", [])
    implicit = []

    exp_texts = parsed_cv.get("experience", [])
    if not exp_texts:
        return {"explicit": explicit, "implicit": []}

    if USE_TRANSFORMER:
        exp_embeddings = model.encode(exp_texts, convert_to_tensor=True)
        skill_embeddings = model.encode(SKILL_LIBRARY, convert_to_tensor=True)
        cos_scores = util.cos_sim(exp_embeddings, skill_embeddings)

        for i, exp in enumerate(exp_texts):
            for j, skill in enumerate(SKILL_LIBRARY):
                if cos_scores[i][j] > 0.5:  # threshold relevansi
                    implicit.append(skill)

    else:
        # fallback rule-based
        for exp in exp_texts:
            exp_lower = exp.lower()
            if "react" in exp_lower or "next.js" in exp_lower:
                implicit.append("Frontend Development")
            if "api" in exp_lower or "prisma" in exp_lower:
                implicit.append("REST API Design")
            if "payment" in exp_lower or "midtrans" in exp_lower or "stripe" in exp_lower:
                implicit.append("FinTech Integration")
            if "postgresql" in exp_lower or "database" in exp_lower:
                implicit.append("Database Design")
            if "team" in exp_lower or "collaboration" in exp_lower:
                implicit.append("Collaboration")

    return {
        "explicit": explicit,
        "implicit": list(set(implicit))
    }
