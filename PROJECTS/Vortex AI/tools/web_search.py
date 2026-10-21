from ddgs import DDGS

def web_search(query: str) -> str:
    """Search the web and return titles, snippets, and URLs."""
    if not query or not query.strip():
        raise ValueError("Search query cannot be empty.")

    if len(query) > 500:
        raise ValueError("Search query is too long.")

    try:
        results = DDGS().text(query, max_results=5)

        if not results:
            return "No search results were found."

        formatted_results = []

        for index, result in enumerate(results, start=1):
            title = result.get("title", "Untitled")
            snippet = result.get("body", "No description available.")
            url = result.get("href", "No URL available.")

            formatted_results.append(
                f"{index}. {title}\n"
                f"   Summary: {snippet}\n"
                f"   URL: {url}"
            )

        return "\n\n".join(formatted_results)

    except Exception as exc:
        return f"Web search failed: {type(exc).__name__}: {exc}"
