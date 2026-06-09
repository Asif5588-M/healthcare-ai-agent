import streamlit as st
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.absolute()
sys.path.insert(0, str(PROJECT_ROOT))

from src.agents.orchestrator import run_research_crew

st.set_page_config(
    page_title="Healthcare AI Research Agent",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Healthcare AI Research Agent")
st.caption("AI-powered medical literature research | PubMed + LLM | By Asif Nawaz, PMAS Arid Agriculture University")
st.divider()

# ── Sidebar ────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ System Info")
    st.metric("LLM", "Llama 3.3-70B")
    st.metric("Data Source", "PubMed + Web")
    st.metric("Agent Type", "Research + Writer")
    st.divider()

    st.header("💡 Example Queries")
    examples = [
        "Latest treatments for Type 2 diabetes 2024",
        "Pakistan out-of-pocket health expenditure",
        "Immunotherapy effectiveness for cancer 2024",
        "Long-term effects of COVID-19",
        "Hypertension management guidelines 2024",
        "Mental health depression treatment outcomes",
        "Antibiotic resistance latest research",
    ]
    for ex in examples:
        if st.button(ex, use_container_width=True, key=ex):
            st.session_state["query"] = ex

    st.divider()
    st.markdown("""
    **How it works:**
    1. Enter medical question
    2. Agent searches PubMed
    3. LLM generates report
    4. Download as Markdown
    """)

# ── Main ───────────────────────────────────────────────────
col1, col2 = st.columns([3, 1])

with col1:
    query = st.text_area(
        "Enter your medical research question:",
        value=st.session_state.get("query", ""),
        height=100,
        placeholder="e.g. What are the latest treatments for Type 2 diabetes in 2024?"
    )

with col2:
    st.write("")
    st.write("")
    search = st.button(
        "🔍 Research & Generate Report",
        type="primary",
        use_container_width=True
    )

# ── Results ────────────────────────────────────────────────
if search and query.strip():
    with st.spinner("🔬 Searching PubMed and generating report... (30-60 sec)"):
        try:
            report = run_research_crew(query)

            st.divider()
            st.subheader("📋 Medical Research Report")

            st.markdown(report)

            st.divider()

            # Download button
            st.download_button(
                label="📥 Download Report (Markdown)",
                data=report,
                file_name=f"medical_report_{query[:30].replace(' ', '_')}.md",
                mime="text/markdown",
                use_container_width=True
            )

        except Exception as e:
            st.error(f"Error: {e}")

elif search and not query.strip():
    st.warning("Please enter a research question!")

st.divider()
st.caption(
    "Data: PubMed + Web Search · "
    "LLM: Llama 3.3-70B via Groq · "
    "Asif Nawaz | PMAS Arid Agriculture University | MPhil Economics"
)