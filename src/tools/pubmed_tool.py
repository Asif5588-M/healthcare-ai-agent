import requests
import xml.etree.ElementTree as ET
from langchain.tools import tool

@tool
def search_pubmed(query: str) -> str:
    """
    Search PubMed for medical research papers.
    Use this tool when you need to find clinical evidence,
    research papers, or medical literature on any health topic.
    Input: medical search query (e.g. 'diabetes treatment 2024')
    Output: top 5 relevant papers with titles, abstracts, authors
    """
    try:
        # Step 1 — Search IDs
        search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        search_params = {
            "db"     : "pubmed",
            "term"   : query,
            "retmax" : 5,
            "retmode": "json",
            "sort"   : "relevance",
            "datetype": "pdat",
            "mindate": "2020",
        }
        r = requests.get(search_url, params=search_params, timeout=15)
        pmids = r.json()["esearchresult"]["idlist"]

        if not pmids:
            return f"No papers found for: {query}"

        # Step 2 — Fetch details
        fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
        fetch_params = {
            "db"     : "pubmed",
            "id"     : ",".join(pmids),
            "retmode": "xml",
            "rettype": "abstract",
        }
        r2 = requests.get(fetch_url, params=fetch_params, timeout=30)
        root = ET.fromstring(r2.content)

        results = []
        for i, article in enumerate(root.findall(".//PubmedArticle"), 1):
            title_el    = article.find(".//ArticleTitle")
            abstract_el = article.findall(".//AbstractText")
            journal_el  = article.find(".//Journal/Title")
            year_el     = article.find(".//PubDate/Year")
            pmid_el     = article.find(".//PMID")

            title    = title_el.text if title_el is not None else "N/A"
            abstract = " ".join((el.text or "") for el in abstract_el)[:400]
            journal  = journal_el.text if journal_el is not None else "N/A"
            year     = year_el.text if year_el is not None else "N/A"
            pmid     = pmid_el.text if pmid_el is not None else "N/A"

            results.append(
                f"[{i}] {title}\n"
                f"    Journal: {journal} ({year})\n"
                f"    PMID: {pmid}\n"
                f"    Abstract: {abstract}...\n"
                f"    URL: https://pubmed.ncbi.nlm.nih.gov/{pmid}/\n"
            )

        return "\n".join(results)

    except Exception as e:
        return f"PubMed search error: {str(e)}"