import requests
from bs4 import BeautifulSoup

def search(query: str) -> str:
    """
    Searches the web for the given query and returns the text content of the first result.

    Args:
        query: The query to search for.

    Returns:
        The text content of the first search result, or an error message if the search fails.
    """
    try:
        response = requests.get(f"https://www.google.com/search?q={query}")
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        # This is a simplified approach and might not work for all Google search result layouts.
        # A more robust solution would use a dedicated search API.
        search_results = soup.find_all("div", class_="BNeawe vvjwJb AP7Wnd")
        if search_results:
            return search_results[0].get_text()
        else:
            return "No search results found."
    except requests.exceptions.RequestException as e:
        return f"An error occurred during the web search: {e}"
