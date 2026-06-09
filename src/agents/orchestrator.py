import os
import sys
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).parent.parent.parent.absolute()
sys.path.insert(0, str(PROJECT_ROOT))

load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from src.tools.pubmed_tool import search_pubmed
from src.tools.search_tool import web_search


def get_llm():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found")
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.3,
        max_tokens=3000,
        api_key=api_key,
    )


def run_research_crew(query: str) -> str:
    llm = get_llm()

    print(f"\n🔍 Researching: {query}")
    print("=" * 90)

    # Step 1 — PubMed search manually
    print("📚 Searching PubMed...")
    pubmed_results = search_pubmed.invoke({"query": query})

    # Step 2 — Web search manually
    print("🌐 Web search...")
    try:
        web_results = web_search.invoke({"query": query})
    except Exception:
        web_results = "Web search unavailable."

    # Step 3 — LLM generates report from gathered data
    print("✍️ Generating report...")

    system = SystemMessage(content="""You are a professional medical research writer.
Write comprehensive, well-structured medical research reports with proper citations.
Always include: Introduction, Key Findings, Treatment Options, Conclusion, References.
Use academic medical writing style.""")

    user = HumanMessage(content=f"""
Research Query: {query}

PubMed Research Papers Found:
{pubmed_results}

Additional Web Information:
{web_results}

Based on the above research data, write a comprehensive, professional medical research report.
Include proper citations, structured headings, and evidence-based recommendations.
""")

    response = llm.invoke([system, user])

    report = response.content

    print("\n" + "="*90)
    print("✅ FINAL MEDICAL REPORT")
    print("="*90)
    print(report)

    # Save report
    reports_dir = PROJECT_ROOT / "reports"
    reports_dir.mkdir(exist_ok=True)
    safe_name = "".join(c if c.isalnum() else "_" for c in query[:50])
    report_path = reports_dir / f"report_{safe_name}.md"

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"\n📄 Report saved: {report_path}")
    return report


if __name__ == "__main__":
    print("🚀 HEALTHCARE RESEARCH SYSTEM")
    print("=" * 90)

    test_queries = [
        "Latest treatments for Type 2 Diabetes in 2024",
    ]

    for q in test_queries:
        run_research_crew(q)
        print("\n" + "="*100 + "\n")