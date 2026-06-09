# src/tools/search_tool.py
from langchain.tools import tool
from ddgs import DDGS   # ← Changed here

@tool
def web_search(query: str, max_results: int = 5) -> str:
    """
    Search the web for latest medical news, statistics, and general health information.
    """
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(
                keywords=query, 
                max_results=max_results,
                region="wt-wt",      # world-wide
                safesearch="moderate"
            ))
        
        if not results:
            return f"No web results found for: {query}. Try a simpler query."

        output = []
        for i, r in enumerate(results, 1):
            title = r.get('title', 'N/A')
            body = (r.get('body') or r.get('snippet', ''))[:280]
            href = r.get('href', 'N/A')
            output.append(
                f"**{i}. {title}**\n"
                f"{body}...\n"
                f"URL: {href}\n"
            )
        
        return "\n---\n".join(output)
        
    except Exception as e:
        return f"Web search error: {str(e)}"