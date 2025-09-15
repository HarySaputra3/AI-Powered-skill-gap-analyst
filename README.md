# 🚀 AI-Powered Skill Gap Analyst

## 📌 Objective

This project builds a **multi-agent** system to assist recruiters in analyzing candidate CVs.  
The system will:

- Extract explicit & implicit skills from a CV.
- Compare the candidate's skills with current job market demands.
- Generate a **Skill Gap Analysis** report in Markdown format.

---

## 🔄 Workflow

1. **CV Parser Agent** → Reads a `.txt` CV file and converts it into structured data.
2. **Skill Analyst Agent** → Identifies explicit skills & infers implicit skills.
3. **Market Intelligence Agent** → Fetches in-demand skills from the job market (via Remotive API, with fallback lists if API fails).
4. **Recommender Agent** → Compares the candidate's skills with market demands and creates `report.md`.

---

## 📂 Project Structure

```
AI-Powered-skill-gap-analyst/
├── agents/
│   ├── cv_parser.py
│   ├── market_intel.py
│   ├── recommender.py
│   └── skill_analyst.py
├── main.py
├── README.md
├── requirements.txt
└── sample_cv.txt
```

---

## ⚙️ Installation

### 1. Clone the Repository

```
git clone https://github.com/HarySaputra3/AI-Powered-skill-gap-analyst.git
```

```
cd ai-skill-gap
```

### 2. (Optional) Create a Virtual Environment

# create a virtual environment

```
python -m venv venv
```

# activate it windows

```
venv\Scripts\activate
```

# macos/linux

```
source
venv/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

**requirements.txt should include:**

```
requests
pandas
spacy
langgraph
langchain
langchain-core
torch
sentence-transformers
beautifulsoup4
```

---

## ▶️ Usage

Run the application from the project root:

```
python main.py
```

You will be prompted to enter a job role:

Enter target job role:
`cyber security`

### Input

- A CV file in `.txt` format (example: `sample_cv.txt`).

**Example `sample_cv.txt`:**

```
Hary Saputra
Software Engineer

Experience:
- Built a web application using React, Next.js, and PostgreSQL.
- Developed an API using Hapi.js and Prisma.
- Integrated Midtrans payment gateway.

Skills:
- JavaScript, TypeScript, React, Node.js
- SQL, PostgreSQL
- API Development

Education:
- BSc in Information Systems
```

### Output

- Console will show parsing & analysis results.
- A new file `report_<role>.md` will be created with the analysis.

---

## 📄 Example Output (report.md)

### 1. Web Developer

```markdown
# Skill Gap Analysis (web developer)

## Strengths

JavaScript, React, Node.js, SQL

## Gaps

Cloud Deployment, Python, Cyber Security, SEO, Google Analytics, Excel, Testing Frameworks, Content Marketing

## Recommended Upskilling Path

- Focus on learning: Cloud Deployment, Python, Cyber Security, SEO, Google Analytics, Excel, Testing Frameworks, Content Marketing.

```

### 2. Cyber Security

```markdown
# Skill Gap Analysis (Cyber Security)

## Observation

Your CV mainly highlights **JavaScript, API, React, Node.js, PostgreSQL, SQL, Prisma, TypeScript**,  
which does **not align well** with the common requirements for **Cyber Security**.

## Recommended Next Step

- If you want to transition into Cyber Security, start developing role-specific skills such as: Cloud Deployment, Python, Cyber Security, Excel, Testing Frameworks, SQL.
- Alternatively, target roles that better fit your current background (e.g., Software Engineer, Web Developer).
```

### 3. Digital Marketing

```markdown
# Skill Gap Analysis (digital marketing)

## Observation

Your CV mainly highlights **JavaScript, API, React, Node.js, PostgreSQL, SQL, Prisma, TypeScript**,  
which does **not align well** with the common requirements for **digital marketing**.

## Recommended Next Step

- If you want to transition into digital marketing, start developing role-specific skills such as: Cloud Deployment, SEO, Data Visualization, Cyber Security, React, Google Analytics, Excel, Testing Frameworks, Social Media Marketing, Content Marketing, SQL, Email Marketing, Statistics.
- Alternatively, target roles that better fit your current background (e.g., Software Engineer, Web Developer).

```

---

## 🧩 Code Overview

**cv_parser.py**

- Uses spaCy NLP to parse CV text.
- Extracts key information: name, work experience, skills, education.

**skill_analyst.py**

- Identifies explicit skills (directly listed).
- Infers implicit skills (from experience section).
- Uses embeddings (Sentence Transformers) to enhance skill detection.

**market_intel.py**

- Uses Remotive API to fetch job postings by role and extracts skills from descriptions.
- If API fails or returns insufficient data, falls back to role-based default skill lists.

**recommender.py**

- Compares candidate skills vs market demands.
- Applies a relevancy threshold and transferable-skill checks.
- Generates `report_<role>.md` with strengths, gaps, and recommended upskilling paths.

**main.py**

- Orchestrates the multi-agent workflow using LangGraph as a state-machine.
- Accepts dynamic role input from user in a loop (no need to rerun script).
- Saves reports for each role separately.

---

## 📊 Workflow Diagram

```
flowchart TD
    A[CV .txt] --> B[CV Parser Agent]
    B -->|Structured Data| C[Skill Analyst Agent]
    C --> E[Recommender Agent]
    D[Market Intelligence Agent] --> E
    E --> F[Skill Gap Report .md]
```

---

## 🧪 Evaluation Criteria

- **Architectural Design** → The multi-agent workflow is clear and logical.
- **Code Quality** → The code is modular, clean, and easy to read.
- **Agent Logic** → Each agent performs its function correctly.
- **Output Quality** → The generated report is clear and actionable.
- **Completeness** → The project includes README, source code, sample CV, and example outputs.

---

⚠️ **Limitations**

- CV parsing currently keyword-based; can be improved with advanced NLP/LLM parsing.
- API results depend on external service availability and may vary.
