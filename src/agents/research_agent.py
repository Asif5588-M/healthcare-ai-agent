from crewai import Agent
from langchain_core.tools import Tool
from src.tools.pubmed_tool import search_pubmed
from src.tools.search_tool import web_search
from src.tools.calculator_tool import medical_calculator

def create_research_agent():
    """Create Research Agent with CrewAI compatible tools"""
    
    tools = [
        Tool(
            name="search_pubmed",
            func=search_pubmed.invoke,
            description="Search PubMed for medical research papers, clinical trials, and scientific evidence. Best for evidence-based medicine."
        ),
        Tool(
            name="web_search",
            func=web_search.invoke,
            description="Search the web for latest medical news, guidelines, statistics, and general health information."
        ),
        Tool(
            name="medical_calculator",
            func=medical_calculator.invoke,
            description="Perform medical calculations, statistics, percentages, averages, and ratios."
        ),
    ]

    return Agent(
        role="Senior Medical Researcher",
        goal="Conduct thorough and accurate medical research using scientific papers and latest data.",
        backstory="""You are a world-class medical researcher. 
        You specialize in finding high-quality clinical studies from PubMed and reliable sources.
        You are precise, evidence-based, and always cite your sources.""",
        tools=tools,
        verbose=True,
        allow_delegation=False,
        llm="groq/llama-3.3-70b-versatile",
        max_iter=15,
    )