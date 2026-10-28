from tavily import TavilyClient
from dotenv import load_dotenv
from langchain.tools import tool
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

load_dotenv()

tavily_client = TavilyClient()

@tool
def web_search(query: str) -> list[dict[str, str]]:
    """Search the web for recipe, cooking, and ingredient information."""

    logging.info("Searching the web for: %s", query)

    try:
        response = tavily_client.search(
            query=query,
            max_results=3,
        )

        results = [
            {
                "title": item.get("title", ""),
                "content": item.get("content", "")[:1000],
                "url": item.get("url", ""),
            }
            for item in response.get("results", [])
        ]

        logging.info("Tavily returned %d results", len(results))

        for result in results:
            logging.info(
                "Recipe search result: %s | %s",
                result["title"],
                result["url"],
            )

        return results

    except Exception:
        logging.exception("Tavily search failed")
        raise
