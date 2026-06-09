from langchain.tools import tool

@tool
def web_search(query: str) -> str:
    """
    Search the web for latest medical news and health information.
    Use this tool when you need recent news, statistics,
    or information not in research papers.
    Input: search query
    Output: relevant web results
    """
    try:
        from duckduckgo_search import DDGS
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=4))

        if not results:
            return f"No web results found for: {query}"

        output = []
        for i, r in enumerate(results, 1):
            output.append(
                f"[{i}] {r.get('title', 'N/A')}\n"
                f"    {r.get('body', '')[:300]}...\n"
                f"    URL: {r.get('href', 'N/A')}\n"
            )
        return "\n".join(output)

    except Exception as e:
        return f"Web search unavailable: {str(e)}. Using PubMed only."