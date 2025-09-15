def generate_report(cv_skills: dict, market_skills: list, role: str = "Web Developer", relevancy_threshold: float = 0.3) -> str:
    explicit = set(cv_skills.get("explicit", []))
    implicit = set(cv_skills.get("implicit", []))
    candidate_skills = explicit.union(implicit)

    strengths = [s for s in candidate_skills if s in market_skills]
    gaps = [s for s in market_skills if s not in candidate_skills]

    # relevan check
    relevancy_ratio = len(strengths) / len(market_skills) if market_skills else 0

    # CASE 1: CV not relevan with role
    if relevancy_ratio < relevancy_threshold:
        return f"""# Skill Gap Analysis ({role})

## Observation
Your CV mainly highlights **{", ".join(explicit) if explicit else "general experience"}**,  
which does **not align well** with the common requirements for **{role}**.

## Recommended Next Step
- If you want to transition into {role}, start developing role-specific skills such as: {", ".join(market_skills) if market_skills else "role-specific skills"}.
- Alternatively, target roles that better fit your current background (e.g., Software Engineer, Web Developer).
"""

    # CASE 2: cv relevan show Strengths & Gaps
    return f"""# Skill Gap Analysis ({role})

## Strengths
{", ".join(strengths) if strengths else "None"}

## Gaps
{", ".join(gaps) if gaps else "None"}

## Recommended Upskilling Path
- Focus on learning: {", ".join(gaps) if gaps else "Already aligned with market needs"}.
"""
