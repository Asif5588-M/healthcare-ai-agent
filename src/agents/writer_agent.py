from crewai import Agent

def create_writer_agent():
    return Agent(
        role="Medical Report Writer",
        goal="Write clear, well-structured, professional, and citation-rich medical research reports.",
        backstory="""You are an expert medical writer who creates comprehensive, easy-to-understand reports 
        for doctors and researchers. You excel at organizing information, citing sources properly, 
        and making complex medical topics readable.""",
        verbose=True,
        allow_delegation=False,
        llm="groq/llama-3.3-70b-versatile"
    )