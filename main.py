from typing import TypedDict, List, Dict, Any
from langgraph.graph import StateGraph, END
from agents.cv_parser import parse_cv
from agents.skill_analyst import analyze_skills
from agents.market_intel import fetch_market_demands
from agents.recommender import generate_report

class AgentState(TypedDict, total=False):
    role: str
    parsed_cv: Dict[str, Any]
    skills: Dict[str, List[str]]
    market: List[str]

# define nodes
def cv_parser_node(state: AgentState):
    with open("sample_cv.txt", "r", encoding="utf-8") as f:
        cv_text = f.read()
    state["parsed_cv"] = parse_cv(cv_text)
    print("[cv_parser] parsed_cv set:", state["parsed_cv"])
    return state

def skill_analyst_node(state: AgentState):
    if not state.get("parsed_cv"):
        raise ValueError("parsed_cv is missing in state")
    state["skills"] = analyze_skills(state["parsed_cv"])
    print("[skill_analyst] skills analyzed:", state["skills"])
    return state

def market_intel_node(state: AgentState):
    role = state.get("role", "Web Developer")
    state["market"] = fetch_market_demands(role)
    print(f"[market_intel] market demands for {role}:", state["market"])
    return state

def recommender_node(state: AgentState):
    role = state.get("role", "Web Developer")
    report = generate_report(state["skills"], state["market"], role)
    filename = f"report_{role.replace(' ', '_').lower()}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"[recommender] report generated: {filename}")
    return state

# build graph
workflow = StateGraph(AgentState)
workflow.add_node("cv_parser", cv_parser_node)
workflow.add_node("skill_analyst", skill_analyst_node)
workflow.add_node("market_intel", market_intel_node)
workflow.add_node("recommender", recommender_node)

workflow.set_entry_point("cv_parser")
workflow.add_edge("cv_parser", "skill_analyst")
workflow.add_edge("skill_analyst", "market_intel")
workflow.add_edge("market_intel", "recommender")
workflow.add_edge("recommender", END)

app = workflow.compile()

if __name__ == "__main__":
    while True:
        role = input("\nEnter target job role (or type 'exit' to quit): ")
        if role.lower() in ["exit", "quit", "q"]:
            print("Goodbye!")
            break
        final_state = app.invoke({"role": role})
        print("Workflow completed.\n")
