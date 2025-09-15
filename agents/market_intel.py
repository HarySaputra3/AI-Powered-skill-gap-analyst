import requests
from bs4 import BeautifulSoup

def fetch_market_demands(role: str) -> list:
    url = "https://remotive.com/api/remote-jobs"
    querystring = {"search": role}

    try:
        response = requests.get(url, params=querystring, timeout=30)
        response.raise_for_status()
        data = response.json()

        descriptions = []
        for job in data.get("jobs", []):
            desc = job.get("description", "")
            # cleaning html
            clean_desc = BeautifulSoup(desc, "html.parser").get_text(separator=" ")
            descriptions.append(clean_desc)

        skills = []
        for desc in descriptions:
            d = desc.lower()
            # web dev
            if "javascript" in d: skills.append("JavaScript")
            if "react" in d: skills.append("React")
            if "node.js" in d: skills.append("Node.js")
            if "aws" in d or "cloud" in d: skills.append("Cloud Deployment")
            if "jest" in d or "mocha" in d or "testing" in d: skills.append("Testing Frameworks")

            # cyber security
            if "security" in d or "penetration" in d: skills.append("Cyber Security")
            if "network security" in d: skills.append("Network Security")
            if "owasp" in d: skills.append("OWASP Top 10")

            # digital marketing
            if "seo" in d: skills.append("SEO")
            if "google analytics" in d: skills.append("Google Analytics")
            if "content marketing" in d: skills.append("Content Marketing")
            if "social media" in d: skills.append("Social Media Marketing")
            if "email marketing" in d: skills.append("Email Marketing")

            # data analyst
            if "excel" in d: skills.append("Excel")
            if "sql" in d: skills.append("SQL")
            if "tableau" in d or "power bi" in d: skills.append("Data Visualization")
            if "python" in d: skills.append("Python")
            if "statistics" in d: skills.append("Statistics")

        return list(set(skills)) if skills else []

    except Exception as e:
        print("api request failed, using fallback:", e)
        return ["JavaScript", "React", "Node.js", "SQL", "Cloud Deployment", "Testing Frameworks"]
