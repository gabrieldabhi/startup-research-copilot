def route_query(query):
    """
    Decide which tool should answer the query
    """

    query = query.lower()

    web_keywords = [
        "latest",
        "today",
        "news",
        "recent",
        "trend",
        "update"
    ]

    rag_keywords = [
        "startup",
        "funding",
        "product market fit",
        "venture capital",
        "growth strategy",
        "competitor"
    ]

    for word in web_keywords:
        if word in query:
            return "web"

    for word in rag_keywords:
        if word in query:
            return "rag"

    return "llm"

def explain_route(route):

    if route == "rag":
        return "This question relates to startup knowledge, so the system retrieved information from the internal knowledge base using RAG."

    elif route == "web":
        return "This question likely requires recent or real-time information, so the system performed a live web search."

    else:
        return "This question can be answered using general reasoning, so the language model generated the answer directly."