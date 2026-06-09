import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Project Root Setup
PROJECT_ROOT = Path(__file__).parent.parent.parent.absolute()
sys.path.insert(0, str(PROJECT_ROOT))

load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from src.tools.pubmed_tool import search_pubmed
from src.tools.search_tool import web_search
from src.tools.calculator_tool import medical_calculator

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3,
    max_tokens=2048,
)

tools = [search_pubmed, web_search, medical_calculator]

def run_research_crew(query: str):
    print(f"\n🔍 Researching: {query}")
    print("=" * 90)

    system_prompt = SystemMessage(content="""You are a professional Healthcare Research Team.
You have two roles:
1. Researcher: Use tools to gather accurate information from PubMed and web.
2. Writer: After gathering information, write a clean, structured, professional report with citations.

First do research, then write the final report.""")

    user_prompt = HumanMessage(content=f"""
    Query: {query}

    Step 1: Do thorough research using available tools.
    Step 2: Write a professional medical report with proper structure and citations.
    """)

    messages = [system_prompt, user_prompt]

    # First call - Research phase
    response = llm.bind_tools(tools).invoke(messages)
    messages.append(response)

    print("✅ Research phase completed. Generating final report...\n")

    # Final call - Write report
    final_response = llm.invoke(messages)
    
    print("="*90)
    print("✅ FINAL MEDICAL REPORT")
    print("="*90)
    print(final_response.content)

    # Save Report
    reports_dir = PROJECT_ROOT / "reports"
    reports_dir.mkdir(exist_ok=True)
    safe_name = "".join(c if c.isalnum() else "_" for c in query[:50])
    report_path = reports_dir / f"report_{safe_name}.md"
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(final_response.content)
    
    print(f"\n📄 Report saved: {report_path}")
    return final_response.content


if __name__ == "__main__":
    print("🚀 HEALTHCARE RESEARCH SYSTEM Started (LangGraph Style)")
    print("=" * 90)

    test_queries = [
        "Latest treatments for Type 2 Diabetes in 2024-2025",
        "Pakistan out-of-pocket health expenditure percentage latest data"
    ]

    for q in test_queries:
        run_research_crew(q)
        print("\n" + "="*100 + "\n")