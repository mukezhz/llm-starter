from bs4 import BeautifulSoup
import requests


def get_text_from_url(url: str) -> tuple[str, str]:
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return "", "Failed to retrieve the webpage"
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.title.string or "" if soup.title else "No title found"
    for unwanted_tag in soup(["script", "style", "header", "footer", "nav"]):
        unwanted_tag.decompose()

    text = soup.get_text(separator="\n", strip=True) or ""
    return title, text


url = "https://mukesh.name.np"
clean_text = get_text_from_url(url)

if clean_text and __name__ == "__main__":
    print(clean_text)
