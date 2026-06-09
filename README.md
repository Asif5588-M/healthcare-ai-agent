# 🏥 Healthcare AI Research Agent

[![Live App](https://img.shields.io/badge/Live%20App-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)](https://asifnawaz-healthcare-agent.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-1.3-green?style=for-the-badge)](https://langchain.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

> **AI-powered Healthcare Research Agent** that searches PubMed, analyzes medical literature, and generates professional research reports with citations — downloadable as PDF or Markdown.

---

## 🚀 Live Demo

**[🔬 Try the App →](https://asifnawaz-healthcare-agent.streamlit.app)**

Example queries:
- *"Latest treatments for Type 2 diabetes 2024"*
- *"Pakistan out-of-pocket health expenditure"*
- *"Immunotherapy effectiveness for cancer 2024"*
- *"Long-term effects of COVID-19"*

---

## 🤖 How It Works

```
User Question
      ↓
Research Agent (LangChain + Groq)
      ↓
PubMed API Search → Web Search → Calculator
      ↓
Writer Agent (Llama 3.3-70B)
      ↓
Professional Medical Report + Citations
      ↓
Download as PDF or Markdown
```

---

## 🛠️ Tech Stack

| Component | Tool |
|-----------|------|
| LLM | Llama 3.3-70B via Groq API |
| Framework | LangChain 1.3 |
| Tools | PubMed API, DuckDuckGo Search, Calculator |
| PDF Generation | ReportLab |
| Frontend | Streamlit |
| Deployment | Streamlit Cloud |

---

## 📊 Agent Tools

| Tool | Purpose |
|------|---------|
| `search_pubmed` | Search 35M+ PubMed papers for clinical evidence |
| `web_search` | Latest medical news and statistics |
| `medical_calculator` | Statistical calculations and ratios |

---

## 🗂️ Project Structure

```
healthcare-ai-agent/
│
├── src/
│   ├── tools/
│   │   ├── pubmed_tool.py      # PubMed API integration
│   │   ├── search_tool.py      # Web search tool
│   │   └── calculator_tool.py  # Medical calculator
│   └── agents/
│       └── orchestrator.py     # Research + Writer pipeline
│
├── dashboard/
│   └── streamlit_app.py        # Live web application
│
├── reports/                    # Generated reports saved here
├── requirements.txt
└── README.md
```

---

## 🚀 Run Locally

```bash
# Clone
git clone https://github.com/Asif5588-M/healthcare-ai-agent.git
cd healthcare-ai-agent

# Environment
conda create -n healthcare_agent python=3.11 -y
conda activate healthcare_agent
pip install -r requirements.txt

# Add Groq API key
echo 'GROQ_API_KEY=your_key_here' > .env

# Run
streamlit run dashboard/streamlit_app.py
```

---

## 💡 Use Cases

- Clinical literature review automation
- Medical research report generation
- Drug treatment evidence synthesis
- Healthcare policy research
- Academic thesis support

---

## 👨‍💻 Author

**Asif Nawaz**
- 🏥 Healthcare Data Scientist | PMAS Arid Agriculture University
- 🎓 MPhil Economics (Health Economics)
- 📄 Published Researcher — HEC Y-Category Journal
- 🌐 [Pakistan CHE Dashboard](https://asifnawaz-pakistan-health.streamlit.app)
- 💊 [Drug Sentiment Analyzer](https://asifnawaz-drug-sentiment.streamlit.app)
- 🔬 [Medical RAG System](https://asifnawaz-medical-rag.streamlit.app)
- 🤖 [Healthcare AI Agent](https://asifnawaz-healthcare-agent.streamlit.app)
- 🤗 [HuggingFace](https://huggingface.co/asif-nawaz-ml)
- 🔗 [GitHub](https://github.com/Asif5588-M)