from tavily import TavilyClient
from config.config import TAVILY_API_KEY


client = TavilyClient(api_key=TAVILY_API_KEY)


def search_web(query):

    try:

        response = client.search(
            query=query,
            max_results=3
        )

        results = []

        for r in response["results"]:
            results.append({
                "title": r["title"],
                "content": r["content"],
                "url": r["url"]
            })

        return results

    except Exception as e:

        print("Web search error:", e)
        return []